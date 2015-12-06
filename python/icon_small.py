from libs.board import *

#init
board = scratch_n_sketch()
#connect board
board.connect()
board.clearScreen()
board.setFont(Font.icon_small)
board.rotateDisplay(board.rotate_0)
j = 47
k=20
l = 100
while true:

    for y in range(10):
        for x in range(10):
            board.penColor(
            randomNumber(50, 255),
            randomNumber(50, 255),
            randomNumber(50, 255))

            if j >= 90 : break
            else: j+=1

            board.drawText(chr(j), k, l)
            wait(10)
            k+=20
        l+=15
        k = 20
        if j >= 90 : break

board.disconnect()
