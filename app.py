from flask import Flask, render_template
import pymysql
import services666

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/index1')
def index1():
    #本月客流量统计
    april = services666.getApril()[0]
    april1 = []
    for i in  range(0,len(april)):
        april1.append(int(april[i]))

    #客流年龄结构分布
    old = services666.getAge()[0][0][0]
    middleAged = services666.getAge()[1][0][0]
    teen = services666.getAge()[2][0][0]
    youth = services666.getAge()[3][0][0]

    #明日拥挤站点预测
    prediction = services666.getPrediction()
    sta = []
    flow = []
    for i in range(0, 9):
        sta.append(prediction[i][0])
        flow.append(prediction[i][1])

    #断面客流量
    line1 = services666.getFlowBetween()
    line1Up = []
    line1Down = []
    for i in range(1, 19):
        line1Up.append(line1[0][i])
        line1Down.append(line1[1][i])

    return render_template('index1.html', april=april1, old=old, middleAged=middleAged, teen=teen, youth=youth, sta=sta,
                           flow=flow, line1Up=line1Up, line1Down=line1Down)

@app.route('/map')
def map():

    return render_template('map.html')

@app.route('/station154')
def station():

    enterStation = services666.getStationFlow()[0][0][0]
    exitStation = services666.getStationFlow()[1][0][0]

    count1 = services666.getStationCount()[0][0][0]
    count2 = services666.getStationCount()[1][0][0]
    count3 = services666.getStationCount()[2][0][0]

    sta = services666.getStationPrediction()
    stationPrediction=[]
    for i in range(0, 15):
        stationPrediction.append(sta[0][i])
    print(stationPrediction)
    return render_template('station.html', enterStation=enterStation, exitStation=exitStation, count1=count1,
                           count2=count2, count3=count3, stationPrediction=stationPrediction)


@app.route('/station18')
def station2():
    enterStation = services666.getStationFlow2()[0][0][0]
    exitStation = services666.getStationFlow2()[1][0][0]

    count1 = services666.getStationCount2()[0][0][0]
    count2 = services666.getStationCount2()[1][0][0]
    count3 = services666.getStationCount2()[2][0][0]

    sta = services666.getStationPrediction2()
    stationPrediction = []
    for i in range(0, 15):
        stationPrediction.append(sta[0][i])
    print(stationPrediction)
    return render_template('station2.html', enterStation=enterStation, exitStation=exitStation, count1=count1,
                           count2=count2, count3=count3, stationPrediction=stationPrediction)

@app.route('/station1')
def station3():
    enterStation = services666.getStationFlow3()[0][0][0]
    exitStation = services666.getStationFlow2()[1][0][0]

    count1 = services666.getStationCount3()[0][0][0]
    count2 = services666.getStationCount3()[1][0][0]
    count3 = services666.getStationCount3()[2][0][0]

    sta = services666.getStationPrediction3()
    stationPrediction = []
    for i in range(0, 15):
        stationPrediction.append(sta[0][i])
    print(stationPrediction)
    return render_template('station3.html', enterStation=enterStation, exitStation=exitStation, count1=count1,
                           count2=count2, count3=count3, stationPrediction=stationPrediction)

if __name__ == '__main__':
    app.run()
