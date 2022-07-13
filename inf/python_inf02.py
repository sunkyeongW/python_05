#게임만들기 심화 학습

import time
import csv
import random
import winsound


user = input("What is your name? :")

print("hi," +user+"! Let's time to play hangman game!")
print()

time.sleep(1)

print('Start Loding...')

time.sleep(0.5)

#csv 단어 리스트
words = []

with open('./word_list.csv', 'r') as f:
    reader = csv.reader(f)

    #header 스킵
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)

q = random.choice(words)

word = q[0].strip()

guesses = ''

turns = 10

while turns > 0 :

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end= ' ')
    
        else:
            print('_', end= ' ')
            failed += 1


    if failed == 0:
        print()
        print()
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations!')

        break
    print()

    print()
    print('hint : {}'.format(q[1].strip()))

    guess = input("추측해라 :")

    guesses += guess

    if guess not in word:
        turns -= 1
        print('oops')
        print(turns, 'more chance')

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)

            print('bye')
    


