# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 22:51:40 2019

@author: Dell
"""

# For New Year

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('path to chromedriver.exe')
driver.get('https://web.whatsapp.com/')

all_names = ['A', 'B', 'C', '...']
sleep(2)
input('Enter anything after scanning QR code')
 
for name in all_names:
 
    nam = name
     
    find = driver.find_element_by_xpath('//span[@data-icon="search"]')
    find.click()
        
    search = driver.find_element_by_css_selector("input[type='text']")
    search.clear()
    search.send_keys(nam)
            
    sleep(1)
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(nam))
    user.click()
            
    filepath = 'path to attachment'
            
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
            
    sleep(2)
    image_box = driver.find_element_by_xpath('//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
            
    msg = 'your message.'
    sleep(2)
    msg_box = driver.find_element_by_xpath('//div[@dir = "ltr"]') 
    msg_box.send_keys(msg)
            
    sleep(5)
            
    send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    send_button.click()
        
    sleep(4)