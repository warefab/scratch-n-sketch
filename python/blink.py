#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
#find and connect board
board.connect()
console('blinky demo')
board.backGroundColor(255, 255, 255)
board.textBackColor(255, 255, 255)
board.penColor(0, 0, 0)
board.rotateDisplay(board.rotate_0)
board.setFont(Font.calibri)
board.drawText("Scratch n Sketch", 20, 130)
for blink in range(51):
    board.ledWrite(Red, On)
    wait(500)
    board.ledWrite(Red, Off)
    wait(500)
    board.drawText(blink, 100, 170)
#disconnect
board.disconnect()
