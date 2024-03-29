import requests

res = requests.get("http://naver.com")

res1 = requests.get("https://google.com")
res.raise_for_status()  #문제가 있을 시 에러를 내고 중단시킴.
print('웹 스크래핑을 진행합니다.')


print('응답코드 :', res.status_code) #200이면 정상
print('응답코드 :', res1.status_code) #200이면 정상

if res.status_code == requests.codes.ok:
    print('정상입니다')
else:
    print('문제가 생겼습니다. [에러코드 ' , res.status_code, "]")

print(len(res1.text))
print(res1.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res1.text)
