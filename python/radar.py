"""
*Scratch_n_sketch scripting
* Matrix demo
"""
from libs.board import *
#init
mbd = scratch_n_sketch()
#connect
mbd.connect()
#start
console('Radar scanning app')
#initialize
mbd.backGroundColor(255, 255, 255)
mbd.textBackColor(255, 255, 255)
mbd.setFont(mbd.ocr_extended)
#rotate by 90 deg
wait(5)
mbd.rotateDisplay(mbd.rotate_0)
#variables
rad = 5
#start loop
for x in range(100):
    mbd.getSensorData()

    if mbd.LightSensor > 512:
        mbd.penColor(20, 20, 20)
        txt = 'Scanning ....'
    else:
        mbd.penColor(255, 20, 20)
        txt = 'Object Detect'
    mbd.drawText(txt, 60, 10)
    for y in range(0, 6):
        mbd.drawCircle(120, 150, rad)
        rad += 16
        wait(100)
    mbd.penColor(255, 255, 255)
    mbd.fillRectangle(20, 40, 230, 300)
    wait(50)
    rad = 5
#disconnect port
mbd.disconnect()
