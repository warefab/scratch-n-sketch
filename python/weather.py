import pywapi
from libs.board import *
#instance
s = scratch_n_sketch()
wait(20000)
#auto-connect
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
s.drawRoundRectangle(5, 10, 235, 300)
s.drawLine(5, 50, 235, 50)
s.drawText('WEATHER INFO', 40, 25)
s.drawText("SEARCHING ...", 10, 150)
s.rgbLed(255, 0, 0, 50)
wait(50)
while(true):
    #get weather data from weather.com
    wt = pywapi.get_weather_from_weather_com('KEXX0009:1:KE')#, 'imperial')
    s.rgbLed(0, 255, 0, 50)
    wait(50)
    #save weather info
    tmp = wt['current_conditions']['temperature']
    flike = wt['current_conditions']['feels_like']
    dew = wt['current_conditions']['dewpoint']
    humidity = wt['current_conditions']['humidity']
    condition = wt['current_conditions']['text']
    visibility = wt['current_conditions']['visibility']
    wind_speed = '{}{}'.format((wt['current_conditions']['wind']['speed']),
                        (wt['current_conditions']['wind']['text']))
    s.penColor(0, 255, 255)
    #current condition
    s.drawText(condition, 10, 70)
    #feels like
    s.drawText('Feels Like  : ' + flike, 10, 100)
    s.penColor(255, 0, 255)
    #temperature
    s.drawText('Temperature : ' + tmp + ' F', 10, 150)
    #dew point
    s.drawText('Dew Point   : ' + dew, 10, 180)
    #humidity
    s.drawText('Humidity    : ' + humidity, 10, 210)
    #visibility
    s.drawText('Visibility  : ' + visibility, 10, 240)
    #wind speed
    s.drawText('Wind Speed  : ' + wind_speed, 10, 270)
    wait(10000)
#disconnect
s.disconnect()
