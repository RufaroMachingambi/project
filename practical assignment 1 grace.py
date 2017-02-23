


'''number 6 Question:Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
#SOLUTION

>>> def add_string(str1):
	length = len(str1)
	if length>2:
		if str1[-3:]=='ing':
			str1 += 'ly'
		else:
			str1 += 'ing'
		return str1

	
>>> print(add_string("abc"))
abcing
>>> print(add_string("string"))
stringly


''''
number 14 Question: Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''
#SOLUTION

 text="red, white, black, red, green, black"
>>> l=text.split(",")
>>> s=set(l)
>>> print(s)
{' white', ' red', 'red', ' green', ' black'}



