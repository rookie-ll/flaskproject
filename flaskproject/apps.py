from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", a=app.url_map, b="sssss", c=111)

@app.route("/hello")
def hello():
    return "hello word"

if __name__=="__main__":
    app.run()