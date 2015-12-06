#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
board.connect()

while True:
    board.ledWrite(Green, On)
    board.ledWrite(Blue, Off)
    board.ledWrite(Red, Off)
    wait(1000)

    board.ledWrite(Green, Off)
    board.ledWrite(Blue, On)
    board.ledWrite(Red, On)
    wait(100)

board.disconnect()
