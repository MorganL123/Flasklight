from gpiozero import LED
from time import sleep

led = LED(17)


while True:
    in_or_off = input("Type on or off")
    if in_or_off == "on":
        led.on()
    elif in_or_off == "off":
        led.off()