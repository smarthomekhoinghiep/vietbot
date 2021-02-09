import os
import yaml
import gih
import chsv    
from speaking import short_speak
from termcolor import colored
import datetime
import json
import requests
import threading
import gih
import sys
import time
# from pydub import AudioSegment                
# from pydub.playback import play
from pygame import mixer
#STT Engine
import stt_gg_cloud
import stt_gg_free
import stt_fpt
import stt_viettel
stt_engine= gih.get_config('stt_engine')
ggcre = gih.get_config('google_application_credentials')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ggcre
domain = gih.get_config('hass_url')
longlivedtoken = gih.get_config('hass_token')
voice = gih.get_config('voice')
volume=gih.get_config('volume')
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
def find_hass_friendly_name(data):
    print('[BOT] -TÌM TÊN THIẾT BỊ')
    print('')
    friendly_name = chsv.check_fr(data)
    ex,ey = chsv.export_e_d(friendly_name)
    domain_ex = ex
    entity_id_ex = ey
    m = 0
    object = [define(domain_ex,entity_id_ex,domain,longlivedtoken) for x in range(len(domain_ex))]
    while m < len(domain_ex): 
        object[m] = define(domain_ex[m],entity_id_ex[m],domain,longlivedtoken)
        object[m] = object[m].define()
        m += 1
    if len(object)==0:                     
        short_speak('Không tìm thấy thiết bị trong trung tâm điều khiển nhà')        
        short_speak("Vui lòng nói lại tên thiết bị")
        play_ding()
        more_data=getText()
        print('[BOT] -TÌM LẠI TÊN THIẾT BỊ')
        print('')
        friendly_name = chsv.check_fr(data)
        ex,ey = chsv.export_e_d(friendly_name)
        domain_ex = ex
        entity_id_ex = ey
        n = 0
        object = [define(domain_ex,entity_id_ex,domain,longlivedtoken) for x in range(len(domain_ex))]
        while n < len(domain_ex): 
            object[n] = define(domain_ex[n],entity_id_ex[n],domain,longlivedtoken)
            object[n] = object[n].define()
            n += 1
            
    return object
   
def on_off(data,action):
    friendly_name_hass = find_hass_friendly_name(data)
    p = 0
    while p < len(friendly_name_hass): 
        try:
            if action =='on':
                friendly_name_hass[p].turn_on()
            elif action =='off':    
                friendly_name_hass[p].turn_off()                
            # print(colored(str(friendly_name_hass[p])+ ': Tắt/Ngắt','green'))
            p +=1        
        except:
            short_speak('không nhận được phản hồi từ thiết bị')
            break

def on_off_all_1(device,name,action):

    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    payload = {'entity_id': 'all'}        
    if action == 'on':
        url = domain+'/api/services/'+device+'/turn_on'
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Bật tất cả '+name+' thành công')
                short_speak('Bật tất cả '+name+' thành công')
            else:
                print('[BOT]: Bật tất cả '+name+' không thành công')
                short_speak('Bật tất cả '+name+' không thành công')                                            
        except:
            short_speak('có lỗi phản hồi của thiết bị '+  name )
    elif action =='off':
        url = domain+'/api/services/'+device+'/turn_off'
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Tắt tất cả '+name+' thành công')
                short_speak('Tắt tất cả '+name+' thành công')
            else:
                print('[BOT]: Tắt tất cả '+name+' không thành công')
                short_speak('Tắt tất cả '+name+' không thành công')                                            
        except:
            short_speak('có lỗi phản hồi của thiết bị '+  name )

def on_off_all_2(name,action):
    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    payload = {'entity_id': 'all'}        
    if action == 'on':
        url = domain+'/api/services/cover/open_cover'        
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Mở tất cả '+name+' thành công')
                short_speak('Mở tất cả '+name+' thành công')
            else:
                print('[BOT]: Mở tất cả '+name+' không thành công')
                short_speak('Mở tất cả '+name+' không thành công')                                            
        except:
            short_speak('có lỗi phản hồi của thiết bị '+  name )
    elif action =='off':
        url = domain+'/api/services/cover/close_cover'        
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đóng tất cả '+name+' thành công')
                short_speak('Đóng tất cả '+name+' thành công')
            else:
                print('[BOT]: Đóng tất cả '+name+' không thành công')
                short_speak('Đóng tất cả '+name+' không thành công')                                            
        except:
            short_speak('có lỗi phản hồi của thiết bị '+  name )                

