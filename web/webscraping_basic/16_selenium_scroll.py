from selenium import webdriver
browser = webdriver.Chrome("web\webscraping_basic\chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies?hl=ko&gl=US"

browser.get(url)

#스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)")

#맨 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time

interval = 2

prev_height = browser.execute_script("return document.body.scrillHeight")

#반복 수행
while True:
    #스크롤 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #페이지 로딩 대기
    time.sleep(interval)
    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrillHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")