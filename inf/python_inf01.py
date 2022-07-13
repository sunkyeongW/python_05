#"파이썬 게임 만들기"
print('---' * 7)
print('파이썬 게임 만들기')

import time

name = input('What is your name? :')

print('hi,' +name, "Time to play hangman game!")

time.sleep(1)

print('Start Loding...')

time.sleep(0.5)

#정답 단어
word = 'strawberry'

#추측 단어
guesses = ''

#기회
turns = 3

#찬스 카운트가 남아 있을 경우
while turns > 0:
    #실패 횟수(단어 매치 수)
    failed = 0
    
    #정답 단어 반복
    for char in word:
        #추측 문자가 포함되어있는 경우
        if char in guesses:
            #추측 문자 출력
            print(char, end=' ')
        else:
            #틀린 경우 대시로 처리
            print('_', end=' ')
            failed += 1
    #단어 추측을 성공한 경우
    if failed == 0:
        print()
        print()
        print('Congratulations!')
        
        break
    print()
    #추측 단어 문자 단위 입력
    guess = input("Guess a character :")

    #단어 더하기
    guesses += guess

    #정답 단어에 추측한 문자가 포함되지 않을 경우
    if guess not in word:
        turns -= 1
        #오류 메세지
        print("Oops! Wrong")
        #남은 기회 출력
        print('You have', turns, 'more guesses!')

        if turns == 0:
            #실패 메시지
            print("Bye!") 




