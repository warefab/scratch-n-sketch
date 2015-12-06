#Scratch_n_sketch scripting

from libs.board import *

b = scratch_n_sketch()
b.connect()
console('logging sensor data')
for i in range(10):
    b.getSensorData()
    console('Temp: {}'.format(b.TempSensor))
    wait(1000)
b.disconnect()
