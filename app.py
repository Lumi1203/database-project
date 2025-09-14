from flask import Flask, render_template

app = Flask(__name__)

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

@app.route('/register')
def register():
    return render_template('register.html')