from flask import Flask
from flask import jsonify
from flask import request
import json

def get_conversion(conversion_id, conversion_name):
    if not conversion_id:
        msg = "conversion_id不能为空"
    else:
        conversion_id = conversion_id
        conversion_name = conversion_name
        msg = "success"
    return {"conversion_id": conversion_id, "conversion_name": conversion_name}, msg




app = Flask(__name__)           # 实例化一个web服务对象

@app.route('/conversion', methods=["POST"])
def get_conversion():
    # date = request.get_date()
    conversion_id = request.json.get("conversion_id")      # 转化id
    conversion_name = request.json.get("conversion_name")     # 转化名称
    # conversion_id = request.json.get('conversion_id')
    # conversion_name = request.values.get('conversion_name')

    # conversion_id = 123
    # conversion_name = "test123111111111111"
    # if conversion_id:
    return jsonify({"conversion_id":conversion_id, "conversion_name": conversion_name})
    # response = {"conversion_id": conversion_id, "conversion_name": conversion_name}
    # return json.dumps(response, ensure_ascii=False)

# from flask import request, Flask, jsonify
#
# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False


# @app.route('/test', methods=['POST'])
# def post_Data():
#     print('hh')
#     postdata = request.form['id']
#     file = request.files['file']
#     recognize_info = {'id': postdata, 'info': '收到'+file.filename}
#     return jsonify(recognize_info), 201

#
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0', port=8888)

if __name__ == "__main__":
    app.run()
    # import requests, json
    #
    # headers = {"Content-Type": "application/json"}
    #
    # base_url = "http://127.0.0.1:5000/"
    #
    # conversion_url = base_url + '/conversion'
    # request_data = {
    #     "conversion_id": 123,
    #     "conversion_name": "testst"
    # }
    #
    # res = requests.post(conversion_url, headers=headers, data=json.dumps(request_data))
    #
    # print(res.json())


    '''
    # flask.request方法
    https://www.cnblogs.com/leijiangtao/p/11757639.html         
    https://www.cnblogs.com/amengmeng/p/8361416.html 
    # flask mysql, flask.request.values
    https://www.cnblogs.com/sunzzc/p/13416348.html  
    https://www.cnblogs.com/neozheng/p/10440405.html            
    # flask.request.json
    https://zhuanlan.zhihu.com/p/98029804
    https://blog.csdn.net/u011559236/article/details/88708534
    https://blog.csdn.net/ling620/article/details/107562294
    https://www.cnblogs.com/wintest/p/12731508.html
    
    '''
