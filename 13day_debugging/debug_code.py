# ############DEBUGGING#####################

# Describe Problem
def my_function():
#   for i in range(1, 20):
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()


# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
# elif year > 1994:
elif year >= 1994:
  print("You are a Gen Z.")


# # Fix the Errors
#age = input("How old are you?")
age = int(input("How old are you?"))
if age > 18:
#print("You can drive at age {age}.")
  print(f"You can drive at age {age}.")
  
  
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)



# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
# b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# https://pythontutor.com/


## Odd or even number programm
number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
  
## Leap year programm
# year = input("Which year do you want to check?")
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
  
# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
#  if number % 3 == 0 or number % 5 == 0:
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
 # if number % 3 == 0:
  elif number % 3 == 0:
    print("Fizz")
# if number % 5 == 0:
  elif number % 5 == 0: 
    print("Buzz")
  else:
 #   print([number]) 
    print(number) 