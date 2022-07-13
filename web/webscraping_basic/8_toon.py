from statistics import mean
import bs4
import requests
from bs4 import BeautifulSoup
import statistics

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})

title = cartoons[0].a.get_text()

link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com" + link)


print()
print()
print()

#만화 제목 + 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)



print()
print()
print()
#평점 구하기
total_rates = 0
toon = soup.find_all("div", attrs={"class":"rating_type"})

for car in toon:
    rate = car.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 :", total_rates)
print("평균 점수 :", total_rates / len(toon))
