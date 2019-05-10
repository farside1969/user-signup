from flask import Flask, request, redirect, render_template
import cgi, html, os, jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

#form
@app.route('/signup')
def display_user_signup_form():
    return render_template('signup.html')

# validation
def empty_val(x):
    if x:
        return True
 
def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True

def email_at_symbol_more_than_one(x):
    if x.count('@') <= 1:
        return True

def email_period(x):
    if x.count('.') >= 1:
        return True

def email_period_more_than_one(x):
    if x.count('.') <= 1:
        return True

#process form
@app.route("/signup", methods=['POST'])
def user_signup_complete():

#input varibles
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']

#errors
    username_error = ""
    password_error = ""
    password_verify_error = ""
    email_error = ""

    err_required = "Required"
    err_reenter_pw = "Verify password"
    err_char_count = "Must be 3 to 20 characters"
    err_no_spaces = "Must not contain spaces"

#username validation
    if not empty_val(username):
        username_error = err_required
        password = ''
        password_verify = ''
        password_error = err_reenter_pw
        password_verify_error = err_reenter_pw
    elif not char_length(username):
        username_error = "Username " + err_char_count
        password = ''
        password_verify = ''
        password_error = err_reenter_pw
        password_verify_error = err_reenter_pw
    else:
        if " " in username:
            username_error = "Username " + err_no_spaces
            password = ''
            password_verify = ''
            password_error = err_reenter_pw
            password_verify_error = err_reenter_pw

#password validation
    if not empty_val(password):
        password_error = err_required
        password = ''
        password_verify = ''
    elif not char_length(password):
        password_error = "Password " + err_char_count
        password = ''
        password_verify = ''
        password_verify_error = err_reenter_pw
    else:
        if " " in password:
            password_error = "Password " + err_no_spaces
            password = ''
            password_verify = ''
            password_verify_error = err_reenter_pw

#verify password validation
    if password_verify != password:
        password_verify_error = "Passwords do not match"
        password = ''
        password_verify = ''
        password_error = 'Passwords must match'

#e-mail validation
    if empty_val(email):
        if not char_length(email):
            email_error = "Email " + err_char_count
            password = ''
            password_verify = ''
            password_error = err_reenter_pw
            password_verify_error = err_reenter_pw
        elif not email_at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            password_verify = ''
            password_error = err_reenter_pw
            password_verify_error = err_reenter_pw
        elif not email_at_symbol_more_than_one(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            password_verify = ''
            password_error = err_reenter_pw
            password_verify_error = err_reenter_pw
        elif not email_period(email):
            email_error = "Email must contain a . (dot)"
            password = ''
            password_verify = ''
            password_error = err_reenter_pw
            password_verify_error = err_reenter_pw
        elif not email_period_more_than_one(email):
            email_error = "Email must contain only one . (dot)"
            password = ''
            password_verify = ''
            password_error = err_reenter_pw
            password_verify_error = err_reenter_pw
        else:
            if " " in email:
                email_error = "E-mail " + err_no_spaces
                password = ''
                password_verify = ''
                password_error = err_reenter_pw
                password_verify_error = err_reenter_pw

#no error redirects to welcome
#error will display error message
    if not username_error and not password_error and not password_verify_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, username=username, password_error=password_error, password=password, password_verify_error=password_verify_error, password_verify=password_verify, email_error=email_error, email=email)

#redirect to welcome
@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

if __name__ == '__main__':

    app.run()