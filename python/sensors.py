#Scratch_n_sketch scripting

from libs.board import *

board = scratch_n_sketch()
#auto find and connect board
board.connect()
#console
console('Sensor info')
#set colors,  backgroung, textbackcolor and pen
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(0, 255, 255)
#font small
board.setFont(Font.peanut)
#rotate display 0 degrees
board.rotateDisplay(board.rotate_0)
#headers
board.drawText('Luminance', 20, 30)
board.drawText('Touch', 95, 100)
board.drawText('Remote', 85, 170)
board.drawText('Encoder', 150, 30)
board.drawText('Button 1', 20, 230)
board.drawText('Temparature', 120, 230)
#loop checking sensor data
while True:
    #get sensor data
    board.getSensorData()
    wait(20)
    #show light sensor
    board.drawText('{:04d}'.format(board.LightSensor), 35, 50)
    #show touch x and y pos
    board.drawText('x : {0:03d}  y : {1:03d}'.format(board.TouchX, board.TouchY), 55, 120)
    #show remote code
    if board.RemoteCode != '0':
        board.drawText(board.RemoteCode, 95, 190)
    #show angle sensor value
    board.drawText('{:04d}'.format(board.AngleSensor), 155, 50)
    #show switch one status
    if board.Switch:
        board.drawText('ON ', 45, 250)
    else:
        board.drawText('OFF', 45, 250)
    #temp sensor
    board.drawText('{:04d}'.format(board.TempSensor), 135, 250)
    #wait for 100ms
    wait(100)
#disconnect board
board.disconnect()
