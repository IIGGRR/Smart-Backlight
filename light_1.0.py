import network
import espnow
from machine import Pin
import neopixel
import time

led_pin1 = 5
led_pin2 = 6
led_pin3 = 1
led_pin4 = 2
num_leds = 5


led2 = neopixel.NeoPixel(Pin(led_pin1, Pin.OUT), num_leds)
led4 = neopixel.NeoPixel(Pin(led_pin2, Pin.OUT), num_leds)
led1 = neopixel.NeoPixel(Pin(led_pin3, Pin.OUT), num_leds)
led3 = neopixel.NeoPixel(Pin(led_pin4, Pin.OUT), num_leds)

def stop(ld1=led1, ld2=led2):
    # загораем красным первую ленту
    led1.fill((255, 0, 0))
    led2.fill((255, 0, 0))
    led1.write()
    led2.write()
    
    time.sleep(0.5)
    
    led1.fill((0, 0, 0))
    led2.fill((0, 0, 0))
    led1.write()
    led2.write()


def rotate(ld):
    for i in range(num_leds):
        ld[i] = (255, 255, 0)
        ld.write()
        
    ld.fill((0, 0, 0))
    ld.write()
    
    
def hello(ld1=led1, ld2=led2, ld3=led3, ld4=led4):
    for i in range(num_leds):
        ld1[i] = (0, 255, 0)
        ld2[i] = (0, 255, 0)
        ld3[i] = (0, 255, 0)
        ld4[i] = (0, 255, 0)
        ld1.write()
        ld2.write()
        ld3.write()
        ld4.write()
        time.sleep(0.1)
    ld1.fill((0, 0, 0))
    ld2.fill((0, 0, 0))
    ld3.fill((0, 0, 0))
    ld4.fill((0, 0, 0))
    ld1.write()
    ld2.write()
    ld3.write()
    ld4.write()
    print('hello')
    
    
if __name__ == "__main__":

    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()                # Disconnect from last connected WiFi SSID

    e = espnow.ESPNow()                  # Enable ESP-NOW
    e.active(True)
    e1 = espnow.ESPNow()                  # Enable ESP-NOW
    e1.active(True)

    peer = b'' #MAC address of peer's wifi interface
    e.add_peer(peer)
    peer1 = b''
    e1.add_peer(peer1)
    hello()
    

    while True:
        host, result = e.recv()
        host1, result1 = e1.recv()
        msg = result.decode('utf-8')
        msg1 = result1.decode('utf-8')
        if msg[0] == '1' or msg1[0]  == '1':
            stop()
        if msg[1] == '1' or msg1[1] == '1':
            rotate(led4)
        if msg[2] == '1' or msg1[2] == '1':
            rotate(led3)
        print(msg)
        
