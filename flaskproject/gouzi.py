from flask import Flask,request
app=Flask(__name__)

@app.route('/index')
def index():
    print("index 被执行")
    return "hello word"
@app.before_first_request
def frist_gz():
    print("只执行一次的钩子被执行")

@app.before_request
def frist_ergz():
    print("开头执行的钩子执行了")

@app.after_request
def after_gz(request):
    print("后面的钩子被执行")
    return request

@app.teardown_request
def after_afgz(request):
    print("最后的钩子执行了")
    return request

if __name__=="__main__":
    app.run()