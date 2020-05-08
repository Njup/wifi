import pywifi
from pywifi import const
import time
'''
profile = pywifi.Profile()                                  #创建配置文件
profile.ssid = 'ChinaNet-wcl'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '3836729wcl'
'''
wifi = pywifi.PyWiFi()                                      #创建wifi对象，并应用配置
iface = wifi.interfaces()[0]                                #创建接口
#profile = iface.add_network_profile(profile)
#iface.connect(profile)

iface.scan()                                                #扫描wifi，将结果保存到result列表中，再通过for循环逐个打印。注意打印的数据类型，ssid、signal等
time.sleep(8)
result= iface.scan_results()                                #scan_results()扫描结果，返回一个包含profile对象的列表，一般在scan()后2-8秒执行（官方文档）

for name in result:
    print(name.signal,name.ssid.encode('raw_unicode_escape').decode('utf-8'))

for mingzi in result:
    #print(mingzi.signal,mingzi.ssid.encode('raw_unicode_escape').decode('utf-8'))
    profile = pywifi.Profile()                                  #创建配置文件
    profile.ssid=mingzi.ssid.encode('raw_unicode_escape').decode('utf-8')
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = '12345678'
    #.encode('raw_unicode_escape').decode('utf-8')修复中文乱码
    profile = iface.add_network_profile(profile)
    iface.connect(profile)
    time.sleep(8)
    flag=False
    for i in range(5):
        x=iface.status()
        if x==4:
            flag=True
            print('已连接')
            print(mingzi.ssid.encode('raw_unicode_escape').decode('utf-8'))
            break
        if x==1:
            print('连接中')
            time.sleep(3)
    
    if flag == True:
        break
    print('切换至下一个热点')
z=input()