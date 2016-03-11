"""
* scratch_n_ sketch
*
* simple demo scripting in python language
*
"""
from libs.board import *

#init
board = scratch_n_sketch()
#connect board
board.connect()
#start
console('Bubbles app')
#set background color
board.backGroundColor(255, 255, 255)
#rotate the displays
board.rotateDisplay(board.rotate_270)
#delay
wait(1)
#show 50 times
for i in range(0, 50):
    #set the number of circles randomly
    num = randomNumber(5, 30)
    #draw circles
    for x in range(0, num):
        #set random pen color
        board.penColor(randomNumber(0, 255),
                        randomNumber(0, 255),
                        randomNumber(0, 255))
        #draw a circle at random pos and radius
        board.drawCircle(randomNumber(20, 300),
                           randomNumber(20, 200),
                           randomNumber(5, 20))
        #animate with a delay
        board.ledWrite(Blue, On)
        wait(25)
        board.ledWrite(Blue, Off)
        wait(25)
    #clear everything
    board.backGroundColor(255, 255, 255)
    wait(1)
#disconnect board """
board.disconnect()
