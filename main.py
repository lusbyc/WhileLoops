#Week 4 Homework: While Loops

#1
number = 1
userInput = int(input("Please enter a whole number greater than or equal to 1: "))
print(f"Thank you. Numbers {number} through {userInput} are displayed below.")
while number <= userInput:
    print(number)    
    if number == userInput:
        break
    number += 1

#2
number = 1
userInput = int(input("Please enter a whole number greater than 1: "))
print(f"Thank you. Numbers {userInput} through {number} are displayed below.")
while userInput >= number:
    print(userInput)
    if userInput == number:
        break
    userInput -= 1

#3 
print()
print("Uppercase Alphabet:")
letter = 65
while letter in range(65,91):
    print(chr(letter),end=' ')
    letter += 1

print()
print()

print("Lowercase Alphabet:")
letter = 97
while letter in range(97,123):
    print(chr(letter),end=' ')
    letter += 1
print()
print()

#4
number = 0
print("Even numbers between 1 and 100 are displayed below.")
while number < 100:
    number += 1
    while number % 2 == 0:
        print (number)
        break
        if number > 100:
            break
 
#5 
number = 0
print("Odd numbers between 1 and 100 are displayed below.")
while number < 100:
    number += 1
    while number % 2 != 0:
        print(number)
        break
        if number > 100:
            break

#6
number = 1
sum = 0
userInput= int(input("Please enter a number greater than 1: "))
print(f"The sum of all whole numbers from {number} to {userInput} are displayed below.")
while number <= userInput:
    sum = sum + number
    number += 1
    if number > userInput:
        print(sum)    
        break

 
#7
print('Multiplication Table')
userInput = int(input("Please enter a whole number: "))
number = 1
while number <= userInput:
    product = userInput * number
    print(f"{userInput} * {number} = {product}")
    number += 1
    if number > userInput:
        break
