"""
" Scratch_n_sketch scripting
" rgb-remote app
"""
from libs.board import *

#create board instance
board = scratch_n_sketch()
#auto find and connect
board.connect()
console('RGB led Remote color change demo')
while True:
    board.getSensorData()
    #check remote code for colour change.
    rc = board.RemoteCode
    if rc != '0':
        #Red
        if rc == 'EC10': board.rgbLed(255, 0, 0, 50)
        #Green
        elif rc == 'DC20' :board.rgbLed(0, 255, 0, 50)
        #Yellow
        elif rc == '1BE0': board.rgbLed(255, 255, 0, 50)
        #Blue
        elif rc == 'BC40': board.rgbLed(0, 0, 255, 50)
        #White
        elif rc == 'FC00': board.rgbLed(255, 255, 255, 50)
        #Rubber
        elif rc == '4CB0': board.rgbLed(0, 0, 0)
        #White
    #check button touch coordinates
    wait(100)
#button create end #######################################
board.disconnect()
