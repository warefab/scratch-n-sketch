#Scratch_n_sketch scripting
from libs.board import *

board = scratch_n_sketch()
#auto find and connect
board.connect()
console('fan demo (motor control)')
#colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(250, 250, 250)
#oi
board.setFont(Font.terminal)
#rotate 0
board.rotateDisplay(board.rotate_0)
#buttons
board.drawRoundRectangle(10, 250, 115, 300);
board.drawRoundRectangle(120, 250, 230, 300);
#headers
board.penColor(255, 0, 0)
board.drawText('UP',  50 , 270)
board.penColor(0, 255, 0)
board.drawText('DOWM', 150 , 270)
board.penColor(255, 255, 0)
board.textBackColor(0, 0, 0)
xpos = 0
ypos = 0
board.drawText('FAN SPEED', 60, 90)
board.penColor(0, 255, 255)
board.drawText('%', 165, 130)
#font
board.setFont(Font.elephant)
#loop
count = 0
while True:
    #get sensor data
    board.getSensorData()
    #get touch x and y pos
    xpos = board.TouchX
    ypos = board.TouchY
    #draw coordinates
    pc = (int)(map(count, 0, 255, 0, 100))
    board.drawText('{0:03d}'.format(pc), 65, 120)
    #increase brightness button
    if (((xpos>169 and xpos<488) and (ypos>746 and ypos<875)) or
        board.RemoteCode == '4BB0'):
        if count < 255 :
            count+=17
            board.digitalWrite(board.Do3, count);
    #decrease brightness button
    if (((xpos>532 and xpos<875) and (ypos>746 and ypos<875)) or
        board.RemoteCode == '5BA0'):
        if count > 0 :
            count-=17
            board.digitalWrite(board.Do3, count);
    #delay for 50 ms
    wait(50)
    if(pc < 50):
        board.ledWrite(Red, Off)
        board.ledWrite(Green, On)
    else:
        board.ledWrite(Red, On)
        board.ledWrite(Green, Off)
    wait(50)
#disconnect board
board.disconnect()
