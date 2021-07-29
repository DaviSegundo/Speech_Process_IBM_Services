import os
import pygame
import transcribe
import configparser
from googletrans import Translator
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def get_auth():
    config = configparser.RawConfigParser()
    config.read('speech.cfg')
    apikey = config.get('ibm', 'apikey')
    url = config.get('ibm', 'url')
    return (apikey, url)


def translate():
    with open('speech_text.txt', 'r') as f:
        arq = f.read()

    translator = Translator()
    text_en = translator.translate(arq, scr='pt', dest='en')

    return(text_en.text)


def auth(apikey, url):
    try:
        authenticator = IAMAuthenticator(apikey)
        tts = TextToSpeechV1(authenticator=authenticator)
        tts.set_service_url(url)
        print('*Authentication Success')
        return tts
    except:
        print('*Authentication Error')


def convert(tts, text):
    with open('text_speech.mp3', 'wb') as audio_file:
        res = tts.synthesize(text, 
                             accept='audio/mp3', 
                             voice='en-GB_CharlotteV3Voice').get_result()
        audio_file.write(res.content)
    print('*Converted')


def play_speech():
    print('*Playing Audio')
    pygame.init()
    pygame.mixer.music.load('text_speech.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
    input('Press any key to end.')
    print('*End')


def main():
    apikey, url = get_auth()
    tts = auth(apikey, url)
    text = translate()
    convert(tts, text)
    play_speech()
    

if __name__ == "__main__":
    transcribe.main()
    main()


