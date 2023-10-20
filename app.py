from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
# 主机名
HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
db = SQLAlchemy(app)
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello 1123!'


@app.route('/blog/<int:id>')  # 带参数的博客列表
def blog_list(id):  # put application's code here
    return f'这是博客列表{id}'


'''1.debug模式==开启热部署
#2.修改host，如果要让局域网的其他电脑可以访问
 可以在配置中修改host为0.0.0.0

 3.修改port端口号
 --port=8000
'''
if __name__ == '__main__':
    app.run()
