# 웹의 구성
1. HTML
    Hyper Text  markup Language의 약어.
    웹 페이지를 구성하는데 사용하는 언어.
2. CSS
    웹 페이지를 꾸미는 역할.
3. Javascript
    웹 페이지를 동적으로 동작하도록 하는 기술.


# 정규식 기본(Re)
    텍스트에서 특정 문자열을 검색하거나 치환할 때 사용.

    정규 표현식 종류

    ^ (^de): 문자열의 시작 
    . (ca.e) : 하나의 문자를 의미
    & (se&) : 문자열의 끝   

    컴파일(compile)된 패턴 객체의 메소드

    - 정규식 객체를 리턴해줌.
    - 하나의 정규식 패턴이 여러번 사용될 떄 효율적.

    match() : 주어진 문자열의 처음부터 일치하는지 확인
    serch() : 주어진 문자열 중에 일치하는지 확인
    findall() : 매칭되는 모든 결과를 리스트로 반환


    math 객체의 메소드

    group() : 일치하는 문자열 반환
    string() : 입력받은 문자열
    start() : 일치하는 문자열의 시작 인덱스
    end() : 일치하는 문자열의 끝 인덱스
    span() : 일치하는 문자열의 시작과끝 인덱스




# 웹 크롤링(Web Crawling)
    웹서버 내에 있는 링크를 따라가면서 대규모 데이터 세트를 처리하는 기술.
    여러 인터넷 사이트의 페이지(문서,html 등)을 수집해서 분류.

# 웹 스크래핑(Web Scraping)
    웹서버에 저장된 데이터를 검색, 추출하는 기술.
    크롤링도 일종의 스크래핑 기술.

# 웹 스크래핑 과정 
    1. 서버에 페이지를 요청(request)
    2. 서버에서 페이지를 보내줌 (response)
    3. 페이지에서 원하는 데이터를 추출(parsing(bs))

# Requests
    html 문서 정보를 가져오기 위한 라이브러리.
    동적 웹페이지 X.

        GET 방식: URL의 정보를 가져오는 방법으로 가장 많이 사용.
        POST 방식 : HTTP의 바디 부분에 담아서 Key-values 형식으로 넣어서 전송.

    
    res.raise_for_status()
    - requests를 이용할 때 필수적으로 작성해주는 코드.
    - 응답 코드 에러 시 예외처리 및 프로그램 종료.
    - 응답 코드 : 200 - 서버가 요청을 성공적으로 처리.

# selenium
    인터넷 브라우저 컨트롤러(자동화).
    반복적인 웹 업무를 수행하면서 업무 자동화를 구현.
    동적 웹페이지 O.
    크롬 버전에 맞는 chromedriver.exe가 반드시 필요.


# Beautifulsoup
    가져온 데이터에서 내가 원하는 내용만 추출.
    번거로운 작업들을 간단하게 해결 가능.
    동적 웹페이지 X.

    bs 메소드
    1. find - 조건에 맞는 첫번째 element
    2. find_all - 조건에 맞는 모든 element 리스트
    3. find_next_sibling - 다음 형제 찾기
    4. find_previous_sibling - 이전 형제 찾기
    5. ["href"] - 속성 찾기
    6. get_text()- 텍스트 찾기

    # 이미지 출력
    write() - 파일을 쓸 때 사용하는 함수.
    
    with open("파일명", "wb") as f:
        f.write(res.content)

    enumerate
    반복문을 사용할 때 몇 번째 반복문인지 알 수 있는 인덱스를 부여.


# User-Agent
    HTTP 요청을 보낸 디바이스와 사용자 소프트웨어의 식별 정보.
    HTTP 요청 에러가 발생했을 때 요청을 보낸 사용자 환경을 알아보기 위해 사용.


# Headless Chrome
    브라우저를 띄우지 않고 동작
    때로는 user-agent 정의 필요