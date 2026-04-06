'''
num = int(input("Enter the number:"))
fact = 1
for i in range(1,num+1):
    fact=fact*i
print(fact)
'''
num = int(input("Enter a number:"))
lenght = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum+=digit**lenght
    temp//=10
if num == sum:
    print("is amstrong")
else:
    print("not a amstrong")
