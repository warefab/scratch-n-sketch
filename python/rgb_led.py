"""
*Scratch_n_sketch scripting
* Background demo
"""
from libs.board import *
#init
board = scratch_n_sketch()
#connect board
board.connect()
#start
#initialize
for i in  range(101):
    #off
    board.rgbLed(0, 0, 0, 125)
    wait(1000)
    #red, with 25% brightness
    board.rgbLed(255, 0, 0, 125)
    wait(1000)
    #green, with 25% brightness
    board.rgbLed(0, 255, 0, 125)
    wait(1000)
    #blue, with 25% brightness
    board.rgbLed(0, 0, 255, 125)
    wait(1000)
    #white, rwith 25% brightness
    board.rgbLed(255, 255, 255, 125)
    wait(1000)
board.disconnect()
