#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

#The insert() method inserts an item at the specified index:

insList = ["easy", "medium", "difficult", "Ext difficult"]

insList.insert(2, "Little Easy")

print(insList)


#Append Items
#To add an item to the end of the list, use the append() method:

listApp = ["easy", "medium", "difficult", "Ext difficult"]
listApp.append("No comment")

print(listApp)


#Remove Specified Item
#The remove() method removes the specified item.

listApp = ["easy", "medium", "difficult", "Ext difficult"]
listApp.remove("easy")
print(listApp)


