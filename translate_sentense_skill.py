#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import speak, speaken, speakja, speakko, speakzh
import re
import os
import random
import yaml
import gih
import googletrans
# from pygame import mixer
# mixer.init()
from termcolor import colored
from googletrans import Translator
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel

stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
response_translate_sentense=gih.get_response('response_translate_sentense')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
def main(data):
    print('[BOT]: XỬ LÝ DỊCH CÂU: '+data)
    print('---------')
# Dịch câu
    translator = Translator()
    speak(random.choice(response_translate_sentense))  
    more_data = getText()
    print (more_data)       
#       def gconv (data,more_data):
#           continue_go = 1
#           empty = []
    if more_data is not None:
        print ('Google translate: '+more_data)
        # print ('Data translate: '+more_data)
#              speak('')
        if 'TIẾNG VIỆT' in more_data:
            translations = translator.translate (more_data, dest = 'vi')
            print (translations.text)
            speak(translations.text)
        elif 'TIẾNG ANH' in more_data:
            translations = translator.translate (more_data, dest = 'en')
            print (translations.text)
            speaken(translations.text)
        elif 'TIẾNG HÀN' in more_data:
            translations = translator.translate (more_data, dest = 'ko')
            print (translations.text)
            speakko(translations.text)
        elif 'TIẾNG TRUNG' in more_data:
            translations = translator.translate (more_data, dest = 'zh-cn')
            print (translations.text)
            speakzh(translations.text)
        elif 'TIẾNG NHẬT' in more_data:
            translations = translator.translate (more_data, dest = 'ja')
            print (translations.text)
            speakja(translations.text)
        else:
            short_speak(random.choice(response_choose_lose))
            pass
    else:
        short_speak(random.choice(response_say_nothing))
        pass                          
def getText():
    #time.sleep(1)
#   Dùng STT Google Free
    if stt_engine == 0:
        data=input("Nhập lệnh cần thực thi:  ")
    elif stt_engine == 1:
        print(colored('---------------DÙNG STT GOOGLE FREE-----------------------','red'))
        data = stt_gg_free.main() 
#   Dùng STT Google Cloud
    elif stt_engine == 2:
        print(colored('---------------DÙNG STT GOOGLE CLOUD-----------------','green'))
        data = stt_gg_cloud.main()
#   Dùng STT VTCC
    elif stt_engine == 3:
        print(colored('---------------DÙNG STT VIETTEL-------------','blue'))        
        data = stt_viettel.main()        
    elif stt_engine == 4:
        print(colored('---------------DÙNG STT VIETTEL-------------','blue'))        
        data = stt_viettel_test.main()
#   Dùng STT FPT
    elif stt_engine == 5:
        print(colored('---------------DÙNG STT FPT-------------','yellow'))
        data = stt_fpt.py.main()
#   Sử dụng text input
    return data                                               
if __name__ == '__main__':
    main(data)