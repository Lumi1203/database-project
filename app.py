from flask import Flask, render_template, render_template, request, redirect, url_for, flash
from certificates import valid_certificate_numbers

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/accident')
def accident():
    return render_template('accident.html')

@app.route('/view')
def view():
    return render_template('view.html')

#@app.route('/register')
# def register():
#    return render_template('register.html')

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

        # Password match check
        if password != confirm_password:
            flash('Passwords do not match.')
            return render_template('register.html')

        # If first aider selected "Yes", validate certificate number
        if firstaider == 'Yes':
            if not cert_number:
                flash('Certificate number is required for First Aiders.')
                return render_template('register.html')
            if cert_number not in valid_certificate_numbers:
                flash('Invalid First Aider Certificate Number.')
                return render_template('register.html')

        # TODO: Save user to database

        flash('Registration successful! Please log in.')
        return render_template('login.html')

    return render_template('register.html')
