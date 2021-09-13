import pymysql

class ConnectMysql():

    def __init__(self, mysql_base_data):
        self.dbhost = mysql_base_data.get('dbhost')
        self.dbuser = mysql_base_data.get('dbuser')
        self.dbpwd = mysql_base_data.get('dbpwd')
        self.dbname = mysql_base_data.get('dbname')
        self.dbport = mysql_base_data.get('dbport')

    def connectMysql(self):
        try:
            conn = pymysql.connect(host=self.dbhost,
                                 user=self.dbuser,
                                 password =self.dbpwd,
                                 port=self.dbport,
                                 database=self.dbname,
                                 charset='utf8mb4',
                                 # cursorclass=pymysql.cursors.DictCursor
                                 )

            # cur = conn.cursor()
            # return cur      # 返回游标
            return conn

        except pymysql.Error as e:
            return ('数据库连接失败' + str(e))

    def operate_mysql(self, sql):
        conn = self.connectMysql()
        with conn:
             with conn.cursor() as cursor:

        # conn = pymysql.connect(host=setting.MYSQL_HOST, user=setting.USER,
        #                        7
        #
        # cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 判断是否需要commit，根据select update delete insert的类型
                cursor.execute(sql)
                sql_start = sql[:6].upper()  # select不区分大小写,取前6位转换成大写
                if sql_start == 'SELECT':
                    res = cursor.fetchall()
                else:
                    conn.commit()



        # cursor.close()

        # conn.close()
        return res



def aaa():
    connection = pymysql.connect(host='101.34.65.89',
                             user='root',
                             password='Dream@1618*12',
                             database='test_conversion1',
                             port=9998,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    #with connection:
    #     with connection.cursor() as cursor:
    #         # Create a new record
    #         sql = "SELECT * FROM test_conversion_name "
    #         res = cursor.execute(sql)
    # return res
    #cursor = connection.cursor()
    #return  cursor
if __name__ == "__main__":
    mysql_basedata = {
        "dbhost": "101.34.65.89",
        "dbuser": "root",
        "dbpwd": "Dream@1618*1",
        "dbport":9998,
        "dbname": "test_conversion1"
    }

    connect = ConnectMysql(mysql_basedata)
    sql = "select * from test_conversion_name"
    res = connect.operate_mysql(sql)
    print(res)