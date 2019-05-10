from flask import Flask, request, redirect, render_template
import cgi, html, os, jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

#start page
@app.route('/')
def start():
    return render_template('alt_signup.html')

#form
@app.route('/alt_signup')
def signup():
    return render_template('alt_signup.html')

# validation Booleans
def empty(x):
    if x:
        return True
     
def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True

def email_symbol(x):
    if x.count('@') == 1:
        return True

def email_period(x):
    if x.count('.') == 1:
        return True

#validate form
@app.route('/alt_signup', methods=['POST'])
def validate():

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

    error_required = "Required input"
    error_reenter_pw = "verify password"
    error_char_count = "must be 3 to 20 characters"
    error_no_spaces = "must not contain spaces"

#username validation
    if not empty(username):
        username_error = error_required
        return username_error

    elif not char_length(username):
        username_error = "Username " + error_char_count
        return username_error

    else:
        if " " in username:
            username_error = "Username " + error_no_spaces
            return username_error

#password validation
    if not empty(password):
        password_error = error_required
        return password_error

    elif not char_length(password):
        password_error = "Password " + error_char_count
        return password_error

    else:
        if " " in password:
            password_error = "Password " + error_no_spaces
            return password_error

#verify password validation
    if password_verify != password:
        password_verify_error = "Passwords do not match"
        return password_verify_error

#e-mail validation
    if empty(email):
        if not char_length(email):
            email_error = "Email " + error_char_count
            return email_error
 
        elif not email_symbol(email):
            email_error = "Email must contain one @ symbol"
            return email_error

        elif not email_period(email):
            email_error = "Email must contain one . (dot)"
            return email_error

        else:
            if " " in email:
                email_error = "Email " + error_no_spaces
                return email_error

#no error redirects to welcome
#error will display error message
    if not username_error and not password_error and not password_verify_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('alt_signup.html', username_error=username_error, username=username, password_error=password_error, password=password, password_verify_error=password_verify_error, password_verify=password_verify, email_error=email_error, email=email)

#redirect to welcome
@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run()
