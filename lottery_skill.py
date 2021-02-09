import os
import gih
from speaking import speak, short_speak
import random
import feedparser
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel

stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_lottery_area= gih.get_request('request_lottery_area')         
request_lottery_link= gih.get_request('request_lottery_link')
response_lottery_area=gih.get_response('response_lottery_area')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
# data = 'KẾT QUẢ SỔ XỐ MIỀN BẮC'
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH SỔ XỐ: '+data)
    data = data.upper()
    if any(item in data for item in request_lottery_area):
        lottery_area = str([s for s in request_lottery_area if s in data])
        lottery_area = lottery_area.replace("['", "")
        lottery_area = lottery_area.replace("']", "") 
        lottery_process(lottery_area)
    else:
        short_speak(random.choice(response_lottery_area))
        more_data=getText()    
        if more_data is not None:
            more_data=more_data.upper()            
            if any(item in more_data for item in request_lottery_area):
                lottery_area = str([s for s in request_lottery_area if s in more_data])
                lottery_area = lottery_area.replace("['", "")
                lottery_area = lottery_area.replace("']", "") 
                lottery_process(lottery_area)
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
def lottery_process(data):
    item_index=request_lottery_area.index(data)
    url = str(request_lottery_link[item_index])
    d = feedparser.parse(url)
    if 'CŨ HƠN' in data:
        tg = d['entries'][1]['title'] 
        kq = d['entries'][1]['description']
#       print(kq)
    else:
        tg = d['entries'][0]['title'] 
        kq = d['entries'][0]['description']
        print(kq)
    kq = kq.replace(']',': ')
    kq = kq.replace('ĐB:','Giải đặc biệt:')
    kq = kq.replace('1:','Giải nhất:')
    kq = kq.replace('2:','Giải nhì:')
    kq = kq.replace('3:','Giải ba:')
    kq = kq.replace('4:','Giải tư:')
    kq = kq.replace('5:','Giải năm:')
    kq = kq.replace('6:','Giải sáu:')
    kq = kq.replace('7:','Giải bảy:')
    x = kq.split("[")
    speak(tg)
    ketqua = '. '.join(x)
    ketqua = ketqua.replace('\n','. ')
    speak(ketqua)            

if __name__ == '__main__':
    main(data)        