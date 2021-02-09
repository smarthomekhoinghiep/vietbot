#import news
import feedparser
from speaking import speak, short_speak
import random
import gih
import re
import os
from termcolor import colored
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_news_link=gih.get_request('request_news_link')
request_news_name=gih.get_request('request_news_name')
response_news=gih.get_response('response_news')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
data = 'TIN TỨC HÔM NAY THANH NIÊN'
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH TIN TỨC: '+data)
    if any(item in data for item in request_news_name):    
        if request_news_name[0] in data:
            read_news(0,0)
        elif request_news_name[1] in data:
            read_news(1,1)
        elif request_news_name[2] in data:
            read_news(2,2)    
        elif request_news_name[3] in data:
            read_news(3,3)    
    else:
        short_speak(random.choice(response_news))     
        more_data=getText()    
        if more_data is not None:
            more_data=more_data.upper()    
            if any(item in more_data for item in request_news_name):    
                if request_news_name[0] in more_data:
                    read_news(0,0)
                elif request_news_name[1] in more_data:
                    read_news(1,1)
                elif request_news_name[2] in more_data:
                    read_news(2,2)    
                elif request_news_name[3] in more_data:
                    read_news(3,3) 
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

def read_news(data1,data2):

    newsFeed = feedparser.parse(request_news_link[data1])   
    i =1
    while i < 6: 
        entry = newsFeed.entries[i]
        print (entry.published)
        clean = re.compile('<.*?>')
        clean_content= re.sub(clean, '', entry.summary)
        speak('Tin mới nhất từ '+ request_news_name[data2] +" "+clean_content)        
        entry = None
        clean = None
        clean_content = None        
        i += 1

        
if __name__ == '__main__':
    main(data)