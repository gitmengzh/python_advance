import pymysql

class OpeMysql(object):
    def __init__(self, mysql_base_data):
        self.dbhost = mysql_base_data.get('dbhost')
        self.dbuser = mysql_base_data.get('dbuser')
        self.dbpwd = mysql_base_data.get('dbpwd')
        self.dbname = mysql_base_data.get('dbname')
        self.dbport = mysql_base_data.get('dbport')

    @classmethod
    def connect_mysql(self):


        try:
            conn = pymysql.connect(host=self.dbhost,
                                 user=self.dbuser,
                                 password =self.dbpwd,
                                 port=self.dbport,
                                 database=self.dbname,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor
                                 )

            return conn

        except pymysql.Error as e:
            return ('数据库连接失败' + str(e))
    @classmethod
    def operate_mysql(sql):
        conn =
        with conn:
            with conn.cursor() as cursor:
        cur.
        conn = pymysql.connect(host=setting.MYSQL_HOST, user=setting.USER,
                               7

        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        12  # 判断是否需要commit，根据select update delete insert的类型
        13
        cur.execute(sql)
        14
        sql_start = sql[:6].upper()  # select不区分大小写,取前6位转换成大写
        15
        if sql_start == 'SELECT':
            16
            res = cur.fetchall()
        17 else:
        18
        conn.commit()
        19
        res = 'ok'
        20
        cur.close()
        21
        conn.close()
        22
        return res

def aaa():
    connection = pymysql.connect(host='101.34.65.89',
                             user='root',
                             password='Dream@1618*',
                             database='test_conversion1',
                             port=9998,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    with connection:
    #     with connection.cursor() as cursor:
    #         # Create a new record
    #         sql = "SELECT * FROM test_conversion_name "
    #         res = cursor.execute(sql)
    # return res
    cursor = connection.cursor()
    return  cursor
if __name__ == "__main__":
    mysql_basedata = {
        "dbhost": "101.34.65.89",
        "dbuser": "root",
        "dbpwd": "Dream@1618*",
        "dbport":9998,
        "dbname": "test_conversion1"
    }
    print(connect_mysql(mysql_basedata))
    # print(aaa())