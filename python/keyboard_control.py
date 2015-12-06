#Scratch_n_sketch scripting
import pyautogui
pyautogui.FAILSAFE = false

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
xpos = 0
ypos = 0
xp = 0;
yp = 0;
board.setFont(board.font_small)
board.rotateDisplay(board.rotate_0)
board.drawLine(10, 180, 235, 180)
board.drawLine(115, 10, 115, 180)
board.drawText('volume up', 20, 80)
board.drawText('volume down', 130, 80)
board.drawText('press anywhere', 40, 240)
while True:
    board.getSensorData()
    xpos = board.touchX
    ypos = board.touchY
    
    if not xp==xpos and not yp == ypos:
        #remove unnecessary clicks
        if (abs(xp-xpos) > 5) and  (abs(yp-ypos) > 5):
            #volume up
            if (xpos>210 and xpos<513) and (ypos>108 and ypos<550):
                pyautogui.press('volumeup')
                board.ledWrite(Red, On)
            #volume down
            elif (xpos>513 and xpos<950) and (ypos>108 and ypos<550):
                pyautogui.press('volumedown')
                board.ledWrite(Green, On)
            #backspace
            else:
                pyautogui.press('space')
                board.ledWrite(Blue, On)
            #save coords
            xp = board.touchX
            yp = board.touchX
    wait(50)
    board.ledWrite(All, Off)
    wait(50)
    #disconnect board
board.disconnect()