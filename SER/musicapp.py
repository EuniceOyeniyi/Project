import pyttsx3 as pt
import speech_recognition as sr
import pywhatkit
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import os
import sys
os.system("cls")  #Clearing the screen


recognizer = sr.Recognizer()

def Speak(text):
    # Initialize the engine
    engine = pt.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()


def getaudio():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio2 = recognizer.listen(source)
    try: 
        s = recognizer.recognize_google(audio2,language="en").lower()
        print(s)
        
    except:
        Speak("I don't seems to get that!")


def play_song(song_or_video):
    search_box=driver.find_element(By.NAME, "search_query")
    search_box.click()
    search_box.clear()
    search_box.send_keys(song_or_video)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)
    video = driver.find_elements(By.ID, 'thumbnail')
    videos = [i for i in video if i.is_displayed()]
    videos[0].click()

def full_screen():
    screen_button = driver.find_element(By.CLASS_NAME ,'ytp-fullscreen-button' )
    screen_button.click()

def skip_ad():
        try:
            driver.find_element(By.CLASS_NAME,"ytp-ad-skip-button").click()
            # return driver.find_element(By.CLASS_NAME,"ytp-ad-skip-button").text
        except:
            return None








pth = Service("../chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=pth,options=options)
driver.get('https://www.youtube.com/')
time.sleep(5)

button = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
button.click()
time.sleep(5)
play_song('calm songs')