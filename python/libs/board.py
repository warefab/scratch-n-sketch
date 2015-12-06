"""
*
* scratch_n_sketch V 1.0
*
* (c) 2015 wwww.warefab.com
* Author  : muchiri john [john@warefab.com]
* Date    : 27-06-2015 05:30:42
* License : MIT
*
"""

import threading
import serial
import sys
import os
import time, datetime
from random import randint
from enum import Enum
import math
#import pyautogui as hmi
#from pynche.pyColorChooser import *

import libs.commands as commands
from libs.list_ports import *

#leds
Red = 'r'
Green = 'g'
Blue = 'b'
All = 'a'

On = 255
Off = 0

#utils
#generate random number
def randomNumber(start, end):
    return randint(start, end)
#end

#join two objects
def join(token1, token2):
    return '{0}{1}'.format(token1, token2)
#end

#delay milliseconds
def wait(millis):
    time.sleep((millis/1000))
#end

#write message to console
def console(message):
	print(message)
	sys.stdout.flush()
#end
#map data
def map(val, in_min, in_max, out_min, out_max):
    return ((val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
#end

#region fonts
class Fonts:
    calibri         = 'c'
    calibri_light   = 'i'
    digital         = 'd'
    ocr_extended   = '0'
    font_big        = 'f'
    font_small      = 'g'
    comic_sans      = 's'

class Font:
    ocr             = 'c'
    terminal        = 'i'
    peanut         = 'd'
    comic           = 'o'
    calibri         = 'f'
    consolas        = 'g'
    droid           = 's'
    #peanut          = 't'
    #transformer     = 'r'
    #trebuchet       = 'b'
    elephant        = 'h'
    atomic          = 'a'
    icon_small      = 'p'
#end


#region fonts
class Control:
    rotate_0    = 'p'
    rotate_90   = 'i'
    rotate_180  = 'q'
    rotate_270  = 'n'
    clear_display = 'c'
    power_off = 'f'
    power_on = 'o'
    Do1 = '1'
    Do2 = '2'
    Do3 = '3'
#end

#sensor info
    """
class SensorInfo:
    angleSensor = 0
    lightSensor = 0
    A1 = 0
    A2 = 0
    SwitchOne = 0
    SwitchTwo = 0
    Do2 = 0
    Do1 = 0
    remoteCode = 0"""
#end

class BoardNotFound(Exception): pass

#end utils
false = 0
true = 1
#board class
class scratch_n_sketch(Fonts, Control):
    #sensors init
    AngleSensor = 0
    LightSensor = 0
    TempSensor = 0
    A1 = 0
    A2 = 0
    Switch = 0
    Di2 = 0
    Di1 = 0
    Di3 = 0
    RemoteCode = 0
    TouchX = 0
    TouchY = 0
    brightness = 255;

    #initialize
    def __init__(self):
        self.errorMsg = 'none'
        #self.ser = serial.Serial(port, 230400, timeout=1)
        #self.ser.close()
    #end

    def connect(self, port = 'p'):
        try:
            console('-'*20)
            console('searching scratch-n-sketch')
            if len(port) > 1:
                self.ser = serial.Serial(port, 230400, timeout=1)
                self.ser.close()
            else:
                ports = serial_ports()
                if len(ports) > 0:
                    cpt = find_port(ports)
                    if ('COM' in cpt) or ('/dev' in cpt):
                        console(join('Found!, Accesing port : ' , cpt))
                        console('Board connected successfully!') # : ' + cpt)
                        console('-'*20)
                        self.ser = serial.Serial(cpt, 230400, timeout=1)
                        self.ser.close();
                else:
                    raise BoardNotFound#Exception('Board not found')
        except:
            console('cant find board! please reconnect it.')
            os._exit(0)

    #send helper
    def sendHelper(self, out):
        try:
            if not self.ser.isOpen():
                    self.ser.open()
            #self.ser.flushOutput()
            self.ser.write(('<' + out + '>').encode())
            self.ser.flush()
        except:
            console('can\'t communicate with the port!')
            os._exit(0)
    #end

    #populate sensor info
    def __populateSensorData(self, data):
        if data[0] == 'a' and len(data) == 10:
            self.AngleSensor = int(data[1])
            self.LightSensor = int(data[2])
            self.A1 = int(data[3])
            self.A2 = int(data[4])
            self.Switch = ((int(data[5]) >> 3) & 1)
            self.Di1 = (int(data[5])  & 1)
            self.Di2 = ((int(data[5]) >> 1) & 1)
            self.Di3 = ((int(data[5]) >> 2) & 1)
            self.RemoteCode = data[6]
            self.TouchX = int(data[7])
            self.TouchY = int(data[8])
            self.TempSensor = int(data[9])
    #end

    #get sensor data
    def getSensorData(self):
        try:
            if not self.ser.isOpen():
                    self.ser.open()
            self.ser.write(b'<0xE0>')
            self.ser.flush()
            sensors = (str(self.ser.readline(), 'utf8')).split(',')
            """while (not (len(sensors) == 10)) and blocking == True:
                self.ser.write(b'<0xE0>')
                sensors = (str(self.ser.readline(), 'utf8')).split(',')
            """
            self.__populateSensorData(sensors)
        except:
            console('Failed to retrieve sensor info!')
            os._exit(0)
            pass

    #clear screen
    def clearDisplay(self):
        data = '{0}|{1}'.format(commands.ctl, 'c')
        self.sendHelper(data)
        #self.errorMsg = 'Failed to clear screen'
    #end

    #clear screen
    def digitalWrite(self, l, x):
        data = '{0}|{1}|{2}'.format(commands.dout, l, x)
        self.sendHelper(data)
    #end

    #change background color
    def rgbLed(self, r, g, b, brightness=255):
        r = (r * brightness) >> 8;
        g = (g * brightness) >> 8;
        b = (b * brightness) >> 8;
        data = '{0}|{1}|{2}|{3}'.format(commands.wsled, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set background color'
    #end

    #change background color
    def backGroundColor(self, r, g, b):
        data = '{0}|{1}|{2}|{3}'.format(commands.fsc, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set background color'
    #end

    #change pen color
    def penColor(self, r, g, b):
        data = '{0}|{1}|{2}|{3}'.format(commands.pen, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set pen color'
    #end

    #image begin
    def imageBegin(self, px, py, img_w, img_h):
        data = '{0}|c'.format(commands.ime)
        #self.sendHelper(data)
        data = data + '><{0}|{1}|{2}|{3}|{4}'.format(commands.ims, px, py, img_w, img_h)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set text back color'
    #end

    #image data
    def imageData(self, img):
        self.sendHelper(img)

    #image end
    def imageEnd(self):
        data = '{0}|s'.format(commands.ime)
        self.sendHelper(data)

    #change text back color
    def textBackColor(self, r, g, b):
        data = '{0}|{1}|{2}|{3}'.format(commands.tbc, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set text back color'
    #end

    #draw text
    def drawText(self, text, xpos, ypos):
        data = '{0}|{1}|{2}|{3}'.format(commands.txt, text,
                                        xpos, ypos)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #erase text from specified position
    def eraseText(self, num, xpos, ypos):
        data = '{0}|{1}|{2}|{3}'.format(commands.ers, num,
                                        xpos, ypos)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw pixel
    def drawPixel(self, x, y):
        data = '{0}|{1}|{2}'.format(commands.dpx, x, y)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled rectangle
    def drawLine(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.drl, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled rectangle
    def fillRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.frt, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty rectangle
    def drawRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.drt, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty round rectangle
    def fillRoundRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.frr, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled round rectangle
    def drawRoundRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.drr, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled circle
    def fillCircle(self, x, y, r):
        data = '{0}|{1}|{2}|{3}'.format(commands.fcr, x, y, r)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty circle
    def drawCircle(self, x, y, r):
        data = '{0}|{1}|{2}|{3}'.format(commands.dcr, x, y, r)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled ellipse
    def fillEllipse(self, x, y, w, h):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.fep, x, y, w, h)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty ellipse
    def drawEllipse(self, x, y, w, h):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.dep, x, y, w, h)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw arc
    def drawArc(self, x, y, s, e, r, t):
        data = '{0}|{1}|{2}|{3}|{4}|{5}|{6}'.format(commands.dac, x,
                                                    y, s, e, r, t)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end
    """
    #draw battery level icon
    def drawBatteryIcon(self, x, y, l):
        data = '{0}|{1}|{2}|{3}'.format(commands.bli, x, y, l)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw progress bar icon
    def drawProgressIcon(self, x, y, l):
        data = '{0}|{1}|{2}|{3}'.format(commands.pgi, x, y, l)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw toggle icon
    def drawToggleIcon(self, x, y, st):
        data = '{0}|{1}|{2}|{3}'.format(commands.tgi, x, y, st)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #show calendar icon
    def showCalendar(self, dt, wk, mth, rh):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.cal, dt,
                                        wk, mth, rh)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end
    """
    #set font
    def setFont(self, x):
        data = '{0}|{1}'.format(commands.fnt, x)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #rotate display
    def rotateDisplay(self, x):
        data = '{0}|{1}'.format(commands.ctl, x)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #power control
    def powerControl(self, x):
        data = '{0}|{1}'.format(commands.ctl, x)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #set screen brightness
    def displayBrightness(self, l):
        data = '{0}|{1}'.format(commands.bgt, l)
        self.sendHelper(data)
        wait(1)
        #self.errorMsg = 'Failed to draw text'
    #end

    #led write
    def ledWrite(self, l, x):
        data = '{0}|{1}|{2}'.format(commands.led, l, x)
        self.sendHelper(data)
        wait(1)
        #self.errorMsg = 'Failed to draw text'
    #end

    #disconnect board
    def disconnect(self):
        try:
            if self.ser.isOpen():
                self.ser.close()
        except:
            console('Failed to disconnect board')
            os._exit(0)
    #end
#end board class
