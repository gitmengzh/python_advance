# https://pymysql.readthedocs.io/en/latest/user/examples.html   pymysql doc
import pymysql


# class OpeMysql(object):
#     def __init__(self, mysql_base_data):
#         self.dbhost = mysql_base_data.get('dbhost')
#         self.dbuser = mysql_base_data.get('dbuser')
#         self.dbpwd = mysql_base_data.get('dbpwd')
#         self.dbname = mysql_base_data.get('dbname')
#         self.dbport = mysql_base_data.get('dbport')
#
#     @classmethod
#     def connect_mysql(self):
#
#
#         try:
#             conn = pymysql.connect(host=self.dbhost,
#                                  user=self.dbuser,
#                                  password =self.dbpwd,
#                                  port=self.dbport,
#                                  database=self.dbname,
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor
#                                  )
#
#             return conn
#
#         except pymysql.Error as e:
#             return ('数据库连接失败' + str(e))
#     @classmethod
#     def operate_mysql(sql):
#         pass
#         # conn = pymysql.connect(host=setting.MYSQL_HOST, user=setting.USER,
#         # cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#         # with conn:
#         #     with conn.cursor() as cursor:
#         #         cursor.execute(sql)
#         #         sql_start = sql[:6].upper()  # select不区分大小写,取前6位转换成大写
#         #         if sql_start == 'SELECT':
#         #         res = cur.fetchall()
#         #     else:
#         #         conn.commit()
#         #         res = 'ok'
#         #         cur.close()
#         # conn.close()
#         # return res
#
# def aaa():
#     connection = pymysql.connect(host='101.34.65.89',
#                              user='root',
#                              password='Dream@1618*',
#                              database='test_conversion1',
#                              port=9998,
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#     with connection:
#         with connection.cursor() as cursor:
#             # Create a new record
#             sql = "SELECT * FROM test_conversion_name "
#             res = cursor.execute(sql)
#     return res
#     cursor = connection.cursor()
#     return  cursor

def connect_mysql(info,sql):
    try:
        conn = pymysql.connect(host=info['dbhost'],
                               user=info['dbuser'],
                               password=info['dbpassword'],
                               port=info['dbport'],
                               database=info['dbname'],
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor
                               )
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
        return cur.fetchall()
    except pymysql.Error as e:
        return ('数据库连接失败' + str(e))



if __name__ == "__main__":
    mysql_basedata = {
        "dbhost": "101.34.65.89",
        "dbuser": "root",
        "dbpassword": "Dream@1618*",
        "dbport":9998,
        "dbname": "test_conversion1"
    }
    sql = 'select conversion_name from test_conversion_name where conversion_id = 10001'
    res = connect_mysql(mysql_basedata,sql)
    print(res)
