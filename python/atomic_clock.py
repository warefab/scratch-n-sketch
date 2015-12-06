"""
* Scratch_n_sketch scripting
* Sketch demo
"""
from libs.board import *

def printNum(num, pos_x, pos_y, sep= ' '):
    index = 0
    board.setFont(Font.atomic)
    for ch in num:
        board.drawText(ch, pos_x + index, pos_y)
        index += 30
    if sep != ' ':
        board.setFont(Font.terminal)
        board.drawText(sep, pos_x + index-3, pos_y+2)
        board.drawText(sep, pos_x + index-3, pos_y+16)
#init
board = scratch_n_sketch()
#fina and autoconnect
board.connect()
#start
console('Date and Time Demo')
#initialize
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.setFont(Font.calibri)
board.rotateDisplay(board.rotate_0)
#rotate by 90 deg
wait(5)
#draw date
board.penColor(255, 0, 255)
cr = time.strftime('%b-%d-%Y', time.localtime())
board.drawText(cr.upper(), 40, 100)
#time color
board.penColor(0, 0, 255)
#show time forever
while(1):
    #draw time
    hr = time.strftime('%H', time.localtime())
    mn = time.strftime('%M', time.localtime())
    sc = time.strftime('%S', time.localtime())
    printNum(hr, 20, 140, ':')
    printNum(mn, 90, 140, ':')
    printNum(sc, 160, 140)
    #delay for 1000ms/1 second
    wait(1000)
#disconnect port
board.disconnect()
