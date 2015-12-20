#Scratch_n_sketch scripting
from libs.board import *
import requests

board = scratch_n_sketch()
board.connect()
#enter your url with public and private keys
url = 'http://data.sparkfun.com/input/YGVx1GOYN7uOo908OQ04?' + \
       'private_key=Rbvxkb0P7AtXP07KX57p&luminance='
#set background color
board.backGroundColor(0, 0, 0)
#set text back color
board.textBackColor(0, 0, 0)
#set pen color
board.penColor(255, 255, 0)
#set font
board.setFont(Font.terminal)
#roate display
board.rotateDisplay(board.rotate_0)
count = 0
while True:
    #get sensor data
    board.getSensorData()
    #check switch one status
    if board.Switch: btn = 'On'
    else: btn = 'Off'
    #add light sensor, button and remote data
    post = url + str(board.LightSensor) + \
           '&button=' + btn + \
           '&remote=' + str(board.RemoteCode)
    #send data to cloud
    phant = requests.post(post)
    #check response/status code
    if phant.status_code == 200:
        #success
        log = 'success'
        #blink green led
        board.ledWrite(Green, On)
        wait(500)
        board.ledWrite(Green, Off)
        count+=1
    else:
        #fail
        log = 'fail'
        #blink red led
        board.ledWrite(Red, On)
        wait(500)
        board.ledWrite(Red, Off)
    wait(500)
    #show status on the display
    board.setFont(Font.terminal)
    board.penColor(255, 255, 0)
    board.drawText('status : ' + log + '   ', 20, 80)
    board.penColor(0, 255, 255)
    board.drawText('logs', 70, 150);
    board.setFont(Font.elephant)
    board.drawText('{:03d}'.format(count), 50, 180)
    #show on the console
    console(log)
    wait(2000)
