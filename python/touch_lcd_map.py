#Scratch_n_sketch scripting
from libs.board import *

board = scratch_n_sketch()
#auto find and connect
board.connect()
#colors
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(0, 255, 255)
#rotate 0
board.rotateDisplay(board.rotate_0)
xpos = 0
ypos = 0
#font
board.setFont(Font.peanut)
board.drawText('Raw', 100, 80);
board.drawText('Mapped', 70, 180);
board.penColor(255, 0, 255)
board.setFont(Font.peanut)
"""
- touch_in_min_xp 145
- touch_in max_xp 905
- touch_in_min_yp 089
- touch_in max_yp 916
- lcd_in min_xp 0
- lcd_in max_xp 239
- lcd_in min_yp 0
- lcd_in max_yp 319
"""
while True:
    #get sensor data
    board.getSensorData()
    #map touch xpos to lcd(0-239)
    xpos = int(map(board.TouchX, 105, 904, 0, 239))
    #map touch xpos to lcd(0-319)
    ypos = int(map(board.TouchY, 80, 935, 0, 319))
    #draw coordinates
    board.drawText('x : {0:03d}  y : {1:03d}'.format(board.TouchX, board.TouchY), 50, 120)
    board.drawText('x : {0:03d}  y : {1:03d}'.format(xpos, ypos), 50, 220)
    wait(50)
#disconnect board
board.disconnect()
