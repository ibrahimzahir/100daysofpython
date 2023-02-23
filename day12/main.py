#Since lists are indexed, lists can have items with the same value:
#Lists allow duplicate values:


nList = ["apple", "mango", "red", "red", "passion fruit"]

print (nList)

#determine list length

print(len(nList))


#List Items - Data Types
#List items can be of any data type: 
# #String, int and boolean data types:

list1 = ["apple", "mango", "passion", "cheese",  "kunnaru"]
list2 = ["red", "blue", "white"]
list3 = [True, False, True]


#Access Items
#List items are indexed and you can access them by referring to the index number:
#Print the second item of the list:

print("List1" + " " +  list1[1])

#Print the last item of the list: Negative indexing means start from the end

print(list1[-1])


#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new list with the specified items.

print(list1[2:4])


#By leaving out the start value, the range will start at the first item:

print(list1[:3])


#By leaving out the end value, the range will go on to the end of the list:

print (list1[2:])


#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

if "apple" in list1:
    print("Apple is present in the list") 
else: 
    print("No apple in the list")