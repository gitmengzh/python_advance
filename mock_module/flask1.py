from flask import Flask
from flask import request



app = Flask(__name__)           # 实例化一个web服务对象

@app.route('/conversion', methods="POST")
def get_conversion():
    pass


