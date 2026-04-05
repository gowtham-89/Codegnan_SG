'''
control statements :
1.conditional statements
 .if
 .else
 .elif
 .nested if

2.looping statements
  .for
  .while
  .nested loops

3.jumping statements
  .pass
  .continue
  .Break


'''
'''
syntax :
if condition:
   statements
else:
   statements    
'''
age = int(input("enter the age"))
if age>18:
    print("you are eligibile for vote")
elif age==18:
    print("you can also vote")
else:
    print("you need to wait")        