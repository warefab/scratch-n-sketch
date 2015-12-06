"""
*
* Scratch_n_sketch scripting
* Text screen saver
*
"""
from libs.board import *
#init
board = scratch_n_sketch()
#connect board
board.connect()
#initialize colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
#set font to ocr extended
board.setFont(Font.calibri)
#rotate display by 180
board.rotateDisplay(board.rotate_0)
text = 'PEANUT'
ln = len(text)*16
#animate matrix for a certain duration
for i in range(100):
    for i in range(20):
        #choose a random pen color
        board.penColor(randomNumber(0, 255),
                       randomNumber(0, 255),
                       randomNumber(0, 255))
        x = randomNumber(0, 239-ln)
        y = randomNumber(0, 319-16)
        board.drawText(text, x, y)
        wait(250)
    board.clearScreen()
    wait(500)
#disconnect from port
board.disconnect()
