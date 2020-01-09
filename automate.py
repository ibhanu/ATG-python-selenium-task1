import time
import os
from datetime import datetime
import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By


logging.basicConfig(filename='myapp.log', level=logging.INFO)

logging.info('Automation Started at %s'%datetime.now())

driver = webdriver.Chrome('/home/bhanu/ChromeDriver/chromedriver')  # Optional argument, if not specified will search path.
starttime = time.time()

driver.get('http://www.atg.party/')

responsetime = time.time() - starttime

r = requests.get('http://www.atg.party/')

if r.status_code == 200:
	print("Status Code is OK:200")
else:
	print("Status code :"+r.status_code)

logging.info('Response Time %s seconds'%responsetime)
print("Response Time %s seconds"%responsetime)

login_button = driver.find_elements_by_xpath("//*[@data-toggle='tab' and @href='#login']")[0]
login_button.click()
time.sleep(0.5)

email = driver.find_element(By.ID, "email")
email.send_keys('wiz_saurabh@rediffmail.com')
time.sleep(0.5)

password  = driver.find_element(By.ID, "password")
password.send_keys('Pass@123')
time.sleep(0.5)

go_button = driver.find_elements_by_xpath("//form[@id='frm_landing_page_user_login' and @name='frm_landing_page_user_login']/div[3]/button[1]")[0]
go_button.click()
time.sleep(2)

driver.get('http://www.atg.party/article')
time.sleep(0.5)

title = driver.find_elements_by_xpath("//input[@id='title']")[0]
title.send_keys('Random')

desc = driver.find_elements_by_xpath("//div[@class='fr-element fr-view']")[0]
desc.send_keys('Random')

pic = driver.find_element_by_id("article_pic")
pic.send_keys(os.getcwd()+'/image.png')
time.sleep(0.5)

publish = driver.find_elements_by_xpath("//div[@id='postsavefeature']/button[2]")[0]
publish.click()
time.sleep(2)

print(driver.current_url)

logging.info('current url is %s'%driver.current_url)
logging.info('Automation Ended at %s'%datetime.now())

time.sleep(1)
driver.quit()
