"""
" Scratch_n_sketch
" motor speed control demo, connected to digital pin Do3
"""
from libs.board import *

s = scratch_n_sketch()
count = 0

def setup():
    #auto find and connect
    s.connect()
    console('Motor speed control')
    #colors
    s.backGroundColor(0, 0, 0)
    s.textBackColor(0, 0, 0)
    #oi
    s.setFont(Font.terminal )
    #rotate 0
    s.rotateDisplay(s.rotate_0)
    #buttons
    s.drawRoundRectangle(10, 250, 115, 300);
    s.drawRoundRectangle(120, 250, 230, 300);
    #headers
    s.penColor(255, 0, 0)
    s.drawText('UP',  50 , 270)
    s.penColor(0, 255, 0)
    s.drawText('DOWM', 150 , 270)
    s.penColor(255, 255, 0)
    s.textBackColor(0, 0, 0)
    xpos = 0
    ypos = 0
    s.drawText('MOTOR SPEED', 60, 90)
    s.penColor(0, 255, 255)
    s.drawText('%', 165, 130)
    #font
    s.setFont(Font.elephant)

def run():
    global count
    #get sensor data
    s.getSensorData()
    #get touch x and y pos
    xpos = s.TouchX
    ypos = s.TouchY
    wait(10)
    #draw coordinates
    s.drawText('{0:03d}'.format((int)(count/2.55)), 65, 120)
    #increase speed
    if (xpos>169 and xpos<488) and (ypos>746 and ypos<875):
        if count < 255 :
            count+=5
            s.digitalWrite(s.Do3, count);
    #decrease speed
    if (xpos>532 and xpos<875) and (ypos>746 and ypos<875):
        if count > 0 :
            count-=5
            s.digitalWrite(s.Do3, count);
    #delay for 50 ms
    wait(40)

if __name__ == "__main__":
    #initialize
    setup()
    #loop
    while True:
        #post data
        run()
