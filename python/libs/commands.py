"""
*
* scratch_n_sketch
* Baords control commands
*
* (c) 2016 wwww.warefab.com
*
"""

#board commands

ims     =  '0xA0'   #image start*/
ime     =  '0xA1'   #image end*/
dpx     =  '0xA2'   #draw pixels*/
ust     =  '0xA3'   #usart speed*/
ver     =  '0xA4'   #version*/
ctl     =  '0xA5'   #display control*/
txt     =  '0xA6'   #draw text*/
pen     =  '0xA7'   #pen color*/
tbc     =  '0xA8'   #text back color*/
fsc     =  '0xA9'   #fill screen/background color*/
sbc     =  '0x9A'   #set brush color*/
ers     =  '0xB0'   #erase characters*/
frt     =  '0xB1'   #fill rectangle*/
drt     =  '0xB2'   #draw rectangle*/
frr     =  '0xB3'   #fill round rectangle*/
drr     =  '0xB4'   #draw round rectangle*/
drl     =  '0xB5'   #draw line*/
dvh     =  '0xB6'   #draw vertical/horizontal line*/
fcr     =  '0xB7'   #fill circle*/
dcr     =  '0xB8'   #draw circle*/
dep     =  '0xB9'   #draw ellipse*/
fep     =  '0xC0'   #fill ellipse*/
fnt     =  '0xC1'   #set font*/
dtr     =  '0xC2'   #draw triangle*/
ftr     =  '0xC3'   #fill triangle*/
tch     =  '0xC4'   #print char*/
dbi     =  '0xC5'   #draw bitmap image*/
btd     =  '0x5C'
dac     =  '0xC6'   #draw arc*/
sns     =  '0xE0'   #poll sensors*/
led     =  '0xE1'   #led control*/
dout    =  '0xE2'   #digital out*/
wsled   =  '0xE3'   #rgb led
bgt     =  '0xE5'  #tft backlight control
#end boards commands
