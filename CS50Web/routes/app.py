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
