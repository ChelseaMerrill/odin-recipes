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
h, i = 10, 10
print(id(h))
print(id(i))
print(h is i) #True
print(h is not i) #False

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