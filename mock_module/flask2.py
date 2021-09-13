from flask import Flask
from flask import request
from flask import jsonify
from connect_mysql import ConnectMysql
base_data  = {
        "dbhost": "101.34.65.89",
        "dbuser": "root",
        "dbpwd": "Dream@1618*1",
        "dbport":9998,
        "dbname": "test_conversion1"
    }

connectmysql = ConnectMysql(base_data)
app = Flask(__name__)


@app.route('/conversion', methods=['POST'])
def get_conversion():
    account_id = request.json.get("account_id")
    conversion_id = request.json.get("conversion_id")
    sql = 'select * from test_conversion_name where conversion_account = %s and conversion_id = %s' %(account_id, conversion_id)
    res = connectmysql.operate_mysql(sql)
    return jsonify({"data": res})



if __name__ == "__main__":
    app.run()


# 复杂数据如何返回
# 按照请求转化的接口编写完成

