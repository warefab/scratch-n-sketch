#Scratch_n_sketch scripting
from libs.board import *

s = scratch_n_sketch()

def setup():
  #auto find and connect
  s.connect()
  console('light and touch controlled switch')
  #colors
  s.backGroundColor(0, 0, 0)
  s.penColor(250, 250, 250)
  #oi
  s.setFont(Font.terminal )
  #rotate 0
  s.rotateDisplay(s.rotate_0)
  #headers
  s.textBackColor(0, 0, 0)
  s.penColor(255, 0, 255)
  s.drawText('LIGHT STATUS', 40, 120)
  s.penColor(255, 255, 0)
  s.textBackColor(0, 0, 0)
  #font
  #s.setFont(Font.peanut)
#loop
def turnOnOff():
    #get sensor data
    s.getSensorData()
    #on touch button
    if (s.LightSensor <= 500):
        s.digitalWrite(s.Do1, On)
        s.drawText('STATUS : ON ', 40, 160)
    #off touch button
    if(s.LightSensor > 500):
        s.digitalWrite(s.Do1, Off)
        s.drawText('STATUS : OFF', 40, 160)
    #delay for 50 ms
    wait(100)

#run
if __name__ == "__main__":
    #initialize
    setupvis
    while True:
        #turn lights on/off
        turnOnOff()
