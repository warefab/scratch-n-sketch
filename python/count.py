#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
#find and connect board
board.connect()
console('count demo')
#change colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(2, 255, 255)
#set font
board.setFont(Font.peanut)
#rotate display
board.rotateDisplay(board.rotate_0)
#draw text
board.drawText("Scratch n Sketch", 40, 130)
#set font
board.setFont(Font.elephant)
x= 40
#show count
for count in range(1001):
    index = 0
    for c in str('%04d'%count):
        board.drawText(c, x + index, 170)
        index += 40
        wait(10)
#disconnect
board.disconnect()
