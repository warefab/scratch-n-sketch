"""
 mario.py
 play the famous pacman game using home media remote control
 link : http://www.originalpacman.com/pacman-original-full-screen.html
"""
from libs.board import *
#use pyautogui
import pyautogui as hmi

hmi.FAILSAFE = false

s = scratch_n_sketch()
rc_prev = 0

def setup():
    s.connect()
    s.backGroundColor(0, 0, 0)
    s.textBackColor(0, 0, 0)
    s.setFont(Font.terminal)
    s.rotateDisplay(s.rotate_0)
    s.penColor(255, 255, 0)
    s.drawText('PACMAN GAME', 60, 120)
    s.drawText('START GAME!!!' , 50, 160)
    wait(50)

def play():
    #get sensor data
    s.getSensorData()
    #sense keypress
    global rc_prev
    rc = s.RemoteCode
    #remove double clicks
    if not (rc == rc_prev):
        if rc  == '6C90':
            hmi.keyDown('up')
            hmi.keyUp('up')
        elif rc == 'CC30':
            hmi.keyDown('down')
            hmi.keyUp('down')
        elif rc == 'AC50':
            hmi.keyDown('right')
            hmi.keyUp('right')
        elif rc == '8C70':
            hmi.keyDown('left')
            hmi.keyUp('left')
        elif rc == '9C60':
            hmi.keyDown('p')
            hmi.keyUp('p')
        rc_prev = rc
    s.ledWrite(Red, On)
    wait(20)
    s.ledWrite(Red, Off)
    wait(20)

if __name__ == "__main__":
    setup()
    while True:
        play()
