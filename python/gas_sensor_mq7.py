# scratch_n_sketch
# graph MQ7 gas sensor on the screen display + send data to thingspeak
# sensor connected to A1 pin
from libs.board import *
import requests
#instance
s = scratch_n_sketch()
url = 'http://api.thingspeak.com/update?api_key=key&field1='
xpos = ypos = ypo = xpo =  drawHeight = 0
sensor_val = 0
count = 0

def setup():
    s.connect()
    #set background color
    s.backGroundColor(0, 0, 0)
    s.rotateDisplay(s.rotate_90)
    s.penColor(0, 180, 250)

    s.setFont(Font.terminal)
    s.drawText("GAS SENSOR", 90, 20)

    s.penColor(250, 10, 10)

def drawOnScreen():
    global sensor_val
    global xpos, ypos, ypo, xpo, drawHeight
    #read the sensor and map it to the screen height
    s.getSensorData();
    wait(10);
    sensor_val = s.A1
    drawHeight = map(sensor_val, 0, 1023, 10, 240-60)
    #draw a line in a nice color
    #s.drawLine(xpos, 240 - 10, xpos, 240 - drawHeight)
    #s.fillCircle(xpos, 240 - drawHeight, 1)
    s.drawLine(xpo, ypo, xpos, 240 - drawHeight)
    xpo = xpos
    ypo = 240 - drawHeight
    s.penColor(250, 180, 10)
    s.drawText('{:04d}'.format(sensor_val), 140, 40)
    s.penColor(250, 10, 10);
    #if the graph has reached the screen edge
    #erase the screen and start again
    if (xpos >= 320):
        xpos = xpo = 0
        s.backGroundColor(0, 0, 0)
        s.drawText("GAS SENSOR", 90, 20)
    else:
        #increment the horizontal position:
        xpos+=1
    wait(100)

def post_data():
    #send gas sensor data
    post = url + '{}'.format(sensor_val)
    req = requests.post(post)
    if req.status_code == 200:
        console('success')
    else:
        console('fail')

#post data to thingspeak, 15 seconds interval
#and still graph on the display, realtime
if __name__ == "__main__":
    #initialize
    setup()
    #loop
    while True:
        #graph 100ms interval
        drawOnScreen()
        #post data after 15 seconds
        if count == 150:
            post_data()
            count = 0
        else:
            count+=1
