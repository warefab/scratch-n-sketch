#Scratch_n_sketch scripting
from libs.board import *

board = scratch_n_sketch()
#auto find and connect
board.connect()
console('touch switch demo')
#colors
board.backGroundColor(0, 0, 0)
board.penColor(250, 250, 250)
#oi
board.setFont(Font.terminal )
#rotate 0
board.rotateDisplay(board.rotate_0)
#buttons
board.drawRoundRectangle(10, 250, 115, 300);
board.drawRoundRectangle(120, 250, 230, 300);
#headers
board.textBackColor(0, 0, 0)
board.penColor(255, 0, 255)
board.drawText('PRESS BUTTONS', 30, 80)
#board.textBackColor(250, 250, 250)
board.penColor(255, 0, 0)
board.drawText('ON',  50 , 270)
board.penColor(0, 255, 0)
board.drawText('OFF', 150 , 270)
board.penColor(255, 255, 0)
board.textBackColor(0, 0, 0)
xpos = 0
ypos = 0
#font
#board.setFont(Font.peanut)
#loop
while True:
    #get sensor data
    board.getSensorData()
    #get touch x and y pos
    xpos = board.TouchX
    ypos = board.TouchY
    #draw coordinates
    #board.drawText('x : {0:03d}  y : {1:03d}'.format(xpos, ypos), 50, 120)
    #on touch button
    if (xpos>169 and xpos<488) and (ypos>746 and ypos<875):
        board.ledWrite(Blue, On)
        board.drawText('STATUS : ON ', 40, 120)
    #off touch button
    if (xpos>532 and xpos<875) and (ypos>746 and ypos<875):
        board.ledWrite(Blue, Off)
        board.drawText('STATUS : OFF', 40, 120)
    #delay for 50 ms
    wait(50)
#disconnect board
board.disconnect()
