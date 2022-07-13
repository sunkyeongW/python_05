#"파이썬 변수"
print('---' * 7)
print('파이썬 변수')

name = 'sori'

message = 'hi, ' +name+ ' ... by, ' +name+ '.'

print(message)
print()

#"파이썬 입력과 출력"
print('---' * 7)
print('파이썬 입력과 출력')

user = input('What your name? :')

message1 = 'hi, ' +user+ ' ... by, ' +user+ '.'

print(message1)

#"파이썬 외부 모듈 사용"
print('---' * 7)
print('파이썬 외부 모듈 사용')

import pandas

records = pandas.read_csv('1000 Records.csv')

print(records)
print(records.describe())
print(records.head())
print(records.tail())

