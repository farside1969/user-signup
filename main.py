from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/base", methods=['POST'])
def encrypt():
    user = request.form['user_input']
    return render_template('base.html', user=user)
    

if __name__ == '__main__':

    app.run()