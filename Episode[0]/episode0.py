from machine import Pin
from time import sleep

led_pi_pico = Pin(25, Pin.OUT)

print("Hello Friend")

while True:
    led_pi_pico.value(1)
    sleep(1)
    led_pi_pico.value(0)
    sleep(1)