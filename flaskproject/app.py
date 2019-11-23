from flask import Flask,request,Response,abort,make_response,jsonify

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    #name=request.form.get("name")
    #value=request.form.get("value")
    name=request.form.get("name")
    value=request.form.get("value")
    age=request.args.get("age")
    fil=request.files.get("pic")
    with open("./demo.png","wb") as f:
        dat=fil.read()
        f.write(dat)
    #使用abort函数可以立即终止函数的运行
    #1.传递响应体状态吗
    #abort(404)
    #2.传递响应提信息
   # ret=Response("slfjdsklfj")
    #abort(ret)
   # res=make_response()
    return "name:%s,value:%s,age:%s"%(name,value,age)

if __name__ == '__main__':
    app.run()