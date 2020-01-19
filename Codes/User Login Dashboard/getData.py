from om2mfunctions import *
from flask import Flask, jsonify,request,redirect,url_for,render_template,flash

import time
import numpy as np
import re
import random


import gspread
from oauth2client.service_account import ServiceAccountCredentials

from team_list_file import team_list

app = Flask(__name__)

# server = "http://139.59.42.21:8080"
server = "http://onem2m.iiit.ac.in:443"
cse = "/~/in-cse/in-name/"


i = 15
ae = "Team" + str(i) + "_" + team_list[i]['title']
print(ae)

contname = "pr_3_esp32_1"

# val is for the application entity to read data values from
val = server + cse + ae + "/" + contname 
val_temp = val + "/oe/oe_1_temperature" + "/la"
val_humid = val + "/oe/oe_1_rh" + "/la"
val_power = val + "/em/em_1_watts_total" + "/la"
val_voltage = val + "/em/em_1_vll_avg" + "/la"
val_current = val + "/em/em_1_current_total" + "/la"
# val_energy = val + "/em/em_1_var_total" + "/la"
val_flowrate = val +  "/fm/fm_1_pump_flowrate" + "/la"
val_totflow = val + "/fm/fm_1_pump_capacity" + "/la"

# /////////////////////////////////////
# GOOGLE SHEETS --- OBTAIN LIST OF USERS

# scope = ["https://spreadsheets.google.com/feeds"]
scope = ['https://www.googleapis.com/auth/analytics.readonly',
      'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
# print(creds)

# print(reco)


# print(val_temp)
# temp = get_data(val_temp)
# # temperature = 0 #temp[0]
# print("Temperature")
# # print(temperature)
# hum = get_data(val_humid)
# # humidity = 0 #hum[0]
# power = get_data(val_power)
# # power_watts = 0 #power[0]
# voltas = get_data(val_voltage)
# # voltage_volts = 0 #voltas[0]
# curr = get_data(val_current)
# # current_amps = 0 #curr[0]
# # tf = get_data(val_totalflow)
# # total_flow = tf[1]
# wfr = get_data(val_flowrate)

# energ = get_data(val_energy)
# # water_flow_rate = 0 #wfr[0]
# print(temp)
# print(hum)
# print(power)
# print(voltas)
# print(curr)
# print(wfr)
# print(energ)







#/////////////////////////////////////////////////////////////////////////
# FLASK RENDERING PAGES


# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    shert = client.open("sample").sheet1
# reco = shert.get_all_records()
    users = shert.col_values(1)
    rnos = shert.col_values(2)
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        rno = request.form['password']
        uidx = [i for i in range(len(users)) if users[i] == uname]
        ridx = [i for i in range(len(rnos)) if rnos[i] == rno]
        if len(ridx)==0 or len(uidx)==0:
            error = "No such details found"
        elif ridx[0] != uidx[0] :
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('result'))
    return render_template('login.html', error=error)

# ///////////////////////////////////////////////
@app.route('/result',methods= ['POST', 'GET'])
def result():

    # getting data from onem2m
    # x = get_data(val)
    # print(x)
    # y = re.split('[(),]',x[1])
    # print(y)
    # y = list(filter(None, y))
    # temperature = y[0]
    # humidity = y[1]
    # water_flow_rate = y[2]
    # total_flow = y[3]
    # voltage = y[4]
    # power = y[5]
    # current = y[6]
    # temperature = get_data(val_temp)
    # humidity = get_data(val_humid)
    # # water_flow_rate = get_data(val_flowrate)
    # # total_flow = get_data(val_totflow)
    # water_flow_rate = 0
    # total_flow = 0
    # voltage = get_data(val_voltage)
    # power = get_data(val_power)
    # current = get_data(val_current)
    # result = {}
    # result = {'temperature' : temperature , 'humidity' : humidity , 'water_flow_rate' : water_flow_rate , 'total_flow' : total_flow , 'voltage' : voltage , 'power' : power , 'current' : current}
    # return render_template("result.html",result = result)

    temp = get_data(val_temp)
    temperature = temp[1]
    print("Temperature")
    print(temperature)
    hum = get_data(val_humid)
    humidity = hum[1]
    power = get_data(val_power)
    power_watts = power[1]
    voltas = get_data(val_voltage)
    voltage_volts = voltas[1]
    curr = get_data(val_current)
    current_amps = curr[1]
    if(current_amps == "NULL-Value"):
        stat = "OFF"
    else:
        currnew = float(current_amps)
        if(currnew < 1):
            stat = "OFF"
        else:
            stat = "ON"
    # tf = get_data(val_totalflow)
    # total_flow = tf[1]
    wfr = get_data(val_flowrate)
    water_flow_rate = wfr[1]

    # ene = get_data(val_energy)
    # energy = ene[1]
    print(temp)
    print(hum)
    print(power)
    print(voltas)
    print(curr)
    print(wfr)

    # brazil.append(temperature)
    result = {}
    # result = {'temperature' : temperature , 'humidity' : humidity , 'water_flow_rate' : water_flow_rate , 'total_flow' : total_flow}
    result = {'temperature' : temperature , 'humidity' : humidity , 'power' : power_watts , 'voltage' : voltage_volts, 'current' : current_amps ,'flowrate' : water_flow_rate}
    return render_template("result.html",result = result, stat = stat)


# ///////////////////////////////////////////////////////
@app.route('/result/control',methods = ['POST', 'GET'])
def ctrl():

    wor= request.form['word']
    k = 1
    if(wor=="on"):
        print("ON")
        k = 1
    else:
        print("OFF")
        k = 0
    
    # This is to post data from the app to the onem2m server to turn the machine On/Off using relay
    create_data_cin(server + cse + ae + "/" + "pr_3_esp32_1/ss/ss_1_control_signal",str(k))

    return "OK"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

# ///////////////////////////////////////////////////////////////////////////                                                   
