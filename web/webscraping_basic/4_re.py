import re

#ca?e

#caae.. cabe..cace...

p = re.compile('ca.e')

# ^ (^de): 문자열의 시작   #desk..destination..
# . (ca.e) : 하나의 문자를 의미
# & (se&) : 문자열의 끝    #base..case...


def print_match(m):
    if m:
        print("group :", m.group()) #일치하는 문자열 반환
        print("string :", m.string) #입력받은 문자열
        print("start :", m.start()) #일치하는 문자열의 시작 인덱스
        print("end :", m.end()) #일치하는 문자열의 끝 인덱스
        print("span :", m.span()) #일치하는 문자열의 시작과끝 인덱스
        
    else:
        print('매치되지 않았습니다.')

#m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인


m = p.search("lesscare") #serch : 주어진 문자열 중에 일치하는지 확인

print_match(m)

list = p.findall("good care cafe") #findall: 일치하는 모든 것을 리스트 형태로 반환

print(list)
