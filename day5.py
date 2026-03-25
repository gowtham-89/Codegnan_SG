'''
#24 HOUR CLOCK
Time_aday = input("enter 24 hours time:")
parts_ = Time_aday.split(":")
hours_ = int(parts_[0])
min_ = int(parts_[1])
if hours_ >= 13 and min_< 60:
    print(f"{Time_aday} covert into {hours_ -12}:{min_}pm")
else:
    print(f"you are enter normal or min are incorrect")

'''
#list ---> collection of different items (or) different data types in side the [] , which are seperated by,
#          ex--->>[1,"name",[1,2,"teja"]]
'''
list_1 = [1,2,3, "python",[1,2,["python","java"],"lanuage"]]
print(list_1[4][2][0][3])--->h

list_2 = [5,75,890,"raju",["hai",3,4],["kaju","sunny"]]
print(list_2[5][1][2])

'''
#METHODS OF LIST
#1.append()--->this method is used to add new items into list it will only go for the last index
#of the list
#               SYNTAX:--->variable_name.append(item)
'''
list_1 = [1,2,3,4,5]

list_1.append(56)
print(list_1)--->[1, 2, 3, 4, 5, 56]
'''
#2.extend()--->this method is used to list in the list index,where each item or substring is each
#index in the list
#              SYNTAX:--->variable_name.extend(item)
'''list_1.extend("teja")
print(list_1)--->[1, 2, 3, 4, 5, 't', 'e', 'j', 'a']
'''
#3.remove()---> this method will delet the item or value directly
#              SYNTAX:--->variable_name.remove(item)

list_1 = [23,"sunny",7,67]
'''
list_1.remove("sunny")
print(list_1)--->[23, 7, 67]
'''
#4.pop()--->this method will deleat the item or the variable based on index position
#              SYNTAX:--->variable_name.pop(index value)
list_1.pop(3)
print(list_1)--->[23, 'sunny', 7]

#NOTE:-
##MUTABLE---> I CAN DIRECTLY MODIFY ON THAT PARTICULAR VARIABLE
##IMMUTABLE--> I CAN NOT MODIFY DIRECTLY ON THE VARIABLE

















    
    
    
