'''
if statement-->this(if statement)is used to check any condition,if the condition becomes
true then it will enter in side the(if statement) 

age = int(input("enter your age"))
if age >= 18:
    print("your age is 18 or above")

age = int(input("enter your age"))
if age>=18:
    print("you can vote")

'''
'''
if-else statement--> this is also called as fall back statement which only excute when the
(if statement) becomes false

age = int(input("enter your age"))
if age >= 18:
    print("you can vote")
else:
    print(f"you can not and have to wait{18-age}years")

total_amount = int(input("Enter the total number of shopping amount:"))
if total_amount >= 150:
    print("no delivery cost")
else:
    print(f"add {150-total_amount} to your cart")


total_salary = int(input("enter your total salary:"))
if total_salary >= 50000:
    print("you eligible for this loan")
else:
    print(f"you are not eligible until your salary adds {50000-total_salary} more")
'''
'''
if-elif-else statement (if + else)---in the elif part,i can write more conditions

student_marks = int(input("enter your marks"))
if student_marks >=90:
    print("you got A+ grage")
elif student_marks >=75:
    print("you got A grade")
elif student_marks >=50:
    print("you got B grade")
else:
    print("you are fail next time better luck")'''
'''
#USER CALCULATOR
num_1 = int(input("enter 1st number:"))
num_2 = int(input("enter 2nd number:"))
user_choice = (input("enter your choice:"))
if user_choice == "+":
    print(num_1 + num_2)
elif user_choice == "-":
    print(num_1 - num_2)
elif user_choice == "*":
    print(num_1 * num_2)
else:
    print("error")
#another method
num_1 = int(input("Enter 1st number:"))
num_2 = int(input("enter 2nd number:"))
user_choice = (float(input("enter your choice \n1.add \n2.sub \n3.mul \n4.dive")))
if user_choice == 1:
    print(num_1 + num_2)
elif user_choice == 2:
    print(num_1 - num_2)
elif user_choice == 3:
    print(num_1 * num_2)
elif user_choice == 4:
    print(num_2 / num_2)
'''
user_choice = int(input("pls enter any number:"))
if user_choice % 2 == 0:
    print(f"{user_choice}is a even number")
else:
    print(f"{user_choice}is odd number")
    
    
