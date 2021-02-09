from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import re
from speaking import short_speak
from termcolor import colored
import gih
import os
import random
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_day= gih.get_request('request_day')         
response_day=gih.get_response('response_day')
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH HỎI THỨ MẤY: '+data)
    if any(item in data for item in request_day):       
        if request_day[0] in data:        
            check_last_day()    
        elif request_day[1] in data:
            check_to_day()    
        elif request_day[2] in data: 
            check_tomorrow()
        elif request_day[3] in data:
            check_next_day()    
    else:        
        if 'NGÀY' in data and 'THÁNG' in data :
            check_other_day(data)           
        else:
            short_speak(random.choice(response_day))     
            more_data=getText()  
            if more_data is not None:
                more_data=more_data.upper()                  
                if any(item in more_data for item in request_day):       
                    if request_day[0] in more_data:        
                        check_last_day()    
                    elif request_day[1] in more_data:
                        check_to_day()    
                    elif request_day[2] in more_data: 
                        check_tomorrow()
                    elif request_day[3] in more_data:
                        check_next_day()                    
                else:                
                    if 'NGÀY' in data and 'THÁNG' in more_data:
                        check_other_day(more_data)                                               
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
    
def check_last_day():
    print ('Hôm qua')
    a = 'hôm qua'
    ngay = datetime.date.today() - timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    wd=date.weekday(ngay)    
    days= ["THỨ HAI","THỨ BA","THỨ TƯ","THỨ NĂM","THỨ SÁU","THỨ BẢY","CHỦ NHẬT"]
    if dd < 10:
        docngay = 'ngày mùng '+ str(dd) + ' '
    else: 
        docngay = 'ngày ' + str(dd) + ' '
    print(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    short_speak(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    
def check_to_day():
    a = 'hôm nay'
    print ('Hôm nay')
    ngay = datetime.date.today()
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    wd=date.weekday(ngay)    
    days= ["THỨ HAI","THỨ BA","THỨ TƯ","THỨ NĂM","THỨ SÁU","THỨ BẢY","CHỦ NHẬT"]
    if dd < 10:
        docngay = 'ngày mùng '+ str(dd) + ' '
    else: 
        docngay = 'ngày ' + str(dd) + ' '    
    print(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    short_speak(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    
def check_tomorrow():
    print ('Ngày mai')
    a = 'Ngày mai'
    ngay = datetime.date.today() + timedelta(1)
    yy =  ngay.year
    mm = ngay.month
    dd = ngay.day
    wd=date.weekday(ngay)    
    days= ["THỨ HAI","THỨ BA","THỨ TƯ","THỨ NĂM","THỨ SÁU","THỨ BẢY","CHỦ NHẬT"]
    if dd < 10:
        docngay = 'ngày mùng '+ str(dd) + ' '
    else: 
        docngay = 'ngày ' + str(dd) + ' '
    print(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    short_speak(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    
def check_next_day():
    print ('Ngày kia')
    a = 'ngày kia'
    ngay = datetime.date.today() + timedelta(2)
    yy = ngay.year
    mm = ngay.month
    dd = ngay.day
    wd=date.weekday(ngay)    
    days= ["THỨ HAI","THỨ BA","THỨ TƯ","THỨ NĂM","THỨ SÁU","THỨ BẢY","CHỦ NHẬT"]
    if dd < 10:
        docngay = 'ngày mùng '+ str(dd) + ' '
    else: 
        docngay = 'ngày ' + str(dd) + ' '    
    print(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    short_speak(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 

def check_other_day(data):
    today=datetime.date.today()
    print ('Ngày khác')
    ngay = re.search ('NGÀY (.+?)(.+?)', data)
    dd = int(ngay.group(1)+ngay.group(2))
    thang = re.search ('THÁNG (.+?)(.+?)', data)
    mm = int(thang.group(1)+thang.group(2)) 
    yy = today.year   
    a = 'Ngày '+str(dd)+ 'tháng '+str(mm)
    daa = str(yy)+'-'+str(mm)+'-'+str(dd)
    ngay = datetime.datetime.strptime(daa, '%Y-%m-%d') 
    wd=date.weekday(ngay)    
    days= ["THỨ HAI","THỨ BA","THỨ TƯ","THỨ NĂM","THỨ SÁU","THỨ BẢY","CHỦ NHẬT"]
    if dd < 10:
        docngay = 'ngày mùng '+ str(dd) + ' '
    else: 
        docngay = 'ngày ' + str(dd) + ' '    
    print(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 
    short_speak(a + ' là ' + days[wd] + ' ' +str(docngay) + ' tháng '+ str(mm)) 

        
if __name__ == '__main__':
    main(data)            