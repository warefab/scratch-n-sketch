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
board.penColor(255, 0, 255)
board.textBackColor(0, 0, 0)
#rotate display by 180
board.rotateDisplay(board.rotate_0)
board.setFont(Font.terminal)

#xp =  yp = 100
deg = 0
e = 310
pi = 22/7
r = 25
lf = 0

for i in range(3):
    deg = 0
    if i == 0:
        board.penColor(255, 0, 255)
        xp =  110
        yp = 50
        e = 150
    elif i == 1:
        board.penColor(255, 255, 0)
        xp = 110
        yp = 120
        e = 230
        r = 35
    elif i == 2:
        board.penColor(0, 255, 255)
        xp = 110
        yp = 240
        e = 345
        r = 60
        board.setFont(Font.elephant)
        lf = 1;
    while 1:
        if not deg < 10 : st = deg - 5
        else: st = deg
        board.drawArc(xp, yp, st, deg, r, 2)
        if not lf :
            wait(10)
            board.drawText(join(int(map(deg, 0, 360, 0, 100)), '%') , xp - 18, yp-8)
        else:
            wait(25)
            board.setFont(Font.elephant)
            board.drawText(int(map(deg, 0, 360, 0, 100))  , xp - 44, yp-24)
            board.setFont(Font.terminal)
            board.drawText('%', xp+30, yp-10)
            wait(25)
        if deg < e : deg += 1
        else : break
    wait(1000)
board.disconnect()
