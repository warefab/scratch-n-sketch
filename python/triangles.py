#Scratch_n_sketch scripting
from libs.board import *

board = scratch_n_sketch()
#auto find and connect
board.connect()
board.brushColor(255, 0, 0)
board.penColor(0, 255, 0)
wait(20)
board.clearDisplay()

for y in range(30):
    for x in range(11):
        if (x % 2):
          board.fillTriangle(20 + 20 * x, 10 + y * 10, 10 + x * 20,
                                    20 + y * 10, 30 + x * 20, 20 + y * 10)
        else:
          board.drawTriangle(20 + 20 * x, 10 + y * 10, 10 + x * 20,
                              20 + y * 10, 30 + x * 20, 20 + y * 10)
        wait(50)
#delay for 5 sec before clear screen
wait(5000)
