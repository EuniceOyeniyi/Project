import pyttsx3 as pt
import speech_recognition as sr
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import os
import sys
os.system("cls")  #Clearing the screen




def Speak(text):
    # Initialize the engine
    engine = pt.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say(text)
    engine.runAndWait()


def getaudio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # recognizer.energy_threshold=10000
        recognizer.adjust_for_ambient_noise(source)
        # Speak("I'm listening")
        recognizer.dynamic_energy_threshold = True  
        audio2 = recognizer.listen(source)
        
        try:
            s = recognizer.recognize_google(audio2)
            s = s.lower()
            return s
            
        except:
            # Speak("I didn't get that, please try to speak more clearly")
            pass


def getaudio2():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # recognizer.energy_threshold=10000
        recognizer.adjust_for_ambient_noise(source)
        Speak("How may I help you")
        recognizer.dynamic_energy_threshold = True  
        audio2 = recognizer.listen(source)
        
        try:
            s = recognizer.recognize_google(audio2)
            s = s.lower()
            return s
            
        except:
            Speak("I didn't get that, please try to speak more clearly")
            pass


def play_song(song_or_video):
    search_box=driver.find_element(By.NAME, "search_query")
    search_box.click()
    search_box.clear()
    search_box.send_keys(song_or_video)
    search_box.send_keys(Keys.ENTER)
    time.sleep(5)
    video = driver.find_elements(By.ID, 'thumbnail')
    try:
        checker = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[2]/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-search-pyv-renderer/div/ytd-promoted-video-renderer/div/div[1]/a/div/div[2]/div/ytd-badge-supported-renderer/div/span").text
    
        
        if checker == "Ad":
            videos = [i for i in video if i.is_displayed()]

            videos[1].click()
        
            
    except:
        videos = [i for i in video if i.is_displayed()]
        videos[0].click()

    

def full_screen():
    screen_button = driver.find_element(By.CLASS_NAME ,'ytp-fullscreen-button' )
    screen_button.click()

def skip_ad():
            skipping =driver.find_element(By.CLASS_NAME,"ytp-ad-skip-button")
            skipping.click()
        

def pause_song():
    button = driver.find_element(By.CLASS_NAME ,'ytp-play-button' )
    button.click()

def continue_song():
    cont_button = driver.find_element(By.CLASS_NAME ,'ytp-play-button' )
    cont_button.click()

def next_song():
    next_button = driver.find_element(By.CLASS_NAME ,'ytp-next-button' )
    next_button.click()

def replay_song():
    button=driver.find_element(By.CLASS_NAME,'ytp-play-button')
    check_end=button.get_attribute('title')
    check_end=check_end.lower()
    print(check_end)
    if(check_end=='replay'):
        button.click()

def subtitle():
    driver.find_element(By.CLASS_NAME, "ytp-subtitles-button").click()

def shut_down():
    Speak('ByeBye')
    driver.quit()
    sys.exit()





while True:
    commands = getaudio()
        
    if commands == 'hello':
        # Speak("How may I help you")
        commands = getaudio2()
        print(commands)
        
        
        if 'play' in commands:
            # os.remove('../SER/femi.wav')
            to_do = commands.split('play')[1]
            print(to_do)
            pth = Service("../chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(service=pth,options=options)
            driver.get('https://www.youtube.com/')
            button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")) )
            button.click()
            time.sleep(4)
                    
            play_song(to_do)
            
        if commands == 'stop':
            pause_song()
        elif commands == 'continue':
            pause_song()
        elif commands == 'skip':
            skip_ad()
        elif commands == 'next':
            next_song()
        elif commands == 'subtitle':
            subtitle()
        elif commands == 'shutdown':
            shut_down()

       



