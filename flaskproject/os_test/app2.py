from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/index/<int:id>/', methods=['GET', 'POST'])
def index(id):
    # res=request.form.get("value1")
    res = request.form.get("id")
    print(res)
    date = [{"id": 1, "名字": "wowoowow", "age": 22}, {"id": 2, "名字": "757575oowow", "age": 52}]
    for i in date:
        if i.get("id") == id:
            return jsonify(i.get("名字"))
        else:
            return jsonify(date)
    # json.dumps(字典) 将python的字典转换为json字符串
    # json.loads(字符串) 将字符串转换为python中的字典

    # json_str = json.dumps(data)
    #
    # return json_str, 200, {'Content-Type': 'application/json'}

    # jsonify帮助转为json数据，并设置响应头 Content-Type 为 application/json


@app.route("/", methods=["GET", "POST"])
def emm():
    # try:
    #     pass
    # except Exception as e:
    #     print(e)
    # else:
    #     pass
    # finally:
    #     pass

    date = [{"id": 1, "名字": "wowoowow", "age": 22}, {"id": 2, "名字": "757575oowow", "age": 52}]


    return jsonify(date)

    # return res


if __name__ == "__main__":
    app.run(host="0.0.0.0")
