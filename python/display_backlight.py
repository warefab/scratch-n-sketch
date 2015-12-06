#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
#find and connect board
board.connect()
console('Baclight control')
#change colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(2, 255, 255)
#set font
board.setFont(Font.terminal)
#rotate display
board.rotateDisplay(board.rotate_0)
#draw text
board.drawText("BRIGHTNESS", 50, 130)
#set font
board.setFont(Font.elephant)
#show count
board.penColor(255, 255, 2)

for count in range(21):
    board.displayBrightness(count);
    board.drawText('{0:03d}'.format(count), 60, 170)
    wait(1000)
#disconnect
board.disconnect()
