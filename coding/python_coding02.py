#"파이썬 데이터 타입"
print('---' * 7)
print('파이썬 숫자형 데이터 타입')
print('정수형(int)')
print(-1)
print(0)
print(1)
print()
print('실수형(float)')
print(-1.1)
print(3.34243)
print()


print('숫자형 연산자')
print('1 + 1 =', 1 + 1)
print('2 - 1 =', 2 - 1)
print('3 * 2 =', 3 * 2)
print('4 / 2 =', 4 / 2)
print('3 % 2 =', 3 % 2)
print('3 // 2 =', 3 // 2)
print()


print('math 모듈')
from cmath import sqrt
import math

print('제곱근 sqrt :',math.sqrt(4))
print('제곱 pow :',math.pow(4, 3))
print()


print('random 모듈')
import random

print('랜덤 기능 :', random.random())

print('---' * 7)
print('파이썬 문자형 데이터 타입')
print('hello world')
print("hello world")
print('''
'python'
'world'
'star'
''')
print()


print('문자형 연산자')
print("'1' + '1' =", '1' + '1')
print("'hello를 10번 입력해라.", 'hello' * 10)
print('hello world의 길이 :', len('hello world'))
print('hello star'.replace('star', 'python'))
print()

print('---' * 7)
print('파이썬 리스트형 데이터 타입')

print('리스트형 선언')
names = ['star', 'paper', 'lipstick']
grades = [2, 1, 4]

print('리스트형 연산자')
print(names[1])
print(len(names))
print('가장 작은 값 :', min(grades))
print('가장 큰 값 :', max(grades))
print('합계 :', sum(grades))
print()


print('statistics 모듈')
import statistics

print('평균 값 :', statistics.mean(grades))
print()


print('random 모듈')
import random

print(random.choice(grades))
print(random.choice(names))