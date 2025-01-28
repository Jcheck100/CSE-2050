"""
Strings:
A collection/sequence of characters
Can access individual elements in the sequence using the [] operator

IE my_str = "hello"
    print(my_string[0]) prints h

strings are immutable, meaning my_string[0] = "i" will cause an error
"""

string1 = "data structures are cool "

string1.upper() #uppercase all
string1.lower() #lowercase all
string1.capitalize() #capitalizes first letter first word
string1.count('a') #counts all instances of a in string1
string1.strip() #returns string with leading and changing whitespace removed
string1.split(sep=' ') #seperates string into a list based off each whitespace, or the specifed splicer (sep='whatever you want to seperate by')

"""
Lists:

Ordered sequence of objects
Can be different types (ie: ints, floats, str, etc.)

Access indivdual elements with []
Mutable ie L[0] = "one" will replace index 0 with "one"

"""
list1 = ['cheese', 'pepperoni', 'onion']

list1.append('cheese') #adds cheese to end of list1
list1.extend(['red pepper', 'green pepper']) #used to add the contents of one list to the end of another
list1.insert() #will put whatever at the specifed index ie. (2, 'pepper') will put pepper between pepperoni and onion
list1.remove() #removes the first instance of a specified value
list1.clear() #removes all elements from a list
list1.index() #returns the index of a value in the list
list1.count() #returns how many times a certain value occurs in the list
list1.sort() #sorts the list in accending order, if you use reverse = True then it will sort in decending order
list1.reverse() #reverse the list

"""
Tuples:

Ordered sequence of objects.
Objects can be different types.
[] used to access elements.
immutable.
"""

"""
Slices of sequences:

A segmment of a string, list, tuple

player = 'Josh Allen'
player[2:8] returns "sh All"
player[:8] returns "Josh All"
player[2:] returns "sh Allen"

colors = ["red","yellow","blue"]
colors[1:] = ["orange"] returns ["red", "orange"]
colors[:1] = ["orange"] returns ["orange","yellow","blue"]
colors[1] = ["orange"] ["red",["orange"],"blue"] ***Exam Question?
"""

"""
Dictionaries:

Unordered collection of key-value pairs (not a sequence)
Defined with {}
Keys can be different types, but must be immutable types
Can add new pairs or access current dict using []
can also use [] to reassign a value that corresponds to a key
"""

"""
Set:

Unordered collection of immutable objects WITHOUT duplicates
Can add elements to the set with the add method
Can remove with remove
Set is mutable, elements inside are immutable
"""

