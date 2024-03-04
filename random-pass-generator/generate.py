import math as m
import random as r
#stiring value



alpa = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
special_char = "$#@&?!€"


while True:
  pass_len = int(input("what should be the length of password ? "))
  
  #using 50,30,10 rule of getting the exact length of characters
  pass_char = pass_len//2
  num_len = m.ceil(pass_len*30/100)
  special_len = pass_len-(pass_char+num_len)
  
  password = []
  
  def pass_generator(length, array , is_alpha = False):
    for i in range(length):
      index = r.randint(0,len(array)-1)
      character = array[index]
      if is_alpha:
        case = r.randint(0,1)
        if case == 1:
          character = character.upper()
  
      password.append(character)
  
  
  #getting string password
  pass_generator(pass_char , alpa, True)
  
  #getting numerical password
  pass_generator(num_len, num )
  
  #getting special_char password
  pass_generator(special_len, special_char )
  
  #mixing the all three password 
  r.shuffle(password)
  
  emptypass = ""
  
  for i in password:
    emptypass += str(i)
  
  print(emptypass)

  usr = input("want more password to be generated? (y/n): ").upper()
  if usr == "Y" or usr == "YES":
    continue