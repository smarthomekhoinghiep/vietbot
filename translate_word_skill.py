#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import speak, speaken, speakja, speakko, speakzh

import os
import random
import yaml
import gih
import re
import googletrans
from googletrans import Translator
# from pygame import mixer
# mixer.init()
from termcolor import colored

import main_process
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')

def main(data):
    print('[BOT]: XỬ LÝ DỊCH TỪ: '+data)
    print('---------')
                    
# Dịch từ
    translator = Translator()
    print (data)
    data = data.replace('TỪ ','')
    data = data.replace('TRONG ','')
#       print ('Edit ' + data)

# To Vietnamese
    if 'VIỆT' in data:
        m = re.search ('(.+?) TIẾNG VIỆT', data)
        dataen = m.group(1)
        print (dataen)
        translations = translator.translate (dataen, dest = 'vi')
        print (translations.text)
        speak('Từ ')
        speaken (dataen)
        speak('trong tiếng việt nghĩa là: '+ translations.text)        
#To English
    elif 'ANH' in data:
        m = re.search ('(.+?) TIẾNG ANH', data)
        dataen = m.group(1)
        print (dataen)
        translations = translator.translate (dataen, dest = 'en')
        print (translations.text)
        speak ('Từ '+dataen +' trong tiếng Anh nghĩa là: ')
        speaken(translations.text)
# To Korean
    elif 'TIẾNG HÀN' in data:
        m = re.search ('(.+?) TIẾNG HÀN', data)
        dataen = m.group(1)
        print (dataen)
        translations = translator.translate (dataen, dest = 'ko')
        print (translations.text)
        speak ('Từ '+dataen +' trong tiếng Hàn nghĩa là: ')
        speakko(translations.text)
# To Japanese
    elif 'TIẾNG NHẬT' in data:
        m = re.search ('(.+?) TIẾNG NHẬT', data)
        dataen = m.group(1)
        print (dataen)
        translations = translator.translate (dataen, dest = 'ja')
        print (translations.text)
        speak ('Từ '+dataen +' trong tiếng Nhật nghĩa là: ')
        speakja(translations.text)
# To Chinese
    elif 'TIẾNG TRUNG' in data:
        m = re.search ('(.+?) TIẾNG TRUNG', data)
        dataen = m.group(1)
        print (dataen)
        translations = translator.translate (dataen, dest = 'zh-cn')
        print (translations.text)
        speak ('Từ '+dataen +' trong tiếng TRUNG nghĩa là: ')
        speakzh(translations.text)

if __name__ == '__main__':
    main(data)