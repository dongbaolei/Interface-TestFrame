# -*- coding:utf-8 -*-
"""
@Time:2018/1/26 15:46
@Author:dongbaolei
"""

import pymysql
from requests import ConnectionError


class GetCarID:
    global host, username, password, port, database, config
    # rd=ReadConfig.ReadConfig()
    # host=rd.get_db('host')
    # username = rd.get_db("username")
    # password = rd.get_db("password")
    # port = rd.get_db("port")
    # database =rd.get_db("dbname")
    # database = "yoolifin"

    config = {
        'host': "192.168.2.125",
        'user': "root",
        'passwd': "admin12345",
        'port': 3306,
        'db': "lz_appr"
    }

    def __init__(self):
        self.db = None
        self.cursor = None

    # 创建连接和游标
    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            print("Connect DB successfully!")
        except ConnectionError as ex:
            print(ex)

    def executeSQL(self, sql):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def exeCallprocMoreParam(self, ProName, Paramdate, ParamInt, ParamType):
        self.connectDB()
        cur = self.db.cursor()
        # self.cursor.callproc('SP_REPAYMENT',args=('2017-12-23',5,1))
        # self.cursor.callproc(ProName,args=(param,param1,param1))
        # self.cursor.fetchone()
        for i in range(2):
            cur.nextset()
            print(ProName)
            cur.execute('call ' + ProName + '(%s,%s,%s)', (Paramdate, ParamInt, ParamType))

            # cur.execute('call SP_REPAYMENT(%s,%s,%s)', ('2017-12-23',5,1))
            # cur.commit()
            # row_one = self.cursor.fetchone()
            # text='diaoyong wanbi'
            # print text
            # self.db.commit
            # return text

    def exeCallprocSignParam(self, ProName, Param):
        self.connectDB()
        cur = self.db.cursor()
        cur.nextset()
        print(ProName)

        cur.execute('call ' + ProName + '(%s)', (Param))

    def closeDB(self):
        self.db.close()
        print("Database closed!")

    def getCarID(self, app_code):
        carid = self.executeSQL("select * from ca_car_info where app_code='%s'" % app_code)
        cardata = self.get_one(carid)
        return cardata['id']


if __name__ == '__main__':
    mydb = GetCarID()
    #mydb.connectDB()
    print(mydb.getCarID('K18041750000031005'))
    # 短信查询
    # cc=mydb.executeSQL("select send_content from t_send_log where params='13818764294'")

    # cc = mydb.executeSQL("update ca_app_info set STATUS=32 where app_code='K18041750000031005'")
    #cc = mydb.executeSQL("select * from ca_car_info where app_code='K18041750000031005'")
    # print(mydb.get_one(cc))
    #test_data = mydb.get_one(cc)

    # d=json.loads(test_data["send_content"])
    # print(d.get("keyValue")['code'])

    #print(test_data['id'])

    # appcode = Fast_Apply.Get_appCode()
    # print appcode
    # sqlone_data = DataBaseUtil()
    # sqlone = "select STATUS from ca_app_info where APP_CODE='L1712271000100102009'"
    # cc=sqlone_data.executeSQL( "select STATUS from ca_app_info where APP_CODE='L1712271000100102009'")
    # print sqlone
    # print sqlone_data.get_one(cc)['STATUS']
    # 执行存储过程
    # sqlone_data.exeCallprocMoreParam('SP_REPAYMENT', '2017-12-23', 4, 1)
    # sqlone_data.exeCallprocSignParam('SP_REPAYMENT_UPDATE', 23)
    # print sqlone_data
    # sqlone_data.closeDB()
