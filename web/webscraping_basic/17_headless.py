from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")


browser = webdriver.Chrome("web\webscraping_basic\chromedriver.exe", options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies?hl=ko&gl=US"

browser.get(url)

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
browser.get_screenshot_as_file("google_movie.png")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":["ULeU3b neq64b", "VfPpkd-BFbNVe-bF1uUb NZp2ef"]})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":["Epkrse","MPNOXb"]}).get_text()
    print(title)

    #할인 전 가격

    origin_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})

    if origin_price:
        origin_price = origin_price.get_text()
    else:
        #print(title, "<할인되지 않은 영화 제외>")
        continue


    #할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

    #링크
    link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    #올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {origin_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" *80)

browser.quit()

