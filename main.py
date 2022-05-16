import time
import random
restart = ' '

while restart.upper() not in ['NO' ,'N', 'EXIT']:
  name=input('Hello. What is your name? : ')
  print("Hello," ,name,". Welcome to my magic 8-Ball")
  time.sleep(2)
  print(' ')

  responses=['Yes', 'No', 'Possibly', 'not sure',]
  print(responses)
  choice=int(input("Press 1 if you would like to add another option. Press 2 if you want to keep defult settings. = "))
  if choice==1:
    additional=input('For your personalization, Would you like to add any aditional responses? : ')
    responses.append(additional)
  print(responses)
  print(' ')

  question=input('What would you like to ask my 8-Ball? : ')
  answer=random.choice(responses)
  time.sleep(1)
  print(' ')
  print("Actually",name,", My answer to (" ,question, ") is" ,answer,)
  time.sleep(2)
  print(' ')
  
  restart = input('Press enter to play again')
  print(' ')
  print(' ')