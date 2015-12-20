"""
*
* Scratch_n_sketch
* wild numbers app
*
"""
from libs.board import *

board = scratch_n_sketch()
#find and connect board
board.connect()
#start
console('wild numbers app')
#initialize colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
#set font to ocr extended
board.setFont(Font.peanut)
#rotate display by 180
board.rotateDisplay(board.rotate_0)
wait(5)
#variables
yl = 10
xl = 15
r =  0
ch = 60
#animate matrix for a certain duration
while(1):
    #choose a random pen color
    board.penColor(randomNumber(0, 255),
                 randomNumber(0, 255),
                 randomNumber(0, 255))
    #single line animation
        #get ascii letters only
    while(True):
        ch = randomNumber(48, 70);
        if not ((58<= ch <=65) or (
                91<= ch <=96)) :
            break
    #draw number
    board.drawText(('%c'%ch), xl, yl)
    yl = (15 * randomNumber(1, 20))
    r += 1
    #20ms delay
    wait(20)
    #clear screen if more than 400 letters drawn
    if r > 400:
        board.clearDisplay()
        r = 0
        yl = 10
        #delay 5ms
        wait(10)
    #random number for a random position
    xl = (15 * randomNumber(1, 16))
    #delay 5ms
    wait(10)
#disconnect from port
board.disconnect()
