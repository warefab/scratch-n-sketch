
import serial
import sys
import time
import glob

#list ports
def serial_ports():
    """Lists serial ports

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

cpt = 'none'
def find_port(port):
    try:
        if len(port) > 0 :
            for prt in port:
                try:
                    cser = serial.Serial(prt, 230400, timeout = 1)
                    for i in range(0, 10):
                        cser.write(b'[0xA4]')
                        cser.flush()
                    if 'WFSN215V1' in (str(cser.readline(), 'utf8')):
                        cser.close()
                        return prt
                    """
                    #ser.setWriteTimeout(1)
                    line = str(ser.readline().splitlines()[0])
                    ver = line.split('\'', 2)[1]
                    if ver == 'WFSN215V1':
                        return str(prt)
                        ser.close()
                        #break;
                    ser.close()
                    """
                except:
                    pass
        return ''
    except:
        pass
"""
if __name__ == '__main__':
    try:
        cpt = find_port(serial_ports())
        if 'COM' in cpt:
            print('port found : ' + cpt)
    except:
        try:
            sys.exit()
        except:
            pass
"""
