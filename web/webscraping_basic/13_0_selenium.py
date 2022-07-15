import imp
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

browser.get("http://naver.com")

from selenium.webdriver.common.by import By


elem = browser.find_element(By.CLASS_NAME, "link_login") 

elem.click()
browser.back()
browser.forward()

elem = browser.find_element(By.ID, "query") 
from selenium.webdriver.common.keys import Keys

elem.send_keys("원선경")
elem.send_keys(Keys.ENTER)  

elem = browser.find_elements(By.TAG_NAME, "a")

for e in elem:            
    e.get_attribute("href")


browser.get("http://daum.net")

elem = browser.find_element(By.NAME, "q")

elem.send_keys("안녕")
elem.send_keys(Keys.ENTER)

elem = browser.find_element(By.XPATH, "//*[@id='daumBtnSearch']")
elem.click()