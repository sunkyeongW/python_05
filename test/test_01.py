import requests

from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%86%A1%ED%8C%8C%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EC%8B%9C%EC%84%B8&oquery=%EC%86%A1%ED%8C%8C%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&tqi=hW57vwprvN8sscoWa3Rssssstfo-344225"

res =requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#정보 확인
#with open("quiz.html", "w", encoding="utf-8") as f:
    #f.write(soup.prettify())

data = soup.find("table", attrs= {"class":"list market_conditions"}).find("tbody").find_all("tr")

for index, row in enumerate(data):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(index+1))
    print("공급/전용 :", columns[0].get_text())
    print("하한 :", columns[1].get_text())
    print("상한 :", columns[2].get_text())
    print("하한 :", columns[4].get_text())
    print("상한 :", columns[5].get_text())


