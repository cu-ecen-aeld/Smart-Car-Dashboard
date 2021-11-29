import serial
import os,time


sim800l = serial.Serial('/dev/ttyS0', baudrate = 9600,timeout=1)

sim800l.write(str.encode('AT' + '\r\n'))
rcv=sim800l.read(10)
print(rcv)
time.sleep(1)

sim800l.write(str.encode('AT+CMGF=1' + '\r\n'))
time.sleep(1)
print(sim800l.read(24))
time.sleep(1)

receiverNum = "+17206876733"
cmd1 = "AT+CMGS=\""+str(receiverNum)+"\"\n"
sim800l.write(cmd1.encode())
print(sim800l.read(40))
time.sleep(1)
message = "Cool shade stunner!!"
sim800l.write(str.encode(message))
sim800l.write(str.encode('\x1a'))
print(sim800l.read(24))
