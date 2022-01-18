import time
from rpi_ws281x import PixelStrip, Color
from os import system
from flask import Flask, request, make_response, render_template, send_file
import threading
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index() :
    global light_thread
    print("The pid is ", os.getpid())
    formData = request.args['mode']
    print(formData)
    light_thread = None
    myKeyWord(formData)
    # return make_response('OK', 200)

# LED strip configuration:
LED_COUNT = 111       
LED_PIN = 18 
LED_FREQ_HZ = 800000   
LED_DMA = 10 
LED_BRIGHTNESS = 255 
LED_INVERT = False
LED_CHANNEL = 0 

iterations = 20
light_thread = None

def myKeyWord(formData) :
    global light_thread
    result = ["creepy", "relax", "party", "startWerewolf", "sleep", 
              "Christmas", "NewYear", "thePurge", "fu-chou-gui", "pao", 
              "clap", "Birthday", "conan", "so", "music",
              "turnOff", "WTM", "werewolf", "witch", "predictor",
              "breakingDawn"]
    lightMode = [creepy, relax, party, startWerewolf, sleep, 
                Christmas, newyear, thePurge, slasher, fuck, 
                fierce, birthday, conan, turnOff, theaterChaseRainbow,
                turnOff, thePurge, werewolf, witch, predictor,
                breakingDawn]
    
    
    light_thread = threading.Thread(target=lightMode[result.index(formData)]())
    light_thread.start()

    #while(True):

#一個一個點亮
def colorWipe(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(50 / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle():
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)


def theaterChaseRainbow(wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)
            

#一次亮所有顏色
def oneColor(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def creepy():
    print("creepy")
    # oneColor(Color(0, 255, 0)) #綠
    # time.sleep(2)
    # rainbow
    for j in range(260 * iterations, 250 * iterations, -1):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)
    for j in range(250 * iterations, 260 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)

def newyear():
    print("newYear")
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 4):
                strip.setPixelColor(i + q, Color(255, 119, 0))
                strip.setPixelColor(i + 1 + q, Color(255, 0, 2))
            strip.show()
            time.sleep(700 / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + 2, 0)
                strip.setPixelColor(i + 3, 0)
            strip.show()

def birthday():
    print("Birthday")
    for i in range(0, strip.numPixels(), 2):
        strip.setPixelColor(i, Color(239, 255, 0))
        strip.setPixelColor(i + 1, Color(18, 255, 10))
    strip.show()
    time.sleep(2)
    for i in range(1, strip.numPixels(), 2):
        strip.setPixelColor(i, Color(18, 255, 10))
        strip.setPixelColor(i + 1, Color(239, 255, 0))
    strip.show()
    time.sleep(1)

def fuck():
    print("fuck")
    for j in range(120 * iterations, 130 * iterations, 0.5):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(200 / 1000.0)
    for j in range(130 * iterations, 120 * iterations, -0.5):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(200 / 1000.0)

def thePurge():
    print("國定殺戮日")#被當
    oneColor(Color(255, 0, 0)) #紅
    time.sleep(2)
    oneColor(Color(0, 0, 0)) #紅
    time.sleep(2)

def fierce():
    print("fierce")
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, Color(255, 0, 111))
                strip.setPixelColor(i + 1 + q, Color(205, 0, 255))
            strip.show()
            time.sleep(100 / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + 2, 0)
            strip.show()

def party():
    print("party")
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, Color(255, 90, 0))
                strip.setPixelColor(i + 1 + q, Color(77, 0, 255))
                strip.setPixelColor(i + 2 + q, Color(0, 255, 134))
                strip.setPixelColor(i + 3 + q, Color(205, 0, 255))
            strip.show()
            time.sleep(200 / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)    

def relax():
    print("relax")
    for j in range(210 * iterations, 200 * iterations, -1):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)
    for j in range(200 * iterations, 210 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)

def sleep():
    print("sleep")
    for j in range(50 * iterations, 30 * iterations, -1):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(300 / 1000.0)
    for j in range(30 * iterations, 50 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(300 / 1000.0)

def Christmas():
    print("christmas")
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, Color(255, 68, 0))
                strip.setPixelColor(i + 1 + q, Color(239, 255, 0))
                strip.setPixelColor(i + 2 + q, Color(255, 255, 255))
            strip.show()
            time.sleep(500 / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def startWerewolf():
    print("startWerewolf")
    for j in range(50 * iterations, 20 * iterations, -1):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
            strip.show()
            time.sleep(50 / 1000.0)
    for j in range(20 * iterations, 50 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
            strip.show()
            time.sleep(50 / 1000.0)

def slasher():
    print("slasher")
    n = 0
    while n < 20:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(1)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 205, 255))
        strip.show()
        time.sleep(1)
        n = n + 1


def conan():
    print("真相永遠只有一個")
    # oneColor(Color(12, 27, 225)) #藍
    # time.sleep(2)
    #colorWipe
    for i in range(0, strip.numPixels(), 2):
        strip.setPixelColor(1, Color(84, 255, 250))
    strip.show()
    for i in range(strip.numPixels(), ):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    time.sleep(600 / 1000.0)

def werewolf():
    print("werewolf")
    colorWipe(Color(255, 0, 10))

def witch():
    print("witch")
    colorWipe(Color(196, 0, 255))

def predictor():
    print("predictor")
    colorWipe(Color(0, 255, 154))

def breakingDawn():
    print("breakingDawn")
    colorWipe(Color(239, 255, 0))

# 關燈
def turnOff():
    print("關燈")
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()


def turnOn():
    print("開燈")
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()
        time.sleep(500 / 1000)
    n = 0
    while n < 10:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(1)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()
        time.sleep(1)
        n = n + 1

def main() :
    # app.run(host='0.0.0.0', port=8081, threaded=True, debug=True)
    turnOn()

if __name__ == "__main__":
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    app.run(host='0.0.0.0', port=8081, threaded=True, debug=True)
    # main()
