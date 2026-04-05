
'''
print(9+8)
print("python" + "language")
print([1,2] + [3,4])
'''

#CONCATENAGTION --->This is nothing but,a (+) behaviour...
#CASE-1
#INTEGERS--->This will act as addition for the int
#CASE-2
#for other datatypes (we have to us same type)this (+) act as concatenation
#if try to different data types with concatenation it wont be work
'''
print("raju" + [1,2])-->TypeError: can only concatenate str (not "list") to str
print([4,3] + "sunny")--->TypeError: can only concatenate list (not "str") to list
'''
#tuple()--->is a collection of different datatype and this is represented by (),separated by (,)
'''
thing = (1,"teja",[2,3],(8,9))
print(thing)--->(1, 'teja', [2, 3], (8, 9))
'''
'''
thing = (12,89,"sunny",(23,"bunny",[67,"python is a language",(7,8)],[8,('python',[34,9])]))
print(thing)
'''
'''
Num = 9
Num_2 = 90
print(f"before swapping Num = {Num} and Num_2 ={Num_2}")
Num,Num_2 = Num_2,Num
print(f"After swapping Num = {Num} and Num_2 ={Num_2}")
'''


leap_year = int(input("Enter a leap year:"))
if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
    print(f"yes,{leap_year} is a leap year")
else:
    print(f"no,{leap_year} is not a leap year")--->Enter a leap year:2024
yes,2024 is a leap year
    
                
