from flask import Flask, render_template
from database import Database

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/student-login')
def student_login():
   return render_template('login.html', title='Student')

if __name__ == "__main__":
    app.run()

