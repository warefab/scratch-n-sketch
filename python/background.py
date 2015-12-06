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
for i in  range(10):

    board.backGroundColor(18, 203, 252)
    wait(500)
    board.backGroundColor(206, 228, 30)
    wait(500)
    board.backGroundColor(219, 37, 25)
    wait(500)
    """
    board.penColor(18, 203, 252)
    board.fillRectangle(0, 0,240, 160)
    board.fillRectangle(0, 0,160, 320)
    wait(500)
    board.penColor(206, 228, 30)
    board.fillRectangle(0, 0,240, 160)
    board.fillRectangle(0, 0,160, 320)
    wait(500)
    board.fillRectangle(0, 0,240, 160)
    board.fillRectangle(0, 0,240, 320)
    wait(500)
    """
board.disconnect()
