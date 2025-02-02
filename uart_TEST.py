import serial
import time

pico = serial.Serial('/dev/ttyAMA0', 3600, timeout=0.01)

def write(data):
    endata = "#" + str(data) + "_"
    pico.write(endata.encode())
    retry = 0
    while retry <= 5:
        temp = pico.read(32)
        rdata = temp.decode(errors='ignore')  # ここでerrors='ignore'を追加
        if rdata != endata:
            retry = 5
        retry += 1

def read():
    retry = 0
    while retry <= 5:
        data = pico.read(32)
        #decode...
        start = data.find(b"#")
        end = data.find(b"_")
        if start != -1 and end != -1 and start < end:
            decode = data[start + 1:end]
            redata = decode.decode('utf-8', errors='ignore')  # ここでerrors='ignore'を追加
            parts = redata.split(',')
            pico.write(("#" + redata + "_").encode())
            retry = 5
            return(parts)
        retry = retry + 1


def hcsr04():
    write("hcsr04")
    return read()
while True:
    print(hcsr04())