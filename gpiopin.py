import RPi.GPIO as GPIO
import time
Trig = 27
Echo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

maa = 17
mab = 14
mba = 22
mbb = 15
GPIO.setup(maa, GPIO.OUT)
GPIO.setup(mab, GPIO.OUT)
GPIO.setup(mba, GPIO.OUT)
GPIO.setup(mbb, GPIO.OUT)
def read_distance():
    GPIO.output(Trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trig, GPIO.LOW)
    while GPIO.input(Echo) == GPIO.LOW:
        sig_off = time.time()
    while GPIO.input(Echo) == GPIO.HIGH: 
        sig_on = time.time()
    duration = sig_on - sig_off
    distance = duration * 34000 / 2
    return distance
def spdis(recors):
    i = 0
    value = 0
    while recors != i:
        value = value + read_distance()
        i = i + 1
    return value / recors
def speed():
    f = spdis(100)
    time.sleep(0.1)
    i = spdis(100)
    if f >= i:
        sa = f - i
    else:
        sa = i - f
    sp = sa / 0.1
    print(str(f), "s")
    print(str(i), "f")
    return str(sp)
def moter(ct, sp):
    print(str(sp) + ct)
    GPIO.output(maa, GPIO.LOW)
    GPIO.output(mba, GPIO.LOW)
    GPIO.output(mab, GPIO.LOW)
    GPIO.output(mbb, GPIO.LOW)
    if ct == "f":
        GPIO.output(maa, GPIO.HIGH)
        GPIO.output(mba, GPIO.HIGH)
        time.sleep(0.07)
        GPIO.output(maa, GPIO.LOW)
        GPIO.output(mba, GPIO.LOW)
    if ct == "r":
        GPIO.output(maa, GPIO.HIGH)
        time.sleep(0.07)
        GPIO.output(maa, GPIO.LOW)
    if ct == "l":
        GPIO.output(mba, GPIO.HIGH)
        time.sleep(0.07)
        GPIO.output(mba, GPIO.LOW)
