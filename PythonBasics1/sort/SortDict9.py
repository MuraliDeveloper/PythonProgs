# Python program to sort the list  
# alphabetically in a dictionary 
dict ={ 
    "L1":[87, 34, 56, 12], 
    "L2":[23, 0, 30, 10], 
    "L3":[1, 6, 2, 9], 
    "L4":[40, 34, 21, 67] 
} 
  
print("\nBefore Sorting: ") 
for x in dict.items(): 
    print(x) 
  
print("\nAfter Sorting: ") 
  
for i, j in dict.items(): 
    sorted_dict ={i:sorted(j)} 
    print(sorted_dict) 
    
    

# Python program to sort the list  
# alphabetically in a dictionary 
  
dict ={ 
    "L1":["Geeks", "for", "Geeks"], 
    "L2":["A", "computer", "science"], 
    "L3":["portal", "for", "geeks"], 
} 
  
print("\nBefore Sorting: ") 
for x in dict.items(): 
    print(x) 
  
print("\nAfter Sorting: ") 
for i, j in dict.items(): 
    sorted_dict ={i:sorted(j)} 
    print(sorted_dict) 
    
    
    
    
    
    
    
    # Python program to sort the list  
# alphabetically in a dictionary 
dict={ 
    "L1":[87,34,56,12], 
    "L2":[23,0,30,10], 
    "L3":[1,6,2,9], 
    "L4":[40,34,21,67] 
} 
  
print("\nBefore Sorting: ") 
for x in dict.items(): 
    print(x) 
  
sorted_dict = {i: sorted(j) for i, j in dict.items()} 
print("\nAfter Sorting: ", sorted_dict) 