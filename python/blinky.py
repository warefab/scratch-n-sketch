#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
#find and connect board
board.connect()
#rotate display 0 degrees
board.rotateDisplay(board.rotate_90)
#white background color
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
#set font
board.setFont(board.font_big)
#draw text
board.penColor(255, 255, 0)
board.drawText('My first Blinky project!', 15, 120)
#blink forever
board.penColor(0, 255, 255)
for blink in range(51):
    board.ledWrite(Red, On)
    board.ledWrite(Blue, Off)
    wait(100)
    board.ledWrite(Red, Off)
    board.ledWrite(Blue, On)
    wait(100)
    board.drawText(join('Blinks : ', blink), 70, 150)
#disconnect
board.disconnect()
