# importing "operator" for implementing itemgetter 
from operator import itemgetter 

#Approach1
# Python code demonstrate the working of 
# sorted() with lambda 
  
# Initializing list of dictionaries 
lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }] 
  
# using sorted and lambda to print list sorted 
# by age  
print("The list printed sorting by age: ")
print(sorted(lis, key = lambda i: i['age'])) 
  

