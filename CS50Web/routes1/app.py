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

@app.route("/<string:name>")
# when a user goes to a / any name, it will call the hello function
# then pass the name value that the user typed in from the url
def hello(name):
    return f"Hello, {name}!"
