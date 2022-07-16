import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) #soup에서 처음 발견되는 a element 출력
print(soup.a.attrs)  #a element의 속성 정보 출력
print(soup.a["href"]) #a element의 href 속성 '값' 정보 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"})) #class:Nbtn_upload 인 a element를 찾아라

print()
print()
print()
#print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())

#print(rank1.next_sibling)
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling 

print(rank2.a.get_text())
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

#부모/하위
print(rank1.parent)

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

print()
print()
print()

#해당 정보 한번에 가져오기
rank1.find_next_siblings("li")

webtoon = soup.find("a", text ="화산귀환-68화")

print(webtoon)
