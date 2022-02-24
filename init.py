from operator import index
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.action_chains import ActionChains
from pandas.core.frame import DataFrame



import time
import pandas as pd
import requests

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

# ------ 設定要前往的網址 ------
url = 'https://flipclass.stust.edu.tw/index/login'  

# ------ 登入的帳號與密碼 ------
username = '' 
password = ''


# ------ 透過Browser Driver 開啟 Chrome ------
driver = webdriver.Chrome()        

# ------ 前往該網址 ------
driver.get(url)        

# ------ 賬號密碼 ------
# time.sleep(1)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account"]')))
#elem = driver.find_element_by_id("email")
elem = driver.find_element_by_name("account")
elem.send_keys(username)

#elem = driver.find_element_by_id("pass")
elem = driver.find_element_by_name("password")
elem.send_keys(password)        

elem.send_keys(Keys.RETURN)
time.sleep(5)




# 切換頁面
spec_url = 'https://flipclass.stust.edu.tw/dashboard'
driver.get(spec_url)
# //*[@id="xbox2-inline"]/div[1]/div[1]/div[1]/div/ul/li[1]/div[3]/div/div[2]/a/span[2]

# homeworks = driver.find_element(By.CLASS_NAME,'fs-list ')
infos = driver.find_elements_by_css_selector('div .fs-list ')
# //*[@id="xbox2-inline"]/div[1]/div[1]/div[1]/div
# print(homeworks)


parts = ['最近事件','最新公告','最新討論','最新教材']




def get_part_info (info_index,part_name):
    hw_infos = infos[info_index].find_elements_by_class_name('text-overflow')
    if hw_infos:
        print(f'\n\n-----------{part_name}-----------------')

        for hw_num, homework in enumerate(hw_infos):
            topic = homework.find_element_by_tag_name('a ')
            hw_title = homework.find_element_by_class_name('text ').text
            link = topic.get_attribute('href')   
            title = topic.get_attribute('title')                
                                 
            # print(topic.get_attribute('title'))
            print('---------------------------------------------------------------------')
            # print(f'index = {hw_num}')
            # print(hw_title.text)
            print(f'{title} \n課程連結: {link} \n標題: {hw_title}')


for i,part in enumerate(parts):
    get_part_info(i,part)
