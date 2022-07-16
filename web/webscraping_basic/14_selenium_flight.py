import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("web\webscraping_basic\chromedriver.exe")

browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"
browser.get(url) #url로 이동

#가는날 선택
browser.find_element(By.XPATH, '//*[text()="가는 날"]').click()

time.sleep(1)

#이번달 28,다음달 13 선택
browser.find_elements(By.XPATH, "//*[text()='28']")[0].click()
time.sleep(1)
browser.find_elements(By.XPATH, "//*[text()='13']")[1].click()

time.sleep(1)
#출발 여행지 선택
browser.find_element(By.XPATH, '//*[text()="인천"]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[text()="국내"]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[text()="김포"]').click()

#도착 여행지 선택
browser.find_element(By.XPATH, '//*[text()="도착"]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[text()="국내"]').click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[text()="제주"]').click()

#항공권 검색
browser.find_element(By.XPATH, '//*[text()="항공권 검색"]').click()

#첫번째 결과 출력
#1. time.sleep(5)

try:
    elem = WebDriverWait(browser, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]')))
    print(elem[0].text)
finally:
    browser.quit()
    
#first = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')

#print(first.text)