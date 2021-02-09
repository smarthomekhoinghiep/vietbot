#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
# from helper import *
# import spot

from speaking import short_speak
import random
import numpy as np
import gih

from termcolor import colored
response_random_number=gih.get_response('response_random_number')

def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH LẤY SỐ NGẪU NHIÊN: '+data)
    short_speak(random.choice(response_random_number) + ' '+ str(random.randint(0,99)))                     

if __name__ == '__main__':
    main(data)