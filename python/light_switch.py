#Scratch_n_sketch scripting
from libs.board import *

board = scratch_n_sketch()
#auto find and connect board
board.connect()
#set colours
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(255, 255, 0)
#rotate display 0 deg
board.rotateDisplay(board.rotate_0)
board.setFont(Font.terminal)
#loop checking sensor data
while True:
    #get sensor data
    board.getSensorData()
    luminance = board.LightSensor
    #set led on/off according to luminance value
    if luminance < 512:
        #write blue led on
        board.ledWrite(Green, On)
    else:
        #write blue led off
        board.ledWrite(Green, Off)
    #show luminance in display
    board.drawText('Luminance : {:04d}'.format(luminance), 30, 150)
    #wait for 100ms
    wait(200)
#disconnect board
board.disconnect()
