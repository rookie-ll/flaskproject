from flask import Flask,jsonify,render_template,flash,g
app=Flask(__name__)
flag=True
app.config['SECRET_KEY']='SFSADGAASFSA'
app.config['DEBUG']=True


@app.route('/')
def index():
    # noinspection PyInterpreter
    g.username = "kdslfjl"
    print(type(g))
    print(g.__dir__())
    if flag:
        flash("hello")
        flash("hello")
        flash("hello")
        #global flag
        #flag=False

    return render_template('tobase.html')

if __name__=="__main__":
    app.run()