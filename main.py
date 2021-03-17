#Hangman
from time import sleep
import random
from ab import parts

##prints a hangman picture
print("Welcome to Hangman")
print('  ','-------')
print('  ','|     |')
print('  ','      O')
print('  ','     -|-')
print('  ','      |')
print('  ','     / \\')
print('  ','-------')


print('Let me think of a word')

##Wait time function

def wait():
    for i in range(5):
        print('.',end =" ")
        sleep(.5)
    print()

wait()


## List of words
words=['mouse','cat','rabbit','banana','potato','python']

##creates a choice among words

picked =random.choice(words)
print("The word has",len(picked),"letters")

for i in range(len(picked)):
    print('_',' ',end =" ")
print()

###creates  a list for right and wrong guess

right=['_'] * len(picked)
wrong =[]


## prints letter in right with _'s

def add_letter():
    for i in right:
        print(i,' ',end=" ")
    print()


def wrong_letter():
    print("Wrong letters:",end=" ")
    for i in wrong:
        print(i,' ',end=" ")
    print()

##Main Loop

while True:
    print("==========================================")
    guess=input("Guess  a letter")
    if guess in picked:
        print("Let me check")
        index=0
        for i in picked: 
            if i==guess:
                right[index]=guess
            index=index+1
        wait()
        add_letter()
        wrong_letter()
        parts(len(wrong))

    elif guess not in picked:
        print("Let me  check")
        wait()
        if guess in wrong:
            print("You already guessed",guess)
            wrong_letter()

        else:
            print(guess,"is not in my word")
            wrong.append(guess)
            parts(len(wrong))


    if len(wrong) > 4:
        print("Game Over!")
        print("I picked", picked)
        break
    
    if '_' not in right:
        print("You guessed it!")
        print("I picked", picked)
        break