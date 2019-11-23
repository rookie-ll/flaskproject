#coding=utf-8
from flask import Flask,render_template,session,redirect,url_for

#导入wtf扩展的表单类
from flask_wtf import FlaskForm
#导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField
#导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
app = Flask(__name__)
app.config['SECRET_KEY']='hgjhghjtfghv67'

#自定义表单类，文本字段、密码字段、提交按钮
class Loginfrom(FlaskForm):
    us = StringField(label=u'用户：',validators=[DataRequired(u"此字段不可为空")])
    ps = PasswordField(label=u'密码',validators=[DataRequired(u"此字段不可为空")])
    ps2 = PasswordField(label=u'确认密码',validators=[DataRequired(u"确认秘密不能为空"),EqualTo("ps","俩次密码不同")])
    submit = SubmitField(u'提交')

@app.route('/login',methods=['GET','POST'])
def login():
    form=Loginfrom()
    if form.validate_on_submit():
        us1=form.us.data
        ps1=form.ps.data
        ps21=form.ps2.data
        session["user_name"]=us1
        print(us1,ps1,ps21)
        return redirect(url_for("index"))
    return render_template('login.html', form=form)

@app.route("/index")
def index():
    name=session.get("user_name",'')
    return "hello %s" % name
if __name__ == '__main__':
    app.run()