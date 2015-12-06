#Scratch_n_sketch scripting
from libs.board import *
#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
console('text loop demo')
#start
mbd.backGroundColor(0, 0, 0)
mbd.textBackColor(0, 0, 0)
mbd.penColor(0, 255, 255)
mbd.setFont(mbd.font_big)
mbd.rotateDisplay(mbd.rotate_0)
#draw some text
mbd.drawText('Scratch n sketch', 10, 10)
mbd.penColor(255, 255, 0)
wait(5)
#loop 0-100
for x in range(101):
    #draw loop numbers
    mbd.drawText(join('Please wait:',
                join(x, '%')), 10, 140)
    #delay a bit
    wait(50)
#script done
for i in range(0, 3):
    mbd.drawText('Done', 10, 160)
#disconnect port
mbd.disconnect()
