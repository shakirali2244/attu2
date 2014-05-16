from socketIO_client import SocketIO

import serial
import threading

ser = serial.Serial(2, 9600, timeout=1)
print "server started"

def listener(*args):
    if args[0] =='forward':
        ser.write('w')
        print "great success"
    if args[0] =='backward':
        ser.write('s')
        print "great success"
    
    


socketIO = SocketIO('http://localhost:3000', 3000)
socketIO.on('python', listener)
socketIO.wait(seconds=6000)

