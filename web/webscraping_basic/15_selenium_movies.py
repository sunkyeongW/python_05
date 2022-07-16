import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies?hl=ko&gl=US"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movie = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})


#with open("movie.html", 'w', encoding="utf-8") as f:
    #f.write(soup.prettify())

for mov in movie:
    title = mov.find("div", attrs={"class":"Epkrse"}).get_text()
    print(title) #Epkrse
