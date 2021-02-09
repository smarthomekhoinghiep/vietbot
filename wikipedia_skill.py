import wikipedia
import speaking
import feedparser
import time
import gih
from speaking import speak, short_speak
import os
import random
import yaml
import gih
import threading
import psutil
from termcolor import colored
import threading
from threading import Thread
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_wikipedia = gih.get_request('request_wikipedia')
request_wikipedia_thing=gih.get_request('request_wikipedia_thing')
response_wikipedia_thing=gih.get_response('response_wikipedia_thing')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
def main(data):
    print('[BOT]: XỬ LÝ CÂU HỎI BẰNG WIKI: '+data)
    if any(item in data for item in request_wikipedia_thing):
        wiki_obj = str([s for s in request_wikipedia_thing if s in data])
        wiki_obj = wiki_obj.replace("['", "")
        wiki_obj = wiki_obj.replace("']", "") 
        data = data.replace(wiki_obj,'')
        if len(data) > 0:
            wiki_func(data.lower())            
        else:
            short_speak(random.choice(response_wikipedia_thing))
            more_data=getText()    
            if more_data is not None:
                if any(item in more_data for item in request_wikipedia_thing):
                    wiki_obj = str([s for s in request_wikipedia_thing if s in more_data])
                    wiki_obj = wiki_obj.replace("['", "")
                    wiki_obj = wiki_obj.replace("']", "") 
                    more_data = more_data.replace(wiki_obj,'')
                    if len(data) > 0:
                        wiki_func(more_data.lower())            
                    else:
                        short_speak(random.choice(response_say_nothing))
                        pass                    
                else:
                    wiki_func(more_data.lower())            
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
    
def wiki_func(data):
    # data = data[0:len(data)-6]
    rep = find_info(data)
    rep = rep.find_wiki()
    print('[BOT]: Theo wikipedia: '+rep)
    speak('Theo wikipedia: '+rep)
    pass
    
def run_thread(func,data=None):
    if data is not None:
        t = threading.Thread(target = func, args = (data,))
        t.start()
    else:
        t = threading.Thread(target = func, args = ())
        t.start()
        
class find_info():

    def __init__(self,data):
        self.data = data
    def find_wiki(self):
        wikipedia.set_lang('vi')
        datarep = wikipedia.summary(self.data, sentences = 1)
        return datarep


if __name__ == '__main__':
    main(data)
