str = input("please enter a string")
str = str.replace('[','').replace(']','').replace('"','').replace("'",'').split(',')
print(str)