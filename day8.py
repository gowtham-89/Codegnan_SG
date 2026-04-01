#TABLES
'''
table_num = 8
for j in range(1,21):
    print(f"{table_num} X {j} = {table_num*j}")
'''
#COUNTING NO.OF UPPER AND LOWER
'''
an = "python IS a programming language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U +=1
    elif ch.islower():
        count_L +=1
print(count_U)
print(count_L)

an = "python IS a programming language"
cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(cap_L)
print(small_L)
'''
#ATM ATHUENTICATION
'''
ICIC_teja_AC_details = {"Name" : "Sunny",
                        "ATM PIN" : "0066"}
print("WELCOME TO ICIC ATM")
print("PLS INSERT YOUR ATM CARD")
ICIC_user_pin = input("pls enter 4 digits ATM pin: ")
if len(ICIC_user_pin) == 4:
    if ICIC_user_pin in ICIC_teja_AC_details['ATM PIN']:
        print("The pin is correct")
    else:
        print("you have entered invalid pin")
else:
    ("pls enter 4 digit pin ")
'''
#PERFECT NUMBER
per_num = int(input("Enter a number:"))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")















