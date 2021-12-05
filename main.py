#Week 4 Homework: While Loops

#1
number = 1
user_input = int(input("Please enter a whole number greater than or equal to 1: "))
print(f"Thank you. Numbers {number} through {user_input} are displayed below.")
while number <= user_input:
    print(number)    
    if number == user_input:
        break
    number += 1

#2
number = 1
user_input = int(input("Please enter a whole number greater than 1: "))
print(f"Thank you. Numbers {user_input} through {number} are displayed below.")
while user_input >= number:
    print(user_input)
    if user_input == number:
        break
    user_input -= 1

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
print("Even numbers from 1 and 100 are displayed below.")
while number < 100:
    number += 1
    while number % 2 == 0:
        print (number)
        break
        if number > 100:
            break
 
#5 
number = 0
print("Odd numbers from 1 and 100 are displayed below.")
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
user_input= int(input("Please enter a number greater than 1: "))
print(f"The sum of all whole numbers from {number} to {user_input} are displayed below.")
while number <= user_input:
    sum = sum + number
    number += 1
    if number > user_input:
        print(sum)    
        break

 
#7
print('Multiplication Table')
user_input = int(input("Please enter a whole number: "))
number = 1
while number <= user_input:
    product = user_input * number
    print(f"{user_input} * {number} = {product}")
    number += 1
    if number > user_input:
        break
