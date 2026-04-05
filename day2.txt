'''
variables -->variables are named storage location that is used to hold data in the memory,
to make it simple it is the label which points out to a value -->storage placeholders

Rules for defining variables
-->A-Z,a-z,0-9
-->start with uppercase,lowercase letters,even with a underscore _
-->but you cannot start with symbols(@,#,$...),even numbers also
Better preferable way is go with general purpose -->you want to store your details name,
email_id, account_number..

'''
'''
a = 5
b = 6
#python is dynamically typed, you need not define the datatype and also
#only the recent value to the variable with same name is pointed

print(a)
print(b)

#1a23c = 25 #syntax error
#@werf = 4.5 #syntax error
#$dsf = 12 #invaid syntax

#store your personal details

name = "codegnan"
location = "vishakapatnam"
age = 7
email_id ="codegnan@gmail.com"
print(name,location,age,email_id)




#how to assign multiple values to a variables
raju,rani,ramu = 21,23,43
print(raju)
print(rani)
print(ramu)

#assign same value to multiple variables
ramu=raju=rani=21
print(ramu,raju,rani)


#key words are reserved words which will have specific usage
#there are 35 keywords in python
#never use keywords as identifiers

#if = 23
#lambda = 'sunny'
#false = 0 #cannot assign

#python is case-senstive
false = 25

#identifiers are names given to variables,functions,classes,objects...

#literals are fixed values to a identifier
name = 25

#name is identifier,25 is literal

#single line comments --> #
#Multi line comments -->with triple quotes
'''
'''
#built-in Datatypes -->Numeric,boolean,collections

#Numeric datatypes --> int,floats,complex
#int --> count,values,quantities
#float --> temperature,percentage,price,
#complex -->specific conversions(real and imaginary)
count = 40
print(count)
print(type(count))

price = 17.67
print(price)
print(type(price))

j3 = 25
value = 2+3j
print(value)
print(type(value))


#typecasting -->converting one type to another
#int -->float,complex

age = 25
print(type(age))

b = float(age)
print(b)
c = complex(age)
print(c)
print(type(c))


num = 2+3j
print(type(age))
#float,complex
price = 275.25
print(type(price))
d = int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e))


f = 2+5j
print(type(f))
#complex to int is not possible
#complex to float is not possible


#typeconversion of bool
a = True
b = int(a)
print(b)
c = float(a)
print(c)
d=complex(float(int(False)))
print(d)
print(type(d))
'''
#Input -->input()/output -->print()
a=int(input("enter a number:"))
print(a)
print(type(a))
a = float(input("enter a number:"))
print(a)
print(type(a))

#Now let's work on simple case study using above -->fee calculator

#details of the student
name = input("Enter the student name:")
print("*************")
admission_fees = int(input("Enter the admission fees:"))
tution_fees = int(input("Enter the tution fees:"))
hostel_fees = int(input("Enter th hostel fees:"))

#calculate the total fees
total_fees = admission_fees + tution_fees + hostel_fees
print("<<<<wait for few seconds>>>>")
print("Student name:",name)
print("Admission fees is:",admission_fees)
print("Tution fees is:",tution_fees)
print("Hostel fees is:",hostel_fees)
print("Total fees is =",total_fees)
print("****THANK YOU****")









      