def trangthai(data):
    print('')
    friendly_name = chsv.check_fr(data)
    ex,ey = chsv.export_e_d(friendly_name)
    domain_ex= ex
    entity_id_ex= ey
    i=0
    object = [0 for x in range(len(domain_ex))]
    while i < len(domain_ex):
        object[i] = [friendly_name[i],domain_ex[i],entity_id_ex[i],domain,longlivedtoken]
        i+=1
    # print(str(object))        
    k=0
    while k < len(object):        
        doma =  object[k][1]
        print(doma)
        enti =  object[k][2]
        print(enti)
        t,tt = check_state(doma,enti)
        short_speak(object[k][0]+ ' đang '+ t)
        k+=1  

def thietlap(friendly_name_hass,sta,data):
    q = 0
    try:
        r=friendly_name_hass[0].domain_extract()
        doma = sta[0][1]
        enti = sta[0][2]
        t,tt = check_state(doma,enti)
        tt = tt['attributes']['options']
    except:
        pass
    
    while q < len(friendly_name_hass):
        r=friendly_name_hass[q].domain_extract()
        if str(r)== 'input_select':
            for x in range(len(tt)):
                if tt[x].upper() in data.upper():
                    try:
                        res=friendly_name_hass[q].set_option(tt[x])
                        if res == 1:
                            short_speak(' thiết lập thành công ')
                            break
                    except:
                        pass
        q+=1
    
    if 'NHIỆT ĐỘ' in data.upper():
        
        qq=0
        data = data.split()
        x=0
        while x < len(data):
            if data[x].isnumeric() ==True and int(data[x])<32 and int(data[x])>15:
                degree = int(data[x])
                
                break
            x+=1

        while qq < len(friendly_name_hass):
            rep=friendly_name_hass[qq].domain_extract()
            
            if str(rep)== 'climate':
                
                res=friendly_name_hass[qq].set_temperature(degree)
                if res ==1:
                    short_speak('Thiết lập máy lạnh sang '+ str(degree)+ ' độ')
                    break
            qq+=1

def hen_gio(data):
    global t1
    from threading import Timer
    
    
    from time import ctime, strftime
    def check_time_in(xi_tin):
        split_lan1 = xi_tin.split()
        
        for m in range(0,len(split_lan1)):
            
            if ":" in split_lan1[m]:
                split_lan2 = split_lan1[m].split(":")
                
                break
            else:
                split_lan2=[]
        return split_lan2

    def more_info_friendly(data,friendly_name):
        continuego=1
        if friendly_name== []:
            qa = 0
            while qa<3:
                qa+=1
                short_speak('tác vụ cần làm là gì')
                more_data=getText()
                if 'HỦY' in more_data.upper():
                    short_speak('thoát chế độ hẹn giờ')
                    continuego=0
                    break
                else:
                    friendly_name = find_hass_friendly_name(more_data)
                    if friendly_name ==[]:
                        pass
                    else:
                        data=more_data
                        break
        return data, friendly_name, continuego                
    def more_info_time(data,time_in_data):
        continue_go =1
        time_in_data=check_time_in(data)
        if time_in_data ==[]:
            qb = 0
            while qb<3:
                qb+=1
                short_speak('cung cấp thời điểm thực hiện')
                more_data1=getText()
                if 'HỦY' in more_data1.upper():
                    short_speak('thoát khỏi chế độ hẹn giờ')
                    continue_go = 0                                
                    break

                else:
                    time_in_data=check_time_in(more_data1)
                    if time_in_data ==[]:
                        pass
                    else:
                        break

        return time_in_data, continue_go
    friendly_name = find_hass_friendly_name(data)
    print(friendly_name)
    time_in_data=check_time_in(data)
    print(time_in_data)
    continue_go=1
    if friendly_name == []:
        abc = more_info_friendly(data,friendly_name)
        friendly_name =abc[1]
        data = abc[0]
        continue_go=abc[2]
        
    if continue_go ==1:
        if time_in_data == []:
            abcd = more_info_time(data,time_in_data)
            time_in_data = abcd[0]
            continue_go=abcd[1]
    if continue_go == 1:
        time_set = datetime.timedelta(hours=int(time_in_data[0]), minutes = int(time_in_data[1]),seconds=00)
        print(time_set)
        time_now_hour =strftime("%H")
        time_now_minute =strftime("%M")
        time_now_second =strftime("%S")
        time_now=datetime.timedelta(hours=int(time_now_hour), minutes = int(time_now_minute),seconds = int(time_now_second))
        
        second_delta = time_set-time_now
        
        secondelta=str(second_delta).split(":")
        
        second_delta_final = int(secondelta[0])*3600+int(secondelta[1])*60+int(secondelta[2])
        
    
    if len(friendly_name) !=0 and int(second_delta_final) >1:
        seconds=int(second_delta_final)
        print('[BOT]: OK')
        short_speak('đã đặt hẹn giờ' )
        if 'HẸN GIỜ' in data:
            data=data.replace("HẸN GIỜ","")
            
        t1 = Timer(seconds,has_xuly,[data])
        t1.start()
    else:
        short_speak('xin thử lại sau')

