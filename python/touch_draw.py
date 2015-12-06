"""
" Scratch_n_sketch scripting
" touch draw app
"""
from libs.board import *

#create board instance
board = scratch_n_sketch()
#auto find and connect
board.connect()
console('touch draw demo')
#colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(255, 255, 255)
#rotate 0
board.rotateDisplay(board.rotate_0)
#set pen thickness
pen_thickness = 2
pen = 1
while True:
    board.getSensorData()
    #clear screen
    if board.Switch: board.clearDisplay()
    #check remote code for colour change.
    rc = board.RemoteCode
    if rc != '0':
        pen_thickness = pen
        if rc == '4BB0':
            if pen <= 10: pen += 1
        #Green
        elif rc == '5BA0' :
                if pen > 0: pen -= 1
        #Red
        elif rc == 'EC10':
            board.penColor(255, 0, 0)
            board.rgbLed(255, 0, 0, 50)
        #Green
        elif rc == 'DC20' :
            board.penColor(0, 255, 0)
            board.rgbLed(0, 255, 0, 50)
        #Yellow
        elif rc == '1BE0':
            board.penColor(255, 255, 0)
            board.rgbLed(255, 255, 0, 50)
        #Blue
        elif rc == 'BC40':
            board.penColor(0, 0, 255)
            board.rgbLed(0, 0, 255, 50)
        #White
        elif rc == 'FC00':
            board.penColor(255, 255, 255)
            board.rgbLed(255, 255, 255, 50)
        #Rubber
        elif rc == '4CB0':
                board.penColor(0, 0, 0)
                board.rgbLed(0, 0, 0)
                pen_thickness = pen+10
        #White
    #check button touch coordinates
    if board.TouchX == 0 and board.TouchY == 0:
        xpos = ypos = 0
    else:
        #map touch xpos to lcd(0-239)
        xpos = int(map(board.TouchX, 117, 900, 0, 239))
        #map touch ypos to lcd(0-319)
        ypos = int(map(board.TouchY, 87, 890, 0, 319))
        board.fillCircle(xpos, ypos, pen_thickness)
    #wait a bit to process sensor info
    wait(40)
#button create end #######################################
board.disconnect()
