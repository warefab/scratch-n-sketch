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
    if s.A1 >= 350:
        #set buzzer on
        s.digitalWrite(s.Do1, On)
        s.drawText("INTRUDER ...", 40, 140)
        s.ledWrite(Red, On)
    else:
        #dset buzzer off
        s.digitalWrite(s.Do1, Off)
        s.drawText("SCANNING ...", 40, 140)
        s.ledWrite(Red, Off)
    wait(100)
#disconnect scratch_n_sketch
s.disconnect()
