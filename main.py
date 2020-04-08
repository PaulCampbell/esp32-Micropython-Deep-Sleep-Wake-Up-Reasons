# tested on TTGO TDisplay
from machine import Pin, deepsleep, wake_reason
import esp, esp32
from time import sleep

pir = Pin(13, Pin.IN, Pin.PULL_UP)
btn = Pin(12, Pin.IN)

print('Wake from deepsleep... reasons.')
esp.osdebug(None)

while True:
    reason = wake_reason()
    print('Wake Reason =', reason)
    if reason == 3:
        print('button')
    if reason == 2:
        print('PIR')

    sleep(5)

    esp32.wake_on_ext0(pin = pir, level = esp32.WAKEUP_ANY_HIGH)
    esp32.wake_on_ext1(pins = (btn, ), level = esp32.WAKEUP_ANY_HIGH)
    print('going to sleep')
    deepsleep()
