"""
* scratch_n_ sketch
*
* simple demo scripting in python language
*
"""

#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
print('Toggle icon demo')
mbd.showCalendar(22, 6, 5, 0);
wait(2000);
#myBoard.clearScreen()
mbd.backGroundColor(20, 20, 20)
mbd.textBackColor(20, 20, 20)
#delay
for x in range(1, 10):
    wait(250);
    mbd.drawToggleIcon(50, 50 , 1)
    wait(250);
    mbd.drawToggleIcon(50, 50 , 0)
    


#disconnect board """
mbd.disconnect()
