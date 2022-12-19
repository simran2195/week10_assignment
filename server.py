# how to use css in python_ flask
# flask render_template example
 
from flask import Flask, render_template
from flask_session import Session
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 
# @app.route('/')
# def welcome():
#     return "This is the home page of Flask Application"
 
@app.route('/')
def index():
    game = [[None, None, None],[None, None, None],[None, None, "X"] ]
    return render_template('index.html', game = game, turn="X")

# @app.route("/<string:name>")
# def hello(name):
#     # name = name.capitalize()
#     # return f"Hello, {name}!"
#     return render_template("index.html", name=name.capitalize())


 
if __name__=='__main__':
    app.run(debug = True)