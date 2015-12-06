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
text = 'WAREFAB'
ln = len(text)*16
#animate matrix for a certain duration
for i in range(0, 1000):
    #choose a random pen color
    board.penColor(randomNumber(0, 255),
                   randomNumber(0, 255),
                   randomNumber(0, 255))
    x = randomNumber(0, 239-ln)
    y = randomNumber(0, 319-16)
    board.drawText(text, x, y)
    wait(1000)
    er = '';
    for c in text: er += ' '
    board.drawText(er ,x , y)
    wait(1000)
#disconnect from port
board.disconnect()
