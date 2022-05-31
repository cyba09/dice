from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import requests
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
import csv
import const
import aa,bb,cc,dd,ee,ff

idx = const.IDX

def getList():
    p = 1
    nw = datetime.now()
    d = nw.strftime('%Y-%m-%d')
    url3 = 'https://betgames9.betgames.tv/s/web/v1/game/results/testpartner?game_id=10&page={page}&date={date}&timezone=1'
    try:

       data = requests.get(url3.format(date=d, page=p)).json()
       lst = data['runs'][0]['results']
       gst = [round((data['runs'][0]['time'])/1000)]
       for i in data['runs'][0]['results']:
           gst.append(i['number'])
    except requests.ConnectionError:
        lst = 2
    return gst

  
########################################################################################
options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')

dv = webdriver.Chrome(service=s, options=options)
url='https://www.vegasbets.co.za/partner/bet-games'
dv.get(url)
time.sleep(21)
dv.switch_to.frame(dv.find_element(By.TAG_NAME,'iframe')) 
a = b = c = d = e = f = 0

while True:
    try:
        elem_time = WebDriverWait(dv, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.px2BltBZ9d0JArpfjthg:nth-child(11) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")))
        try:
         if elem_time.text == '00:26' :
            ls = getList()
            if len(ls) < 2:
                continue
            red = ls[1]
            blue = ls[2]
            if red%2 != 0:
                a = 0
                b += 1
            else:
                a += 1 
                b = 0
            if blue%2 != 0:
                c = 0
                d += 1
            else:
                c += 1 
                d = 0
            sum = red + blue
            if sum%2 != 0:
                e = 0
                f += 1
            else:
                e += 1
                f = 0
            if a == idx:
                a = b = c = d = e = f = 0
                aa.placebet()
            if b == idx:
                a = b = c = d = e = f = 0
                bb.placebet()
            if c == idx:
                a = b = c = d = e = f = 0
                cc.placebet()
            if d == idx:
                a = b = c = d = e = f = 0
                dd.placebet()
            if e == idx:
                a = b = c = d = e = f = 0
                ee.placebet()
            if f == idx:
                a = b = c = d = e = f = 0
                ff.placebet()
        except exceptions.StaleElementReferenceException as e:
            pass
    except NameError:
        pass
        
    time.sleep(1)


