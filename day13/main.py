#Python - Change List Items
#To change the value of a specific item, refer to the index number:

list1 = ["man", "woman", "House", "Table", "Banana", "Apple"]
list1[1] = ["Pinapple"]

print(list1)

list1 = ["man", "woman", "House", "Table", "Banana", "Apple"]
list1[1] = "Pinapple"

print(list1)

#Change a Range of Item Values

#To change the value of items within a specific range, 
# define a list with the new values, and refer to the 
# range of index numbers where you want to insert the new values:

list2 = ["man", "woman", "House", "Table", "Banana", "Apple"]
list2[2:4] = ["nasdhag", "bitcoin"]
print(list2)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
list2 = ["man", "woman", "House", "Table", "Banana", "Apple"]
list2[1:1] = ["nasdhag", "bitcoin"]
print(list2)


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:1] = ["blackcurrant", "watermelon"]
print(thislist)