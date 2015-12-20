"""
*Scratch_n_sketch scripting
* Background demo
"""
#lib
from libs.board import *
#color wheel method
def colorWheel(WheelPos):
    if(WheelPos < 85):
        return board.rgbLed(WheelPos * 3, 255 - WheelPos * 3, 0, 30)
    elif(WheelPos < 170):
        WheelPos -= 85
        return board.rgbLed(255 - WheelPos * 3, 0, WheelPos * 3, 30)
    else:
        WheelPos -= 170;
        return board.rgbLed(0, WheelPos * 3, 255 - WheelPos * 3, 30)

#init
board = scratch_n_sketch()
#connect board
board.connect()
#console
console('rgb color wheel app')
#start
for x in range(11):
    for i in  range(256):
        #set wheel color
        colorWheel(i)
        #wait for 50ms
        wait(50)
#disconnect board
board.disconnect()
