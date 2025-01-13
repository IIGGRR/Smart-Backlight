import network
import espnow
import time
from machine import Pin

but1 = Pin(5, Pin.IN, Pin.PULL_UP)  # пин для внешней кнопки
but2 = Pin(4, Pin.IN, Pin.PULL_UP)  # пин для внешней кнопки
but3 = Pin(14, Pin.IN, Pin.PULL_UP)  # пин для внешней кнопки

sta = network.WLAN(network.STA_IF)  # Enable station mode for ESP
sta.active(True)
sta.disconnect()  # Disconnect from last connected WiFi SSID

e = espnow.ESPNow()  # Enable ESP-NOW
e.active(True)

peer1 = b''  # MAC address of peer2's wifi interface
e.add_peer(peer1)  # add peer2 (receiver2)c8:c9:a3:39:10:f6
print("Starting...")  # Send to all peers


def start():
    while True:
        msg = [0, 0, 0]
        if but1.value() == 0:
            msg[0] = 1
        if but2.value() == 0:
            msg[1] = 1
        if but3.value() == 0:
            msg[2] = 1
        time.sleep(0.25)
        result = ''
        for i in msg:
            result += str(i)
        e.send(peer1, result, True)
        print(result)


if __name__ == '__main__':
    start()
