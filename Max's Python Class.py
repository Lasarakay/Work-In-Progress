'''
#import random
#random_number = random.randint(0, 4)
mylist = ["Noi", "Thai 2 Go", "Thailandia", "Olive Garden", "Five Guys"]

for restaurant in mylist:
    print("Do you want to go to?")
    print(restaurant)
'''


import random

def restaurant():
    random_restaurant = random.randint(0, 4)
mylist = ["Noi", "Thai 2 Go", "Thailandia", "Olive Garden", "Five Guys"]
print(restaurant())


'''
def myadd(num1, num2):
    return num1 + num2

print(myadd(3,4))
'''





'''
import random

random_number = random.randint(0, 10)
guess = int(input("Guess a number: "))

while True: #guess != random_number:
    if guess > random_number:
        print("This guess is too high")
        print("Guess again")
        guess = int(input("Guess a number: "))
    elif guess < random_number:
        print("This guess is too low")
        print("Guess again")
        guess = int(input("Guess a number: "))
    else:
        print("Correct! :)")
        break
    #guess = int(input("Guess a number: "))
    
#if guess == random_number:
#    print("Correct! :)")
'''


'''
text = "Max"

print(text, "This is a string of text too")

if text == "Max":
    print("Your name is Max")
'''

'''box = input("What is your name? ")
#print("Hello,", box)

if box == "Sara":
    print("Hello, Sara")
'''
'''
box1 = int(input("Give me a number: "))
box2 = int(input("Give me another number: "))

result = box1 / box2

print(result)
if result == 42:
    print("Whatever")
'''    




