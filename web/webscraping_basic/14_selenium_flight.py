from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver.exe")

browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"
browser.get(url) #url로 이동

#가는날 선택
browser.find_element(By.XPATH, '//button[text()="가는 날"]').click()

#이번달 27,28 선택
browser.find_elements(By.XPATH, '//b[int()= 27]')[0].click



#browser.find_element(By.XPATH, '//button[text()="오는 날"]').click()

#browser.find_elements(By.LINK_TEXT, "28")[0].click()