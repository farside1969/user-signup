from flask import Flask, request, redirect, render_template
import cgi, html, os, jinja2

#MEGA FLOW ISSUE - REFLOW

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/signup", methods=['POST'])
def sign_up():
    user_name = request.form['user_name']
    return render_template('signup.html', user_name=user_name)

@app.route("/welcome", methods=['POST'])
def welcome():
    user_name = request.form['user_name']
    return render_template('welcome.html', user_name=user_name)

if __name__ == '__main__':

    app.run()