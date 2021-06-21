

import pymysql

#本月客流量
def getApril():
    db = pymysql.connect(host='localhost', user='root', password='root', database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select * from july")
    data = cursor.fetchall()
    db.commit()
    db.close
    return data

#年龄结构分布
def getAge():
    db = pymysql.connect(host='localhost', user='root', password='root', database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select sum(number) from useragecount where age>60")
    data1 = cursor.fetchall()
    cursor.execute("select sum(number) from  useragecount where age<=60 and age >=46")
    data2 = cursor.fetchall()
    cursor.execute("select sum(number) from  useragecount where age<=45 and age >=19")
    data3 = cursor.fetchall()
    cursor.execute("select sum(number) from  useragecount where age<=18 and age >=10")
    data4 = cursor.fetchall()
    db.commit()
    db.close
    return [data1, data2, data3, data4]

#明日拥挤站点预测
def getPrediction():
    db = pymysql.connect(host='localhost', user='root', password='root', database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select list,July17 from prediction order by July17 desc limit 10")
    data = cursor.fetchall()
    db.commit()
    db.close
    return data

#断面客流量
def getFlowBetween():
    db = pymysql.connect(host='localhost', user='root', password='root', database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select * from line1")
    data = cursor.fetchall()
    db.commit()
    db.close
    return data


#入站、出站客流
def getStationFlow():
    db = pymysql.connect(host='localhost', user='root', password='root',
                            database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select count(*) from trips where entername='Sta154' GROUP BY entername")
    data5 = cursor.fetchall()
    cursor.execute("select count(*) from trips where exitname='Sta154' GROUP BY exitname")
    data6 = cursor.fetchall()
    db.commit()
    db.close
    return [data5, data6]

#今日、本周、本月客流
def getStationCount():
    db = pymysql.connect(host='localhost', user='root', password='root',
                            database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select sum(Sta154) from everyday where exactdate='2020-07-16'")
    data7 = cursor.fetchall()
    cursor.execute("select sum(Sta154) from everyday where exactdate<='2020-07-16' and exactdate>='2020-07-13'")
    data8 = cursor.fetchall()
    cursor.execute("select sum(Sta154) from everyday where exactdate<='2020-07-16' and exactdate>='2020-07-01'")
    data9 = cursor.fetchall()
    db.commit()
    db.close
    return [data7, data8, data9]

def getStationPrediction():
    db = pymysql.connect(host='localhost', user='root', password='root',
                            database='subway', port=3306, charset='utf8')
    cursor = db.cursor()
    cursor.execute("select July17,July18,July19,July20,July21,July22,July23,July24,July25,July26,July27,July28,July29,July30,July31 from prediction where list=154")
    data = cursor.fetchall()
    db.commit()
    db.close
    return data



