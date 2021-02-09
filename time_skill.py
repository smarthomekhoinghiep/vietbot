#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import short_speak

import os
import random
import yaml
import gih

# from pygame import mixer
# mixer.init()
from termcolor import colored
import main_process
from time import ctime, strftime

def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH HỎI GIỜ: '+data)
    print('---------')
    gio = strftime("%H")
    gio = list(gio)
    phut=strftime("%M")
    phut=list(phut)
    if gio[0]=='1':
        if gio[1]=='0':
            docgio='mười giờ '
        else:
            docgio='mười '+gio[1]+ ' giờ '
    elif gio[0]=='0':
        docgio= gio[1] +' giờ '
    elif gio[0]=='2':
        if gio[1]=='0':
            docgio='hai mươi giờ '
        elif gio[1]=='1':
            docgio='hai mươi mốt giờ '
        else:
            docgio='hai mươi '+ gio[1] + ' giờ '        
    if phut[0]=='0':
        docphut = phut[1]+ ' phút '
    elif phut[0]=='1':
        if phut[1]=='0':
            docphut= ' mười phút '
        else:
            docphut = ' mười '+ phut[1]+ ' phút '
    else:
        if phut[1]=='0':
            docphut=phut[0] + ' mươi phút '
        elif phut[1]=='1':
            docphut=phut[0] + ' mươi mốt phút '
        else:
            docphut = phut[0]+ ' mươi '+ phut[1]+ ' phút '
    short_speak(random.choice(gih.get_response('response_moment')) +' LÀ ' + docgio + docphut)
    
    




if __name__ == '__main__':
    main(data)