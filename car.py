import detect
import gpiopin
import numpy as np

file_path = "/home/raspi5/ar_auto/test.txt"
dis = 0
temp = 0

def final_go(data):
    global dis
    global temp
    dis = gpiopin.read_distance()
    if dis >= 50:
        ar_track()
        gpiopin.moter("f", 0)
    else:
        dis = gpiopin.read_distance()
        if dis != None:
            while dis >= 20:
                dis = gpiopin.read_distance()
                gpiopin.moter("f", 0)
        else:
            dis = gpiopin.read_distance()
    print(dis)
rtr = 0
def ar_track():
    global rtr
    info = detect.ar_info()
    print(info)
    if info != None and info[0] == 0:
        if info[1] <= 485:
            data = "left"
            sp = 1 - info[1] / 512
            gpiopin.moter("l", sp)
        if info[1] >= 529:
            data = "right"
            sp = (info[1] - 512) / 512
            gpiopin.moter("r", sp)
        if info[1] >= 485 and info[1] <= 529:
            data = "center"
        print(data)
        rtr = (info[0], info[1], info[2], info[3], data)
        return rtr
    if info != None and info[0] == 1:
        gpiopin.moter("l", 1)
        gpiopin.moter("l", 1)
        gpiopin.moter("l", 1)
        gpiopin.moter("l", 1)
        gpiopin.moter("l", 1)
    if info != None and info[0] == 2:
        gpiopin.moter("r", 1)
        gpiopin.moter("r", 1)
        gpiopin.moter("r", 1)
        gpiopin.moter("r", 1)
        gpiopin.moter("r", 1)
def log(data):
    print(data)
    with open(file_path, "w") as file:
        file.write(str(data))
    print("log done")
while True:
    temp = ar_track()
    if temp != None:
        detect_info = temp[0]
        loc_info = temp[4]
        if loc_info == "center":
            final_go(detect_info)