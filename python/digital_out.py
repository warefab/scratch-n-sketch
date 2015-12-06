#Scratch_n_sketch fan demo app
from libs.board import *

s = scratch_n_sketch()
#auto connect scratch_n_sketch
s.connect()
s.backGroundColor(0, 0, 0)
s.textBackColor(0, 0, 0)
s.penColor(255, 255, 0)
s.setFont(Font.terminal)
for i in range(1000):
    #get sensor data
    s.getSensorData()
    console(s.A1)
    wait(50)
    #check the distance sensor value
    if s.A1 >= 90:
        #set buzzer on
        s.digitalWrite(s.Do1, On)
        s.drawText("INTRUDER ...", 40, 140)
        wait(50)
        #set rgb led to red, with 10% brightness
        s.rgbLed(255, 0, 0, 10)
    else:
        #dset buzzer off
        s.digitalWrite(s.Do1, Off)
        s.drawText("SCANNING ...", 40, 140)
        #wait 50ms
        wait(50)
        #set rgb led to green, with 10% brightness
        s.rgbLed(0, 255, 0, 10)
    wait(100)
#disconnect scratch_n_sketch
s.disconnect()
