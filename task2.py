
str = input("please enter a string")
letter = input("please enter the letter")

if letter in str:
  print([index for index, character in enumerate(str) if character == letter])

#print (str.find(letter))
# print("Current character", "position at",index)