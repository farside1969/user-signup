from flask import Flask, request, redirect, render_template
import cgi, html, os, jinja2

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("base.html")
#@app.route("/")
#def index():
#    template = jinja_env.get_template('hello_form.html')
#    return template.render()    

@app.route("/base", methods=['POST'])
def encrypt():
    user = request.form['user_input']
    return render_template('base.html', user=user)
    

if __name__ == '__main__':

    app.run()