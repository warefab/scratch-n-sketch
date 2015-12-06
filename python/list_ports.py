#scratch and sketch
from libs.board import *

console('checking serial ports.')
wait(500)

ports = serial_ports()

if len(ports) > 0:
    console(join('ports found : ', ports))
    #for port in ports:
        #console(join('>> ', str(port)))
else:
    console('no port not found')
wait(500)
