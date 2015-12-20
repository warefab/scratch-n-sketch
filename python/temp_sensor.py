#Scratch_n_sketch scripting

from libs.board import *
#init
board = scratch_n_sketch()
#auto find and connect
board.connect()
#console
console('Reading temparature')
#change display background color
board.backGroundColor(0, 0, 0)
#change display background color
board.textBackColor(0, 0, 0)
#change font to terminal
board.setFont(Font.terminal)
#rotate display
board.rotateDisplay(board.rotate_0)
#change pen color
board.penColor(255, 255, 0)
#draw text - temparature
board.drawText('TEMPERATURE', 40, 50)
#change pen color
board.penColor(0, 255, 255)
#variables
voltage = 0
celcius = 0
farenheit = 0
while True:
    #get sensor data
    board.getSensorData()
    #convert ADC output to millivolts
    voltage = ((board.TempSensor *3300) / 4096)
    #show sensor voltage in mV
    #board.drawText('{0}{1:04.2f}'.format('V  : ', voltage), 35, 100)
    #get temp in celcius
    board.setFont(Font.comic)
    board.drawText('oC', 160, 150)
    celcius = (abs(voltage-500))/10
    #board.drawText('{0}{1:04.2f}'.format('oC : ', celcius), 35, 140)
    board.setFont(Font.elephant)
    board.drawText('{:03d}'.format((int)(celcius)), 55, 160)
    #farenheit
    farenheit = (celcius * 9.0 / 5.0) + 32
    #board.drawText('{0}{1:04.2f}'.format('F  : ', farenheit), 35, 180)
    #wait for 250 ms
    wait(250)
#disconnect board
board.disconnect()
