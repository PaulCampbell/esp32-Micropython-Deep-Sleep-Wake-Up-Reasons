# ESP32 micropython deepsleep reasons

Micropython on the ESP32 can be put into deepsleep.

It can be woken from deepsleep from mulitple pins using [esp32.wake_on_ext1](https://docs.micropython.org/en/latest/library/esp32.html#esp32.wake_on_ext10).

Unfortunately there is no way to find out which particular IO pin woke the device.

Here's a trick if you only have 2 different inputs that are going to wake the device:

Get one to `wake_on_ext0`, and the other to `wake_on_ext1`.

`machine.wake_reason` will then report 2 for wake_on_ext0 and 3 for wake_on_ext1

## test it out

Put micropython on your controller

```
esptool.py --baud 115200 --port /dev/tty.SLAB_USBtoUART erase_flash
esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART --baud 115200 write_flash 0x1000  ./esp32-idf3-20200327-v1.12-310-g9418611c8.bin
```

Copy the code there

```
ampy put ./main.py main.py
```

watch the output

```
screen /dev/tty.SLAB_USBtoUART 115200 -L
```
