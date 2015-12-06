#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
board.connect()
wait(1)
board.powerControl(mbd.power_on);
wait(3000)
board.backGroundColor(255, 255, 255)
board.textBackColor(255, 255, 255)
board.penColor(255, 0, 0)
board.setFont(mbd.font_small)
board.rotateDisplay(mbd.rotate_0)
wait(5)
board.drawText('Shutting down in 10 seconds', 20, 50)

for i in range(10):
    board.drawText(i, 110, 80)
    wait(1000)
board.ledWrite(All, Off)
board.powerControl(mbd.power_off);
board.rgbLed(0,0,0)
mbd.disconnect()
