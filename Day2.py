#List 
my_list=[1,2,3,4]
print(my_list)
print(type(my_list))

#properties and method
print(len(my_list))
my_list.append(5)# is used to add an element at the end of the list
print(my_list)
my_list.insert(0, 0) # is used to add the element at a specific location or index
print(my_list)
my_list.extend([7,8,9])#is used to add multiple element to the end of the list
print(my_list)
my_list.remove(3)# is used to remove the last element from the line
print(my_list)
my_list.pop()# is used to remove the element from the list 
print(my_list)
#Properties
#ORDERED and mutable
my_list[3]=10 # is used to change the value of an element at a specific index
print(my_list)
#duplicate and heterogeneity
FUN=[1,2,3,12,44,True,False,"Hello"]
print(FUN)