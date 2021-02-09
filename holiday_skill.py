from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import lun
from lun import S2L
from lun import L2S
import random
import gih
from speaking import short_speak
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
request_holiday= gih.get_request('request_holiday')           
request_holiday_name= gih.get_request('request_holiday_name')           
response_holiday= gih.get_response('response_holiday')           
response_choose_lose=gih.get_response('response_choose_lose')
response_say_nothing=gih.get_response('response_say_nothing')
def main(data):
    print('[BOT]: XỬ LÝ CÂU LỆNH HỎI NGÀY LỄ: '+data)   
    data = data.upper()    
    if any(item in data for item in request_holiday_name):        
        holiday_name = str([s for s in request_holiday_name if s in data])
        holiday_name = holiday_name.replace("['", "")
        holiday_name = lottery_area.replace("']", "") 
        holiday_process(holiday_name)
       
    else:       
        short_speak(random.choice(response_holiday))     
        more_data=getText()    
        if more_data is not None:
            more_data=more_data.upper()            
            if any(item in more_data for item in request_holiday_name):        
                holiday_name = str([s for s in request_holiday_name if s in more_data])
                holiday_name = holiday_name.replace("['", "")
                holiday_name = lottery_area.replace("']", "") 
                holiday_process(holiday_name)
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
def xuly(data):
    ngay = datetime.datetime.today()
    dd = ngay.day
    mm = ngay.month
    yy = ngay.year
    lunar = S2L(dd,mm,yy)
    nam_am = int(lunar[2])
    thang_am  = int(lunar[1])
    nam_nhuan = int(lunar[3])   
    if request_holiday[0] in data or request_holiday[1] in data or request_holiday[2] in data:
        xx = yy + 1
        ev = datetime.datetime(xx,1,1)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = 'Tết Tây '        
    elif request_holiday[3] in data or request_holiday[4] in data:
        nam_a = nam_am + 1
        a2d = L2S(28,12,yy,nam_nhuan) #Đổi sag nggayf dương 28/12
        nd = a2d[0]
        td = a2d[1]
        nmd = a2d[2]
        daa = str(nd)+'-'+str(td)+'-'+str(nmd) #Đổi sag ddihj dạng ngày
        a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
        a2d = a2dnew + timedelta(3)         
        nnm = a2d.day
        tnm = a2d.month
        nnm = a2d.year
        nammoi = S2L(nnm,tnm,nnm)
        nam_nhuan = int(str(nammoi[3]))
        ev = L2S(1,1,nam_a,nam_nhuan)
        n = str(ev[0])
        t = str(ev[1])
        nm = str(ev[2])
        daa = str(n)+'-'+str(t)+'-'+str(nm)
        a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
        d = a2d - ngay
        a = 'Tết Ta '               
    elif request_holiday[5] in data or request_holiday[6] in data :
        ev = L2S(10,3,nam_am,nam_nhuan)
        n = str(ev[0])
        t = str(ev[1])
        nm = str(ev[2])
        daa = str(n)+'-'+str(t)+'-'+str(nm)
        a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
        d = a2d - ngay
        a = 'Giỗ tổ Hùng Vương'        
    elif request_holiday[7] in data:
        ev = datetime.datetime(yy,4,30)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = '30/4'
    elif request_holiday[8] in data or request_holiday[9] in data :
        ev = datetime.datetime(yy,1,5)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = '1/5'        
    elif request_holiday[10] in data or request_holiday[11] or request_holiday[12] in data :
        ev = datetime.datetime(yy,9,2)
        n = str(ev.day)
        t = str(ev.month)
        nm = str(ev.year)
        d = ev - ngay
        a = '2/9'
    elif request_holiday[13] or request_holiday[14] in data :
        ev = L2S(15,8,nam_am,nam_nhuan)
        n = str(ev[0])
        t = str(ev[1])
        nm = str(ev[2])
        daa = str(n)+'-'+str(t)+'-'+str(nm)
        a2d = datetime.datetime.strptime(daa, '%d-%m-%Y')
        d = a2d - ngay
        a = 'Trung thu'    
    return [a, d]
def holiday_process(data):
    xuly(data)
    a = xuly(data)[0]
    d = xuly(data)[1]       
    dayleft = d.days
    short_speak('Còn '+str(dayleft)+' ngày nữa là đến ngày ' +a)
    if int(dayleft) < 7 :
        short_speak(random.choice(gih.get_response('response_day_within_week'))+ ' ngày ' +a +' '+random.choice(gih.get_response('response_finish_sentense')))
    elif int(dayleft) < 30:  
        short_speak(random.choice(gih.get_response('response_day_within_month'))+ ' ngày ' +a +' '+random.choice(gih.get_response('response_finish_sentense')))
    else: 
        short_speak(random.choice(gih.get_response('response_day_over'))+ ' ngày ' +a +' '+random.choice(gih.get_response('response_finish_sentense')))
    
if __name__ == '__main__':
    main(data)    