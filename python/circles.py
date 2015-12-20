"""
*Scratch_n_sketch scripting
* Matrix demo
"""
from libs.board import *
#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
print('Draw circles demo')
#initialize
mbd.backGroundColor(0, 0, 0)
#rotate by 90 deg
mbd.rotateDisplay(mbd.rotate_90)
wait(5)
#variables
xloc = 20
yloc = 10
#start loop
for x in range(0, 15):
    for y in range(0, 12):
        #select a random pen color
        mbd.penColor(randomNumber(0, 255),
                     randomNumber(0, 255),
                     randomNumber(0, 255))
        mbd.drawCircle(xloc, yloc, 5)
        yloc += 20
        #delay for 10ms
        wait(50)

    xloc += 20
    yloc = 10
#disconnect port
mbd.disconnect()
