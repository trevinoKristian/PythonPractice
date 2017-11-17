
#Code Academy notes

#printing float with two decimals
print("%.2f" % number)

#putting apostrophes in a string
phrase = "this isn\'t flying"

#accessing the second character of a string
char_of_string = phrase[1]

#string methods
len() #gets the length (the number of characters) of a string Ex: len(object) | can also be used for length of lists or dictionaries
.lower() # makes the characters of the string lower cased Ex: phrase.lower()
.upper() # makes the characters of the string upper cased Ex. phrase.upper()
str()  # turns non-strings into strings Ex: str(object)

#methods for float and integers
max() #takes any number of arguments and returns the largest one Ex: max (1,2,3.4.2) = 4.2
min() #takes any number of arguments and returns the smallest one EX: min (4,5,6) = 4
abs() #takes one number and returns the absolute value. EX: abs(-42) = 42

#other methonds
type() #returns the type of the argument Ex: type(4) = int | type("spam") = string 
# can also do conditionals like this: if type(x) == int
.isalpha() # returns True if it contains all alphabet characters, else returns False


# different ways for string concatination
string = "hello" + "world"
string = "I am " + str(24) + " years old"
string = "Hello" + some_string
print "Let's not go to %s, it is way to %s" % (string_1, string_2)

#reciceving input form user
name = raw_input("Please enter your name: ")

#importing modules
from module import function #function import
from module import * #universal import, don't do this cus it could mess up your code
import module #generic import
dir() #shows everything in that module Ex: print dir(math)

#lists
zoo_animals = []
zoo_animals = ["penguin", "elephant", "tiger", "lion"]
zoo_animals[1] #second element in list, which is the elephant
zoo_animals[1] = "heyena" # replaces the 2nd element with heyena
zoo_animals[0:3] # returns the list from element X to element before Y, in this case Y is 0 and X is 3 so it will return a list with elements 0,1,2
zoo_animals[:3] # will return a list with elements 0,1,2
zoo_animals[3:] # will return a list with element 4 and inlcude all the elements to the end of the list
zoo_animals.append("zebra") # adds zebra to the end of the list
zoo_animals.remove("penguin") #removes "penguin" from the list
.index() # returns the index of the item in paranthesis. Ex: zoo_animals.index("elephant") = 1
.insert(index, item) # will insert an item into the list at the specified index. Ex: zoo_animals.insert(2, "rhino")
.sort() # sorts the list alphabetically. Ex: zoo_animals.sort()
sorted(list_of_nums) #sorts a list of numbers from smallest to largest
.pop(index) #removes the item from the list and returns it to you Ex: zoo_animals.pop(2) will remove "tiger" from the list and return it 
.count(obj) #returns count of how many times the obj occurs in the list
del (zoo_animals[1]) #removes animal at index 1 (doesn't return it like .pop())
" ".join(zoo_animals) #joins all of the elements in the list and returns a string. Ex: this will return "penguin elephant tiger lion"
#can also do things do "".join(zoo_animals) so that there is no space in between each animal and also
#can do things like "---".join(zoo_animals) and it will return "penguin---elephant---tiger---lion" 
[1,2,3] + [4,5,6] = [1,2,3,4,5,6] # adding two list lists together returns a list with all of the values
["hello"] * 3 = ["hello", "hello", "hello"] # multiplying a list retuns a list with all of the values

#dictionaries
student_grades = {}
student_grades = {"john" : 89, "Elizabeth" : 95, "Jeff" : 65}
student_grades["john"] #returns the value associate with the "john" key, in this case it is 89
student_grades["peter"] = 78 #this is how you add a new key and value to the dictionary or replace the value associated with the key
del zoo_animals["Jeff"] #removes the "jeff" entry
student_grades.items() #returns keys with their value pairs in an array of tuples (may not be in order)
student_grades.keys() #returns a list of keys
student_grades.value() #returns a list of values

#dictionaries with lists and other data types
my_dict = {
	"fish" : ["c", "a", "r", "p"],
	"cash" : -4483,
	"luck": "good"
}

my_dict["fish"][0] # will return the first element in the list associated with the "fish" key
my_dict["fish"] = ["d", "x", "y"] # replaces dictionary associated with "fish" key 
my_dict["fish"].sort() # sorts the dictionary associated with the "fish" key 
my_dict["fish"].remove("c") #removes "c" from list associated with "fish" key 
my_dict["cash"] = my_dict["cash"] + 50 # adds 50 to the value associated with the "cash" key

#range function
range(stop) #returns list of numbers from index 0 up to but not including the stop index. Ex: range(6) -> [0,1,2,3,4,5]
range(start, stop) #returns list of numbers from start index (includes the start idex) up to but not including the stop index. Ex: range(1, 6) -> [1, 2, 3, 4, 5]
range(start, stop, step) # returns a list of numbers from start index (inclueds the start index) up to but not including the stop index and goes up by the step index. Ex: range(1, 6, 3) -> [1, 4]

#Loops

#for loops (list)
for item in list: # will allow you to iterate through list but not possible to modify list
	#do something

for item in range(len(list)): #will allow you to iterate through list and modify list if needed
	#do something

