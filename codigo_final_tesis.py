#!/usr/bin/python3
# -*- coding: utf-8 -*-

import spidev
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

m6675 = spidev.SpiDev(0,0)
m6675.max_speed_hz=100000

def c_to_f(temp):
    f = ((temp/5)*9)+32
    return f

def readTempC():
    m6675.writebytes([0x00,0x00])
    tempRead = m6675.readbytes(2)
    temp = (tempRead[0] <<8 | tempRead[1]) >> 3
    return temp * 0.25
a=0
temperatura=np.array([0])
tiempo=0.5*60
while tiempo>0:
    temp = readTempC()
    print('Thermocouple Temperature: {0:0.3F}°C / {1:0.3F}°F'.format(temp, c_to_f(temp)))
    if temp ==0:
        print(a)
        a+=1

    #humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    #if humidity is not None and temperature is not None:
        #print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    #else:
        #print("Failed to retrieve data from humidity sensor")

    temperatura=np.concatenate((temperatura,np.array([temp])),axis=0)
    #tiempo=tiempo-0.2
    #plt.plot(temperatura[1:])
    #plt.pause(0.05)
    sleep(0.2)
    np.save('prueba_5_julio_para_casa',temperatura)
plt.show()