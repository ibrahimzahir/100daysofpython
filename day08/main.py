# Day 7- String Format

# we cannot combine strings and numbers like this:

# age = 36 txt = "My name is John, I am " + age print(txt)

# But we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:


fruit = "mango"
quantity = 24
price = 134.49
myOrder = "I want to buy {} quantity {} and total {}"
print(myOrder.format(fruit, quantity, price))


partners = "girls"
number = 2

myp = "I want to have {} {}"
print(myp.format(number, partners))


