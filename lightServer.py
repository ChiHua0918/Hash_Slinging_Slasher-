#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import PixelStrip, Color
import argparse
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler  # 指令接收 CallbackQuery
from telegram.ext import PollAnswerHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton  # 互動式按鈕
import random
import json
# 文字轉語音
from gtts import gTTS
from os import system
from flask import Flask, request, make_response, render_template, send_file
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index() :
    formData = request.args['mode']
    print(formData)
    myKeyWord(formData)
    return make_response('OK', 200)

# LED strip configuration:
LED_COUNT = 111        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

iterations = 20

def myKeyWord(formData) :
    result = ["creepy", "relax", "party", "werewolf", "sleep", 
              "Christmas", "NewYear", "thePurge", "fu-chou-gui", "pao", 
              "clap", "Birthday", "conan", "so", "music",
              "turnOff", "WTM"]
    lightMode = [creepy, relax, party, werewolf, sleep, 
                Christmas, newyear, thePurge, slasher, fuck, 
                fierce, birthday, conan, turnOff, theaterChaseRainbow,
                turnOff, thePurge]

    # for i in range(len(type)) :
    #     if (formData == result[i]) :
    #         lightMode[i]()
    #         return

    while True:
    # print("ttttttt" + str(result.index(formData)))
    # print(type(result.index(formData)))
        lightMode[result.index(formData)]()
    return
    
# Define functions which animate LEDs in various ways.
def colorWipe(color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(50 / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


# def rainbowCycle(strip, wait_ms=20, iterations=5):
def rainbowCycle():
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)


# def theaterChaseRainbow(strip, wait_ms=50):
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
    print("鬼故事")
    # oneColor(Color(0, 255, 0)) #綠
    # time.sleep(2)
    # rainbow
    for j in range(255 * iterations, 240 * iterations, -1):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)
    for j in range(240 * iterations, 255 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(50 / 1000.0)

def newyear():
    print("新年")
    # oneColor(Color(255, 63, 24)) #紅
    # time.sleep(2)
    #theaterChase
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
    print("生日")
    # oneColor(Color(232, 255, 17)) #黃
    # time.sleep(2)
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
    print("打炮")
    # oneColor(Color(255, 17, 160)) #粉
    # time.sleep(2)
    # rainbow
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
    print("激烈做愛")
    # oneColor(Color(255, 17, 160)) #粉
    # time.sleep(2)
    #theaterChase
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
    print("派對")
    # oneColor(Color(249, 255, 38)) #紅
    # time.sleep(2)
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
    print("放鬆")
    # oneColor(Color(67, 230, 192)) #藍綠
    # time.sleep(2)
    # rainbow
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
    print("睡覺")
    # oneColor(Color(100, 255, 236)) #藍
    # time.sleep(2)
    # rainbow
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
    print("聖誕節")
    # oneColor(Color(255, 9, 0)) #紅
    # time.sleep(2)
    #theaterChase
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


def werewolf():
    print("狼人殺")
    # oneColor(Color(132, 30, 223)) #紅
    # time.sleep(2)
    # rainbow
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
    print("夜光閃亮亮復仇鬼")
    # oneColor(Color(13, 181, 35)) #綠
    # time.sleep(2)
    #theaterChase
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, Color(0, 171, 255))
                strip.setPixelColor(i + 1 + q, Color(255, 255, 255))
            strip.show()
            time.sleep(500 / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)
            time.sleep(50 / 1000.0)


def conan():
    print("真相永遠只有一個")
    # oneColor(Color(12, 27, 225)) #藍
    # time.sleep(2)
    #colorWipe
    for i in range(0, strip.numPixels(), 2):
        strip.setPixelColor(1, Color(84, 255, 250))
    for i in range(strip.numPixels(), ):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    time.sleep(600 / 1000.0)

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
    iterations = 0
    while iterations < 5:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
        time.sleep(1)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(255, 255, 255))
        strip.show()
        time.sleep(1)
        iterations = iterations + 1

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
