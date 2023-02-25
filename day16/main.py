#Loop Through a List
#You can loop through the list items by using a for loop:

lopList =  ["apple", "banana", "cherry"]

for x in lopList:
    print(x)



#Loop Through the Index Numbers
#You can also loop through the list items by referring to their index number.

#Use the range() and len() functions to create a suitable iterable.

lopList =  ["apple", "banana", "cherry"]

for i in range (len(lopList)):
    print(lopList[i])


#While Loop
#You can loop through the list items by using a while loop.
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
#increase the index by 1 after each iteration.

wList =  ["apple", "banana", "cherry"]
i = 0
while i < len(wList):
    
    print (wList[i])
    i = i +1



#A short hand for loop that will print all items in a list:
wList =  ["apple", "banana", "cherry", "foo", "ba"]
[print(x) for x in wList]