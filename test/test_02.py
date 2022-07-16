from attr import attr
import requests
from bs4 import BeautifulSoup
import soupsieve
import re


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {}".format(link))



def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8&oquery=%EC%86%A1%ED%8C%8C%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EC%8B%9C%EC%84%B8&tqi=hW57jlprvh8ssestvI8ssssstx8-012541"
    soup = create_soup(url)
    #어제보다 00높아요
    cast = soup.find("p", attrs= {"class":"summary"}).get_text()
    #현재 00'C (최저 00'C / 최고 00'C)
    curr_temp = soup.find("div", attrs= {"class":"temperature_text"}).get_text().replace("도시","")
    min_temp = soup.find("span", attrs= {"class":"lowest"}).get_text()
    max_temp = soup.find("span", attrs= {"class":"highest"}).get_text()
    #강수 확률
    weather_morning = soup.find("span", attrs= {"class":"rainfall"}).get_text()
    weather_afternoon = soup.find("span", attrs= {"class":"rainfall"}).get_text()

    #체감,습도,바람
    dust = soup.find("dl", attrs= {"class":"summary_list"})
    pm1 = dust.find_all("dd")[0].get_text() #체감
    pm2 = dust.find_all("dd")[1].get_text() #습도
    pm3 = dust.find_all("dd")[2].get_text() #바람


    #출력
    print(cast)
    print(curr_temp,"({} / {})".format(min_temp, max_temp))
    print()
    print("체감 {}".format(pm1))
    print("습도 {}".format(pm2))
    print("바람 {}".format(pm3))
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/newspaper/home"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"offc_lst _headline_list"}).find_all("li", limit=3)

    for index, news in enumerate(news_list):
        title = news.find("strong", attrs={"class":"title"}).get_text().strip()
        link = url + news.find("a")["href"]

        print_news(index, title, link)
    print()


def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url) 
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    
    for index, it in enumerate(news_list):
        a_idx = 0
        img = it.find("img")
        if img:
            a_idx = 1  #img 태그가 있으면 1번째 a 태그의 정보를 사용


        a_tag = it.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]

        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("영어 지문")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())


    print()
    print("한글 지문")
    for sentence in sentences[0:len(sentences)//2]:
        print(sentence.get_text().strip())

    print()




if __name__ == "__main__":
    scrape_weather() #오늘의 날씨 정보 가져오기
    scrape_headline_news()
    scrape_it_news()
    scrape_english()
