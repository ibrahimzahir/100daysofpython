Day 1 - Variables 

Print to the Console 
String Manipulation and Code Intelligence
Debugging

The Python Input Function
Python Variables
Variable Naming



Day 2 - Understanding Data Types
Type Error, Type Checking and Type Conversion
Data Types
Mathematical Operations


Day 3 - Multiple Variables
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:


Day 4 - Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.


Day 5 - Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.


Day 6 Uppercase
The upper() method returns the string in upper case:


Day 7 String Concatenation
To concatenate, or combine, two strings you can use the + operator.


Day 8 - String Format

we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)

But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:



Day 9 - Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
