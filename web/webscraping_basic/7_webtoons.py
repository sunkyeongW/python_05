import bs4
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#모든 정보 출력
cartoons = soup.find_all("a", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.get_text()) #class 속성이 title인 모든 'a' element 반환

print()