class sensor():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def domain_extract(self):
        rr='sensor'
        return rr

class binary_sensor():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def domain_extract(self):
        rr='binary_sensor'
        return rr

class climate():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def domain_extract(self):
        rr='climate'
        return rr
    def set_temperature(self,degree):
        url = self.domain+'/api/services/climate/set_temperature'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'climate.'+self.entity_id_ex, 'temperature':degree}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã thiết lập nhiệt độ thành công')
                r=1
                return r
        except:
            r = 0
            return r

class switch():

    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def turn_on(self):
        url = self.domain+'/api/services/switch/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}            
        payload = {'entity_id': 'switch.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã bật/mở switch thành công')
                r=1
                return r
        except:
            r = 0
            return r
    def turn_off(self):
        url = self.domain+'/api/services/switch/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'switch.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã tắt/ngắt switch thành công')
                r=1
                return r
        except:
            r = 0
            return r
    def domain_extract(self):
        rr='switch'
        return rr

class input_select():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def set_option(self,option):
        url = self.domain+'/api/services/input_select/select_option'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}           
        payload = {'entity_id': 'input_select.'+self.entity_id_ex, 'option':option}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã nhập thành công')
                r=1
                return r
        except:
            r = 0
            return r
    def domain_extract(self):
        rr='input_select'
        return rr

class media_player():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/media_player/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã bật/mở đài phát thành công')
                r=1
                return r
        except:
            r = 0
            return r
    def turn_off(self):
        url = self.domain+'/api/services/media_player/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã tắt/ngắt thành công')
                r=1
                return r
        except:
            r = 0
            return r
    def media_play(self):
        url = self.domain+'/api/services/media_player/media_play'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}            
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã Play thành công')
                r=1
                return r
        except:
            r = 0
            return r
    def media_pause(self):
        url = self.domain+'/api/services/media_player/media_pause'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}           
        payload = {'entity_id': 'media_player.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã Pause thành công')
                r=1
                return r
        except:
            r = 0
            print(r)
            return r

    def domain_extract(self):
        rr='media_player'
        return rr

class script():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/script/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'script.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Chạy kịch bản thành công')
                short_speak('Đã thực hiện thành công')                
                r=1
                return r
            else:
                print('[BOT]: Chạy kịch bản không thành công')
                short_speak('Đã thực hiện thành công')                                
        except:
            r = 0
            return r

    def domain_extract(self):
        rr='script'
        return rr

class scene():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/scene/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'scene.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã bật/mở ngữ cảnh thành công')
                r=1
                return r
        except:
            r = 0
            return r

    def domain_extract(self):
        rr='scene'
        return rr

class automation():
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        url = self.domain+'/api/services/automation/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken, 'content-type': 'application/json',}
        payload = {'entity_id': 'automation.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã bật/mở tự động hóa thành công')
                r=1
                return r
        except:
            r = 0
            return r

    def domain_extract(self):
        rr='automation'
        return rr

