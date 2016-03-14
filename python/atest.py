
from libs.board import *

board = scratch_n_sketch()
board.connect()

for x in range(1020):
    board.ledWrite(All, On)
    wait(250)
    board.ledWrite(All, Off)
    wait(250)
board.disconnect()
