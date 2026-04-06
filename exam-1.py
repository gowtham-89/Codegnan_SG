'''
dictionary:-it is one of the method in python which have keys:value
it is orderd and changeble
eg:-
account details={"name"="sunny",
                 "account.no"="13245678"}
and = it is an operator which is usefullu for compare the two statements
or  = it is an operator which can tell only either this or that

range()
it is mainly used in loops it will tells us the what should be range of its loop and how many times should loop
eg:-for i in range(i,n+1)

break = it will stop totally
contiue= it will stop at there and contiue for further


num = int(input("enter the number:"))
sum = 0
for i in range(1,num+1):
    if num%i==0:
        sum+=1
if (sum==2):
    print("its a prime")
else:
    print("its not a prime")


num = int(input("enter a number:"))
n1=0
n2=1
for i in range(num+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
'''
num = int(input("enter a number"))
temp = num
rev = 0
while num > 0:
    digit = num%10
    rev = (rev*10)+digit
    num = num//10
if temp == rev:
    print("its a palindrome")
else:
    print("not a palindrome")

#reverse a number
num = int(input("enter a number"))
length = len(str(num))
rev = 0
for i in range(length):
    digit = num%10
    rev = (rev*10)+digit
    num = num//10
print(rev)





    

 
