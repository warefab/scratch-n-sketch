"""
*Scratch_n_sketch scripting
* Matrix demo
"""
from libs.board import *
#init
board = scratch_n_sketch()
#connect board
board.connect()
#start
console('Random Rectangles app')
#initialize colors
board.backGroundColor(255, 255, 255)
#rotate 90 degrees
board.rotateDisplay(board.rotate_90)
#delay for 5ms
wait(5)
#variables
y = 0
x = 0
#loop drawing random rectangles
for i in range(0, 50):
    for j in range(0, 20):
        #random pen color
        r = randomNumber(0, 255)
        g = randomNumber(0, 255)
        b = randomNumber(0, 255)
        board.penColor(r, g, b)
        #draw fill round rectangle of random sizer
        board.fillRoundRectangle(x, y,
                         (x+randomNumber(5, 41)),
                         (y+randomNumber(5, 41)))
        #set a random position
        x = randomNumber(20, 301)
        y = randomNumber(20, 221)
        #animate drawing with a 100 ms delay
        wait(50)
    #set background color to white
    board.ledWrite(Blue, Off)
    board.backGroundColor(255, 255, 255)
    board.ledWrite(Blue, On)
#disconnect from port
board.disconnect()