#for loop (dictionary)
fruits = {'a': "apple", "b" : "berry", "c" : 'cherry'}

for key in fruits:
	print key, fruits[key] #prints both the key and the value. will print the key followed by a space and then the value (the comma does this)

#while/else loop
while condition:
	#do someting
else:
	# do something
#the else will execute immediately after the while loop. If there is a break inside of the while loop or it never entered the while loop, the else will be skipped

#for/else loop
	#same concept at while/else loop


#enumerate function - enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence.
choices = ['pizza', 'pasta', 'salad', 'nachos']

for index, item in enumerate(choices): #basically its a good way to see what index you have gone through
  print index, item  # the comma ensures that both will print on the same line                  

  #will print:
  #1 pizza
  #2 pasta
  #3 salad
  #4 nachos

#zip function - basically allows you to iterate over two or more lists at once, stops at the end of the shortest list
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print a
  else:
    print b

#list comprehension

#generate a list of even numbers from 0 to 50
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#create a new list populated by numbers from one to five
new_list = [x for x in range(1, 6)] # => [1, 2, 3, 4, 5]

#create a new list of the previous numbers doubled
doubles = [x * 2 for x in range(1, 6)] # => [2, 4, 6, 8, 10]

#create a new list that for doubled numbers that are evenly divisible by 3
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0] # => [6]

#another example
c = ['C' for x in range(5) if x < 3] # => ['C', 'C', 'C']

#another example - prints cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0] # => [8, 64, 216, 512, 1000]


#list slicing sytax

[start:end:stride] 
#start describes where the slice starts(inclusive)
#end describes where it ends (non inclusive)
#stride describes wthe space between items in the sliced list

#example using list slicing syntax
l = [i ** 2 for i in range(1, 11)] # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2] # => [9, 25, 49, 81]

#slice slicing (without specifiying values)

to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]  #if the  end value is not given, then it defaults to the end of the list
# prints ['D', 'E'] 

print to_five[:2] # if a start value is not given then it defaults to the begining of list
# prints ['A', 'B']

print to_five[1:2] # if the stride value is not given then it defaults to 1

print to_five[::2]  #in this example, only the stride value is given there for the other values default to begining and end of list
# prints ['A', 'C', 'E']

print to_five[::-1] # if the stride value is negative, then it reverses by the stride value
#prints ['E', 'D', 'C', 'B', 'A'].


#Anonymous Functions (lamda functions) - they're usefull when you only need to use a function once


lamda x: x % 3 == 0

#is equivalent to
def by_three(x):
	return x % 3 == 0

#filter function
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list) # => [0, 3, 6, 9, 12, 15]
#parameter 1 for the filter funtion is the lambda function, parameter 2 is what you want to pass it

#another example - Set message to the result of calling filter() with the appropriate lambda that will filter out the "X"s. The second argument will be garbled.
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message # => I am another secret message!

#Bitwise operations
bin() # enter a number in the paranthesis and it will return the binary equivalent to it
oct() # returns the base 8 representation of the number
hex() # returns the base 16 representtion of the numer


#Classes

pass # used as a placeholder in areas of code where Python expects an expression (doesn't do anything)

#By convention, classes start with a capital and like the ZooAnimals for two words

#Parent classes will inherit from the object class so it will have object in the parameter
class NewClass(object):

#class that inherits from a parent class. The class that you are inheriting from goes in the paranthesis
class SomeClass(ParentClass):

#global variables - variables that are available everywhere
#member variables - variables that are only available to members of a certain class
#instance variables - variables that are only available to particular instances of a class

__init__() # this function is required for classes, it is used to initialize the objects it creates
# it always takes at least one argument ,self. | self refers to the object being created

#for a variable passed in the init() function set self.varaiable = variable. You don't have to worry about the self argument.
__init__(self, variable):
    self.variable = variable  #self.variable becomes a member variable i think cus it can be used by any method within the class

#defines how to represent an object of the class
__repr__()

#Anywhere within the class, whenever you want to reference or make changes to the variable, you always refer to it as self.variable
#Anywhere outside the class, you refer to it by YourObject.variable

#methods inside of a class will always need self as the first parameter or only parameter
def some_method(self):

#subclass can overide parent methods that it inhereits
#subclass can also choose to use parent method instead of overidding it using super
super(ParentClass, self).parent_method()

#Creating a new instance of a class
newObject = ClassName()


#File Input/Output

#open a file in write mode
f = open("output.txt", "w")

#open a file in read and write mode
my_file = open("output.txt", "r+")

#write to a file
.write() #method takes a string argument Ex: my_file.write("Data to written")

#open a file in read mode
my_file = open("output.txt", "r")

#read the file
.read() #Ex: my_file.read()

#read from a file line by line
my_file.readline()

#close the file - must do this to successfully write/read the file
.close() #Ex: my_file.close()

#automatically close file after write , can use this format for "r" and "r+" as well
with open("output.txt", "w") as my_file:
	my_file.write("anthing i want to write")

#lets us check to see to see whether a file is close. 
my_file.closed #returns True if file is closed, False if it is opoen