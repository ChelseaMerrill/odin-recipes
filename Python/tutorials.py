from operator import truediv

#this function adds two numbers
def add(x,y):
    return x+y
print(add(4,1))

#program to print all the keywords
import keyword
print (keyword.kwlist)
#total count of the keywords (35)
print(len(keyword.kwlist))

#variables 
number = 12345 #number
name = 'Chelsea' #string
grade = 90.5 #float(number witha decimal point)
print(number, name, grade)

#multiple variables in a single row
a,b,c,d = 2, 3, 4, 65,
print(a, b, c, d)

#multiple variables with different data types
who , what, num = 'chelsea', 232, 7.2
print (who, what, num) 

#single value to several variables
graph1 = graph2 = graph3 = 'DataScience'
print(graph1, graph2, graph3)

#memory allocation - if the value is the same, the memory location is the same 
print(id(graph1))
print(id(graph2))

#updating the value of variable and checking memory location
graph2 = 'Python'
print(id(graph2))
#the performance of our coding depends on 2 things: code logic and memory allocation

#5datatypes:
#1:Number
    #Interger - 3
    #Float - 3.5
    #Complex Number - 2 + 3x
#2:String
#3:List
#4:Tuple
#5:Dictonary
print(type(who))

#Operators: 

#1:arthmictic 
x, y = 20.5, 5
print('Addition of x + y = ', x+y)
print('Float Division of x / y = ', x/y) #40.1 (float division divides left hand by right and will result in a float)
print('Interger Division of x // y = ', x//y) #40.0 (interger division is rounded down (floor) 3.1 = 3 but -3.1 = -4)
print('Interger Division of Negative Number =', -10//3) #-4
print('exponents 4 to the power of 2 is', 4**2)
print(12-5*2) #2
print((12-5)*2) #14

#2:comparison 
a,b = 2, 10
print(a>b) #false
print('{} > {} is'.format(a,b), a>b) #2 > 10 is False
print('{} != {} is'.format(a,b), a!=b) #2 1+ 10 is True

#3:logical (and, or, not)
c, d = True, False
print('c and d is', c and d) #False
print (a==b and a<b) #False 
print('not c is', not c) #not c is False
print('not b is', not b) # not b is False
print( not a==b) #True

#4:assignment: used to assign values (a = 10)
    #Augmented Assignment Operator: combines assignment operator with other logical operators, like addition. The operators that allows to write shortcut assignment statement 
e = 5
e = e +1
print(e) #6

#5:bitwise: used to compare binary numbers (& [AND: sets each bit to 1 if both bits are 1], | [OR: sets each bit to 1 id one of the bits is 1], <<[Zero fill Left Shift: shift left by pushing zeros in from the right and let the leftmost bits fall off], >>[Signed Right Shift: shift right by pushing copies of the leftmost bit in from the left and let the rightmost bits fall off], ~[NOT: inverts the bits], ^[XOR: sets each bit to 1 id only 1 of the 2 bits is 1]). It works on bits and performs bit by bit operation
    #decimal number: 17 -> binary number 10001 (2|17 [1], 2|8 [0], 2|4 [0], 2|2 [0], 1)
f, g = 17, 10
print("Binary number for {0} is {0:08b}".format(f)) #Binary number for 17 is 00010001
print("Binary number for {0} is {0:08b}".format(g)) #Binary number for 10 is 00001010
(print(f&g)) #0
(print(f|g)) #27
(print(f^g)) #27
(print(~f)) #-18
(print(f>>2)) #4
(print(f<<2)) #68

#6:membership: used to find a particular value in a sequence ('in' and 'not in')
mylist = [1, 2, 3, 'python', 5]
print(3 in mylist) #True
print ('python' not in mylist) #False

#7:identity: used to compare the memory locations of two objects. 'is' and 'is not' are the identy operators in python, output will be a boolean
h, h2 = 10, 10
print(id(h))
print(id(h2))
print(h is h2) #True
print(h is not h2) #False

j, k = [1,2,3], [1,2,3]
print( j is k) #False
print( j is not k) #True

l, m = 'chelsea', 'chelsea'
print( l is m) #True
print( l is not m) #False

#control statement is used for decision making (if statments: if, if else, if elif else, nested if)

#if
user_age = 15
if (user_age <= 18):
    print ('user is not yet 18')

#if else
if (user_age <= 18):
    print ('user is not yet 18')
else:
    print('over 18')

#if elif else (else if)
my_num = 10

if my_num > 0:
    print('postive number')
elif my_num == 0:
    print('number is zero')
else:
    print('negative number')


month_num = 10
if month_num == 1:
    print('january')
elif month_num == 2:
    print('february')
elif month_num == 3:
    print('march')
elif month_num == 4:
    print('april')
elif month_num == 5:
    print('may')
elif month_num == 6:
    print('june')
elif month_num == 7:
    print('july')
elif month_num == 8:
    print('august')
elif month_num == 9:
    print('september')
elif month_num == 10:
    print('october')
elif month_num == 11:
    print('november')
elif month_num == 12:
    print('december')
else:
    print('enter a valid number')

#nested if (no switch statments)
if my_num > 0:
    print('postive number')
    if my_num == 0:
        print('number is zero')
else:
    print('negative number')

# while (only language that you can and an if statement to a while loop) loop
i = 1
while i <= 6:
    print(i)
    i+= 1
print('Done')
# 1
# 2
# 3
# 4
# 5
# 6
# Done

i2 = 1
while i2 <= 6:
    print(i2)
    i2+= 1
else: 
    print('else statement is executed at the end')
print('Done')
# 1
# 2
# 3
# 4
# 5
# 6
# else statement is executed at the end
# Done

#for loop
fruits = ['apple', 'banana', 'grape', 'cheery', 'mango', 'pineapple']
for i in fruits:
    print(i) #returns the list

numberList = [1,2,3,4,5,6,7,8,9,]
for x in numberList:
    print(x)


sum = 0
for val in numberList:
    sum = sum +val
print(sum)


for x in numberList:
    print(x)
else: 
    print('no items left')


for x in 'python':
    print(x)
# p
# y
# t
# h
# o
# n

#range: (start, stop, stop size)
print(range(10)) #range(0,10)

for x in range(2,6):
    print(x)
# 2
# 3
# 4
# 5

for x in range(1, 10, 2):
    print(x)
# 1
# 3
# 5
# 7
# 9

#index
for index in range(len(fruits)):
    print('fruit name is:', fruits[index])
# fruit name is: apple
# fruit name is: banana
# fruit name is: grape
# fruit name is: cheery
# fruit name is: mango
# fruit name is: pineapple

#Enumerate: a method that adds a counter to an iterable and returns it in a form of enumerate object 
for index, value in enumerate(fruits):
    print(index, value)
# 0 apple
# 1 banana
# 2 grape
# 3 cheery
# 4 mango
# 5 pineapple

#Nested For Loop
for x in range(1,4):
    for y in range (1,4):
        print(x,y)
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

adj = ['red', 'big', 'tasty']
more_fruit = ['apple', 'banana', 'cherry']
for x in adj:
    for y in more_fruit:
        print(x,y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

for num1 in range(2):
    for num2 in range(5, 10):
        print(num1, ",", num2)
# 0 , 5
# 0 , 6
# 0 , 7
# 0 , 8
# 0 , 9
# 1 , 5
# 1 , 6
# 1 , 7
# 1 , 8
# 1 , 9


#break
for x in fruits:
    print(x)
    if x == 'mango':
        break

#nested loop with a break
for x in range (1,4):
    for y in range(1,4):
        print(x,y)
        if x ==2 and y == 2:
            break
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 3 1
# 3 2
# 3 3

#continue: rejects all remaining statements in the current iteration of the loop and moves the control back to the top of the loop
i = 0
while i <= 10:
    i += 1
    if i ==5:
        continue
    print(i)
# 1
# 2
# 3
# 4
# 6 <--- skiped 5
# 7
# 8
# 9
# 10
# 11  


for num in numberList:
    if num % 2 != 0:
        continue
    print(num)
# 2
# 4
# 6
# 8

#Strings - triple quotes used for formating

#slice
string = "this is my python string"
print(string[:]) # this is my python string
print(string[11:]) # python string
print(string[:11]) # this is my

#How to update a string
str1 = 'hello, my name is Chelsea'
str1 += ' Merrill'
print(str1) #hello, my name is Chelsea Merrill (memory allocation changed)

#how to delete
str2 = 'second string'
del str2 #is not deleted

#anding string to itself
print(str1 * 3) 
#hello, my name is Chelsea Merrillhello, my name is Chelsea Merrillhello, my name is Chelsea Merrill

#ord() : returns the ASCII of the character
ch = 'b'
print(ord(ch)) #98

#chr(): returns charcter represented by ASCII number
print(chr(65)) #A
print(chr(97)) #a

print ('PYTHION' == 'python') #False
print ('PYTHION' < 'python')  #True (based on ASCII values)

print('my' in string) #True

#str(): removes whitespace from the begining
whiteString = "      test"
print(whiteString)
print(whiteString.strip())
#       test
# test

#len(): length
#lower(): lowercase  / islower(): boolean if it is lowercase 
#upper(): uppercase / isupper(): boolean if it is upper 
#isalpha() : checks if all characters are alphabetical letters
#isdigit(): checks to see if it is all numbers
#isalnum(): checks in string is alphanumberic
#join(): concatenates
#split(): breaks up string at a specified location
#replace(): replaces -> new copy
#find(): returns the first occurance of event 
#startswith()
#endswith()

#sorted: sorts and returns a list
messy_String = 'hawiqef'
print(sorted(messy_String)) #['a', 'e', 'f', 'h', 'i', 'q', 'w']

#count(): counts number of times something occurs
new_string = 'how many times is many in here?'
print(new_string.count('many')) #2


#List are mutable and Tuplet is imutable 
list1 = ['python', 'java', 'c']
del list1[2]
print(list1) # [''python', 'java']
# del list1
print(list1) #all items are deleted

#concatenate lisrs: use + 
#Length: len()
#Repetion: print(list*7)
#Membership : in operator and not in, returns boolen
#smallest in list: min()
#largest in list: max()
#sum(): sum of all numbers in the list
#Append: adds element to end of list
    # list.append('value')
#Extend: appends all elements from on list to another list and returns none
    #list1.extends(lists)
#insert: adds element based on index
    # list.insert(index, value you are inserting)
#remove: list.remove(value) (only removes first occurance of the value)
#pop: removes at a given index or the last ---> a =list.pop() and b=list.pop(2)
#count()
#reverse()
#sort() : for decending order do list.sort(reverse=True)
#split()

#List Comprehension :concise way to create a new lists
cube = [i**3 for i in range(10)]
print(cube) #[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

even= [x for x in range(20) if x % 2 == 0]
print(even) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#Tuples: a collection which is ordered and unchangeble. similar to lists but the cannot be changed. Uses parenthesis instead of squar brackets
tuple1 = (1,2,3)

#creating a tuple from a string
tuple2 = tuple(("python"))
print(tuple2) #('p', 'y', 't', 'h', 'o', 'n')

tuple3= tuple({1: 'chelsea', 2: 'josh'})
print(tuple3) #(1,2)

#benefits of using tuples over list: when you dont want to change value 



