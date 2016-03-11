import pywapi
from libs.board import *
#instance
s = scratch_n_sketch()
#auto-connect
s.connect()
#set background color
s.backGroundColor(0, 0, 0)
s.rotateDisplay(s.rotate_90)
s.penColor(250, 180, 10)

s.setFont(Font.terminal)
s.drawText("LIGHT SENSOR", 90, 20)
xpos = ypos = ypo = xpo =  drawHeight = 0
while True:
    #read the sensor and map it to the screen height
    s.getSensorData();
    wait(10);
    drawHeight = map(s.LightSensor, 0, 1023, 10, 240-60)
    #draw a line in a nice color
    #s.drawLine(xpos, 240 - 10, xpos, 240 - drawHeight)
    #s.fillCircle(xpos, 240 - drawHeight, 1)
    s.drawLine(xpo, ypo, xpos, 240 - drawHeight)
    xpo = xpos
    ypo = 240 - drawHeight
    s.penColor(10, 180, 250)
    s.drawText('{:04d}'.format(s.LightSensor), 140, 40)
    s.penColor(250, 180, 10);
    #if the graph has reached the screen edge
    #erase the screen and start again
    if (xpos >= 320):
        xpos = xpo = 0
        s.backGroundColor(0, 0, 0)
        s.drawText("LIGHT SENSOR", 90, 20)
    else:
        #increment the horizontal position:
        xpos+=1
    wait(50)
s.disconnect()
