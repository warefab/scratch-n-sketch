#Scratch_n_sketch scripting

#use pyautogui
import pyautogui
pyautogui.FAILSAFE = false

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
board.setFont(board.font_big)
"""
- touch_in_min_xp 145
- touch_in max_xp 905
- touch_in_min_yp 089
- touch_in max_yp 916
"""
width = pyautogui.size()[0]
height = pyautogui.size()[1]
#loop
while True:
    #get sensor data
    board.getSensorData()
    #map touch xpos to lcd(0-239)
    xpos = int(map(board.touchX, 145, 905, 0, width))
    #map touch xpos to lcd(0-319)
    ypos = int(map(board.touchY, 85, 920, 0, height))
    #draw coordinates
    board.drawText('x : {0:04d}  y : {1:03d}'.format(xpos, ypos), 50, 120)
    #move mouse with specified tween
    pyautogui.moveTo(xpos, ypos, pyautogui.easeInOutExpo(0.2))
    wait(50)
#disconnect board
board.disconnect()