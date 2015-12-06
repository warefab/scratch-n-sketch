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
board.penColor(0, 255, 255)
board.textBackColor(0, 0, 0)
#rotate display by 180
board.rotateDisplay(board.rotate_0)
board.setFont(Font.terminal)

xp =  yp = 100
deg = 0
e = 310
pi = 22/7
r = 30

while 1:
    rad = r
    for i in range(2):
        x = (rad * math.cos(abs(360-deg) * pi / 180)) + xp;
        y = (rad * math.sin(abs(360-deg) * pi / 180)) + yp;
        board.drawPixel(x, y);
        rad += 1
    wait(30)
    board.drawText(deg , 82, 92)
    if deg < e : deg += 1
    else : break
board.disconnect()
