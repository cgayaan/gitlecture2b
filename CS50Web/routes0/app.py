from flask import Flask
# import flask from the Flask module
app = Flask(__name__)
# create new web application of type Flask
# __name__ means that this current file represents the web application
@app.route("/")
# Flask is designed in terms of routes
# / means the default page, so when user goes to the default page, the function below is what should run
def index():
# this index function just returns the text Hello world
    return "Hello, world!"

@app.route("/Chamara")
def Chamara():
    return "Hello, Chamara!"
# now once we run do flask run
# http://127.0.0.1:5000/Chamara going to this path will call the def Chamara() function

# similarly we can add another route, run flask run and then navigate to that url route
@app.route("/Riah")
def Riah():
    return "Hello, Riah!"
