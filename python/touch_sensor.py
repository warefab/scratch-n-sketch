from libs.board import *

s = scratch_n_sketch()

def setup():
    #autoconnect
    s.connect()
    #set background color
    s.backGroundColor(0, 0, 0)
    #set text back color
    s.textBackColor(0, 0, 0)
    #set pen color
    s.penColor(255, 255, 0)
    #set font
    s.setFont(Font.terminal)
    #roate display
    s.rotateDisplay(s.rotate_0)

def sense_touch():
    #get sensor data
    s.getSensorData()
    #get touch data
    touch = s.Di3
    wait(50)
    if(touch == 0): #touched
        s.penColor(255, 255, 255)
        s.fillRoundRectangle(70, 100, 160, 140)
        s.penColor(255, 255, 0)
        s.fillRoundRectangle(70, 100, 115, 140)
        s.drawText('TOUCH DETECTED', 30, 160)
        s.ledWrite(Blue, On)
    else: #not touched
        s.penColor(255, 255, 255)
        s.fillRoundRectangle(70, 100, 160, 140)
        s.penColor(0, 255, 255)
        s.fillRoundRectangle(115, 100, 160, 140)
        s.drawText('   NO TOUCH   ', 30, 160)
        s.ledWrite(Blue, Off)
    #wait for 250ms
    wait(200)

if __name__ == "__main__":
    #initialize
    setup()
    #loop
    while True:
        #post data
        sense_touch()
