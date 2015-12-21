#sending data to thingspeak

from libs.board import *
import requests

url = 'http://api.thingspeak.com/update?api_key=M8WO4key&field1='
count = 0

s = scratch_n_sketch()

def setup():
    #autoconnect
    s.connect()
    #set background color
    s.backGroundColor(0, 0, 0)
    #set text back color
    s.textBackColor(0, 0, 0)
    #set pen color
    s.penColor(255, 255, 0)
    #set font
    s.setFont(Font.terminal)
    #roate display
    s.rotateDisplay(board.rotate_0)

def post_data():
    #get sensor data
    s.getSensorData()
    #send light sensor data
    post = url + '{}'.format(s.LightSensor)
    req = requests.post(post)
    if req.status_code == 200:
        console('success')
        #blink green led
        s.ledWrite(Green, On)
        wait(500)
        s.ledWrite(Green, Off)
        count+=1
    else:
        console('fail')
        #blink red led
        s.ledWrite(Red, On)
        wait(500)
        s.ledWrite(Red, Off)

#post data to thingspeak, 15 seconds interval
if __name__ == "__main__":
    #initialize
    setup()
    #loop
    while True:
        #post data
        post_data()
        #wait for 15 seconds
        wait(15000)
