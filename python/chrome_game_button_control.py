#Scratch_n_sketch scripting
#play the famous google chrome
#dinasaur game
from libs.board import *
#use pyautogui
import pyautogui as hmi

hmi.FAILSAFE = false

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.setFont(board.font_small)
board.rotateDisplay(board.rotate_0)
board.penColor(255, 255, 0)
board.drawText('CURSOR CONTROL', 50, 80)
board.drawText('CHROME GAME', 60, 120)
board.setFont(board.digital)
board.penColor(255, 0, 0)
for i in range(1, 4):
    board.drawText(i, 100, 160)
    wait(1000)
board.setFont(board.comic_sans)
board.drawText('START GAME!!' , 40, 160)
#loop
while True:
    #get sensor data
    board.getSensorData()
    #sense keypress
    if board.SwitchTwo:
        hmi.press('up')
    wait(20)
    #disconnect board
board.disconnect()
