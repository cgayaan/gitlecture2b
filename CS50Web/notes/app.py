from flask import Flask, render_template, request, session
#from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

notes = []
# empty list to store the notes that we will be saving

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
    # if request is POST add a new note the notes list variable
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", notes=notes)
    # if request is not POST or even if it is...
    # return the index.html page with all the notes values
