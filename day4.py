
#string --> string is a collaction of charecters,which represented by ("" or '')
#--------->and we can access the using indexing(string can also allow negative indexing)
#--------->this is also immutable,where i could not able to modifiy on that particular variables
#len()---->len() method is used to get char present in the string or find the laenght of the
#          string
'''
#any = 'python programming'
#print(any)
#print(any[7])
#print(any[7,8,9])#-->TypeError: string indices must be integers, not 'tuple'
#so = any.replace("python","java")
#print(any[7:13])---> slicing
#print(any)
#print(so)
#print(any[-7])
#print(any[20])---->IndexError: string index out of range


day_4 = "I am sunny from vizag,and i am currently purshuing my betch in anits "

print(f"MY name is {day_4[5:11]}")
print(f"MY btech in {day_4[-6:-1]}")

name = "sunny"
print(name[::-1])--->to reverse a string
print(len(day_4))
'''
#NOTE :- WE CAN CONVERT A STRING INTO INTEGER,IF THEY CONTAIN ONLY INTEGER VALUE
'''
some = "123p"
num = int(some)--->ValueError: invalid literal for int() with base 10: '123p'
'''
some = "Python Is Good Coding Language"
'''
print(some.split(" "))--->['python', 'is', 'good', 'coding', 'language']
print(some.split("coding"))--->['python is good ', ' language']
'''
#           ------------------------------------------------------------
                               #Methods of string
#          ------------------------------------------------------------
#1.split()---> remove space,and in the list[]it will give the seperated thing in each index
#                   syntax---> variable_name.split("substring")
#print(some.split(" "))--->['python', 'is', 'good', 'coding', 'language']
#2.lower()--->this is used to convert all letter into lower case
#print(some.lower())--->python is good coding language
#                   syntax--->variable_name.lower("substring")
#3.upper()--->this is used to covert all letters into upper case
#                   syntax--->variable_name.upper("substring")
#print(some.upper())--->PYTHON IS GOOD CODING LANGUAGE
#4.replace()--->this is used to replace old str with new string
#                   syntax--->variable_name.replace("old str","new str")
#print(some.replace("Python","java"))---->java Is Good Coding Language
if "python" in some:
    print("yes")
else:
    print("no")















