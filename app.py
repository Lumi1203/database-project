from flask import Flask, render_template, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from certificates import valid_certificate_numbers
from models import db, User, Accident, FirstAiderRegistry
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from dotenv import load_dotenv
import re

load_dotenv()

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


with app.app_context():
    db.init_app(app)
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f"Welcome, {user.firstname}! You are now logged in.")
            return redirect(url_for('accident'))
        else:
            flash('Incorrect email or password. Please try again.')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/accident', methods=['GET', 'POST'])
@login_required
def accident():

    first_aiders = User.query.filter_by(firstaider=True).all()

    if request.method == 'POST':
        title = request.form['title']
        type_ = request.form['type']
        description = request.form['description']
        location = request.form['location']
        date_str = request.form['date']
        time_str = request.form['time']
        firstaid = request.form['firstaid']
        firstaider_id = request.form.get('firstaider')
        firstaiddetails = request.form['firstaiddetails']

        date_of_accident = datetime.strptime(date_str, '%Y-%m-%d').date()
        time_of_accident = datetime.strptime(time_str, '%H:%M').time()

        first_aid_administered = True if firstaid == "Yes" else False
        firstaider_id = int(firstaider_id) if firstaider_id else None

        new_accident = Accident(
            title=title,
            type=type_,
            description=description,
            location=location,
            date_of_accident=date_of_accident,
            time_of_accident=time_of_accident,
            first_aid_administered=first_aid_administered,
            first_aider_id=firstaider_id,
            first_aid_details=firstaiddetails,
            reporter_id=current_user.id
        )

        db.session.add(new_accident)
        db.session.commit()

        flash('Accident report submitted successfully.')
        return redirect(url_for('index'))

    return render_template('accident.html', first_aiders=first_aiders)

@app.route('/view')
@login_required
def view():
    if not current_user.firstaider:
        flash("Access denied: Only First Aiders can view the accident logs.")
        return redirect(url_for('index'))

    accidents = Accident.query.order_by(Accident.date_reported.desc()).all()
    #first_aiders = FirstAiderRegistry.query.all()
    return render_template('view.html', accidents=accidents)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        surname = request.form['surname']
        email = request.form['email']
        staffnumber = request.form['staffnumber']
        firstaider = request.form['firstaider']
        cert_number = request.form.get('firstaidernumber', '').strip()
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match.')
            return render_template('register.html')
        
        if '@' not in email:
            flash('Please enter a valid email address.')
            return render_template('register.html')

        if password != confirm_password:
            flash('Passwords do not match.')
            return render_template('register.html')

        if len(password) < 8:
            flash('Password must be at least 8 characters long.')
            return render_template('register.html')

        if not re.search(r'[A-Z]', password):
            flash('Password must contain at least one uppercase letter.')
            return render_template('register.html')

        if not re.search(r'[^A-Za-z0-9]', password):
            flash('Password must contain at least one special character.')
            return render_template('register.html')


        if firstaider == 'Yes':
            if not cert_number:
                flash('Certificate number is required for First Aiders.')
                return render_template('register.html')
            if cert_number not in valid_certificate_numbers:
                flash('Invalid First Aider Certificate Number.')
                return render_template('register.html')

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return render_template('register.html')

        # Create new user
        new_user = User(
            firstname=firstname,
            surname=surname,
            email=email,
            staffnumber=staffnumber,
            firstaider=(firstaider == 'Yes'),
            certificate_number=cert_number if firstaider == 'Yes' else None,
            password_hash=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))


@app.route('/first_aider_registry')
@login_required
def first_aider_registry():
    if not current_user.firstaider:
        flash("Access denied: Only First Aiders can view the accident logs.")
        return redirect(url_for('index'))

    first_aiders = FirstAiderRegistry.query.all()
    return render_template('view.html', first_aiders=first_aiders)