class light():

    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
        
    def turn_on(self):
        url = self.domain+'/api/services/light/turn_on'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Bật đèn thành công')
                short_speak('Bật đèn thành công')                
                r=1
                return r
            else:
                print('[BOT]: Bật đèn không thành công')
                short_speak('Bật đèn không thành công')                                
            
        except:
            r = 0
            return r

            
    def turn_off(self):
        url = self.domain+'/api/services/light/turn_off'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}        
        payload = {'entity_id': 'light.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print ('[BOT]: Tắt đèn thành công')
                short_speak('Tắt đèn thành công')
                r=1
                return r
            else:
                print('[BOT]: Tắt đèn không thành công')
                short_speak('Tắt đèn không thành công')                                                
        except:
            r = 0
            return r
            
    def domain_extract(self):
        rr='light'
        return rr

class cover():
    # Implement one of these methods.
    def __init__(self,entity_id_ex=[],domain='',longlivedtoken=''):
        self.entity_id_ex = entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def turn_on(self):
        """Open the cover."""
        url = self.domain+'/api/services/cover/open_cover'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'cover.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã mở rèm thành công')
                short_speak('Đã mở rèm thành công')                
                r=1
                return r
            else:
                print('[BOT]: Mở rèm không thành công')
                short_speak('Mở rèm không thành công')                                
            
        except:
            r = 0
            return r                

    def turn_off(self):
        """Close the cover."""        
        url = self.domain+'/api/services/cover/close_cover'
        headers = {'Authorization': 'Bearer '+ self.longlivedtoken,'content-type': 'application/json',}
        payload = {'entity_id': 'cover.'+self.entity_id_ex}
        try:
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            print('')
            if str(r)=='<Response [200]>':
                print('[BOT]: Đã đóng rèm thành công')
                short_speak('Đã đóng rèm thành công')                
                r=1
                return r
            else:
                print('[BOT]: Đóng rèm không thành công')
                short_speak('Đóng rèm không thành công')                                
            
        except:
            r = 0
            return r                

    def domain_extract(self):
        rr='cover'
        return rr        
        
class define():
    def __init__(self,domain_ex=[], entity_id_ex=[],domain='',longlivedtoken=''):
        self.domain_ex = domain_ex
        self.entity_id_ex= entity_id_ex
        self.domain = domain
        self.longlivedtoken = longlivedtoken
    def define(self):
        if self.domain_ex == 'switch':
            self.object = switch(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'automation':
            self.object = automation(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'device_tracker':
            self.object = device_tracker(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'alarm_control_panel':
            self.object = alarm_control_panel(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex =='script':
            self.object = script(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex =='scene':
            self.object = scene(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'light':
            self.object = light(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'sensor':
            self.object = sensor(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'binary_sensor':
            self.object = binary_sensor(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'media_player':
            self.object = media_player(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'input_select':
            self.object = input_select(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'climate':
            self.object = climate(self.entity_id_ex,self.domain,self.longlivedtoken)
        if self.domain_ex == 'cover':
            self.object = cover(self.entity_id_ex,self.domain,self.longlivedtoken)            
        return self.object

def check_state(domain_ex=[],entity_id_ex=[]):
    url = domain + '/api/states/'+ domain_ex+ '.'+ entity_id_ex
    headers = {'Authorization': 'Bearer '+ longlivedtoken,'content-type': 'application/json',}
    r = requests.get(url, headers=headers)
    # print(str(r))
    r = r.json()
    qq=r
    r = r['state']
    if r == 'off':
        r = 'tắt hoặc đóng'
    elif r == 'on':
        r= 'bật hoặc mở'
    else:
        pass
    return r,qq
    
def play_ding():
    mixer.music.load('resources/ding.wav')
    mixer.music.set_volume(volume)                
    mixer.music.play()    
    # sound = AudioSegment.from_mp3('resources/ding.wav')
    # play(sound)                                
def play_dong():
    mixer.music.load('resources/dong.wav')
    mixer.music.set_volume(volume)                
    mixer.music.play()    
    # sound = AudioSegment.from_mp3('resources/dong.wav')
    # play(sound)         