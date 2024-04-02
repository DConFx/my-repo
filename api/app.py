from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/info')
def get_info():
    return "I am an API"

@app.route('/login')
def get_login():
    return "login page"