# 웹스크래핑
웹페이지에서 원하는 부분만 가져오는 것

# 웹크롤링
웹페이지 내에 있는 링크를 따라가면서 모든 내용을 가져오는 것

# web의 구성
1. html(뼈대)
2. css(인테리어)
3. js(생동감)

# html 정의
 xpath : XML 문서의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어

# chrome

# requests
html 문서 정보를 가져오기 위한 방법

코드가 200이면 정상

# 정규식 기본

^ (^de): 문자열의 시작   #desk..destination..
. (ca.e) : 하나의 문자를 의미
& (se&) : 문자열의 끝    #base..case...

match : 주어진 문자열의 처음부터 일치하는지 확인
serch : 주어진 문자열 중에 일치하는지 확인

group : 일치하는 문자열 반환
string : 입력받은 문자열
start : 일치하는 문자열의 시작 인덱스
end : 일치하는 문자열의 끝 인덱스
span : 일치하는 문자열의 시작과끝 인덱스

findall: 일치하는 모든 것을 리스트 형태로 반환

# http method
1.get:url로 보내는 방법
2.post: http의 바디 부분에 담아서 서버로 보내는 방법

# user-agent
서버에서 권한을 받기위해 받는 자기만의 출입증같은 존재


# requests
주어진 url을 통해 받아온 html 읽어 오기
res.raise_for_status() 
동적 웹페이지 x

# selenium
인터넷 브라우저 컨트롤러(자동화)
동적 웹페이지
크롬 버전에 맞는 chromedriver.exe가 반드시 필요

# beautifulsoup

find - 조건에 맞는 첫번째 element
find_all - 조건에 맞는 모든 element 리스트
find_next_sibling - 다음 형제 찾기
find_previous_sibling - 이전 형제 찾기

soup["href"] - 속성
soup.get_text()- 텍스트

# 이미지 다운로드
with open("파일명", "wb") as f:
    f.write(res.content)

# csv 파일로 저장
import csv

f= open(filename, "w', encoding = "urf-8", newline="")

# headless chrome
브라우저를 띄우지 않고 동작
때로는 user-agent 정의 필요