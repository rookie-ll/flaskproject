from flask import Flask,session,redirect
app=Flask(__name__)
app.config["SECRET_KEY"]="SDFAGASFSFDSFAsdfasdfadsfsadf"

@app.route("/login")
def login():
    session["name"]="laowang"
    session["age"]="wwwwww"
    return "ok"

@app.route("/index")
def index():
    a=session.get("name")
    return a