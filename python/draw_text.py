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
print('Draw Text demo')
#clear screen
#myBoard.clearScreen()
board.backGroundColor(20, 20, 20)
board.textBackColor(20, 20, 20)
board.setFont(Font.terminal);
board.rotateDisplay(board.rotate_270)
#delay a bit
wait(1)
#draw rectangle
board.penColor(0, 255, 255);
board.drawRectangle(40, 70, 275, 160)
wait(1);
#write text 1
board.penColor(150, 150, 150)
board.drawText('* Scratch-N-Sketch', 50, 80)
#delay
wait(1)
#print text 2
board.penColor(255, 55, 240)
board.drawText('* Please wait ....', 50, 110)
#delay
wait(1)
#print number 0 to 100
for x in range(0,101):
    #print new number
    board.drawText(join(x, ' %') , 210, 115)
    #generate a random colour
    """myBoard.penColor(randomNumber(0, 255),
                     randomNumber(0, 255),
                     randomNumber(0, 255))"""
    #a 200 ms short delay
    wait(10)
#print text 3
wait(1)
board.penColor(255, 255, 0)
for i in range(1,3):
    board.drawText('* Done . Bye!', 50, 140)
#disconnect board """
board.disconnect()
