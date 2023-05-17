#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:09:34 2023

@author: sunyenpeng
"""
import random
#Pre-work:
while True:
    print('Enter 5 different numbers from 1 to 69, with spaces between')
    print('each number. (For example: 2 17 23 30 59)')
    response = input('> ')
    
    numbers = response.split()
    if len(numbers)!=5:
        print('Please enter 5 numbers, seperated by spaces.')
        continue
    
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Please enter numbers, like 23, 15...")
        continue
    
    for i in range(5):
        if not(1<=numbers[i]<=69):
            print("The numbers must all between 1 to 69.")
            continue
        
    if len(set(numbers))!=5:
        print('You must enter 5 different numbers.')
        continue
    break

while True:
    print("Enter the powerball number from 1 to 26.")
    response = input('> ')
    
    try:
        powerball = int(response)
    except ValueError:
        print('Please enter a number, such as 3, 5, 9...')
        continue
    break

while True:
    print('How many times do you want to play? (Maximum: 1000000).')
    response = input('> ')
    
    try:
        numPlays = int(response)
    except ValueError:
        print('Please enter a number, like 200, 210, 500...')
        continue
    
    if not  (1<=numPlays<=1000000):
        print('You can play between 1 and 1000000 times.')
        continue
    break



#Simulation part:    
price = '$'+str(2*numPlays)
print('It costs', price, 'to play', numPlays, 'times.')
input("Press Enter to start your game...")


def numbercheck(yournumber, winningnumbers, yourpower, winningpowerball):
    ans=0
    reward=0
    for i in yournumber:
        if i in winningnumbers:
            ans+=1
    if ans==0 and yourpower!=winningpowerball:
        print("You got zero numbers, you won 0 dollar.")
    elif ans==1 and yourpower!=winningpowerball:
        print("You got 1 number! But you still don't have rewards.")
    elif ans==2 and yourpower!=winningpowerball:
        print("You got 2 numbers! You won 100 dollars back!")
        reward+=100
    elif ans ==3 and yourpower!=winningpowerball:
        print("You got 3 numbers! You won 1000 dollars back!")
        reward+=1000
    elif ans ==4 and yourpower!=winningpowerball:
        print("You got 4 numbers! Congratulations! You get 10000 dollars back!")
        reward+=10000
    elif ans==5 and yourpower!=winningpowerball:
        print("That's awsome!, You got 5 numbers correct! You won 100000 dollars now.")
        reward+=100000
        
    return reward

possiblenumbers = list(range(1,70))
for i in range(numPlays):
    random.shuffle(possiblenumbers)
    winningnumbers = possiblenumbers[0:5]
    winningpowerball = random.randint(1,26)
    print('The winning numbers are: ', end='' )
    allwinningnums=''
    for i in range(5):
        allwinningnums+=str(winningnumbers[i])+' '
    allwinningnums+= 'and ' + str(winningpowerball)
    print(allwinningnums.ljust(21), end='')
    
    
    if  (set(numbers)==set(winningnumbers) and powerball==winningpowerball):
        print()
        print('You have won the powerball lottery!')
        break
    
    else:
        numbercheck(numbers, winningnumbers, powerball, winningpowerball)
        reward=numbercheck(numbers, winningnumbers, powerball, winningpowerball)
final = '$'+str(2*numPlays-reward)
print('You have wasted', final)
print('Thanks for playing.')
    






























