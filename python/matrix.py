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
console('Matrix demo')
#initialize colors
mbd.backGroundColor(0, 0, 0)
mbd.textBackColor(0, 0, 0)
#set font to ocr extended
mbd.setFont(Font.calibri)
#rotate display by 180
mbd.rotateDisplay(mbd.rotate_0)
wait(5)
#variables
yl = 10
xl = 15
r =  0
ch = 60
#animate matrix for a certain duration
for i in range(0, 1000):
    #choose a random pen color
    mbd.penColor(randomNumber(0, 255),
                 randomNumber(0, 255),
                 randomNumber(0, 255))
    #single line animation
    for rp in range(1, randomNumber(1, 21)):
        #get ascii letters only
        while(True):
            ch = randomNumber(48, 70);
            if not ((58<= ch <=65) or (
                    91<= ch <=96)) :
                break
        #draw number
        mbd.drawText(('%c'%ch), xl, yl)
        yl += 15
        r += 1
        #20ms delay
        wait(20)
        #clear screen if more than 400 letters drawn
        if r > 400:
            mbd.clearScreen()
            r = 0
            yl = 10
            #delay 5ms
            wait(5)
    #random number for a random position
    xl = (15 * randomNumber(1, 16))
    yl = 10
    #delay 5ms
    wait(5)
#disconnect from port
mbd.disconnect()
