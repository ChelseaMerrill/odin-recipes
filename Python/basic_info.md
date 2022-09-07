## **Day 1:**
Know which Python version you are using. Python 2 vs Python 3. You should never start a new project in Python 2 as it's no longer supported. You can check python version with the command python --version or force the use of Python 3 by using the command python3 over python , for example: python3 script.py

## **Day 2:**
Use the Python PEP-8 style guide. There are a lot of "rules"  but the most important to remember involve whitespace, naming and expressions.
### Whitespace:
- Prefer spaces over tabs
- 4 spaces is a syntactically significant indent
- Lines should be shorter than 79 characters
### Naming:
- Functions, variables and attributes should be in lowercase_underscore format (ex. my_function() over myFunction() )
- Protected functions have one proceeding underscore like _my_protected_function and private functions have two proceeding underscores __my_private_function
- Constants should be in ALL_CAPS format (ex. DB_PASSWORD)
### Expressions:
- Use inline negation if a is not b over if not a is b . Should read like english as much as possible
- Don't check empty values like if len(my_list) == 0: , instead, use the truthyness of variables such that empty lists evaluate to false if my_list:
### You can also get VSCode extensions to run PEP-8 formatting or command line packages that auto format all of your files so you never have to memorize all of the rules. (edited) 

## **Day 3:**
Know the difference between bytes, str.
In Python 3, there are two types that represent character sequences, bytes and str. Bytes contain raw 8-bit characters, str contain unicode characters. The two modes are not compatible with operators like + or >.
Most of the time you will operate with str, but if you need to convert, you can write helper functions to switch between the two.
When reading or writing to files, it is important to know that the default mode is str with UTF-8 encoding. To switch to binary (byte) mode, you can open the file with rb and wb over r and w respectively.

## **Day 4:**
Write helper functions instead of complex expressions.
A general programming tip. However, Python's useful built in functions make it very easy to write really complex single lines of code. While cool, it's best practice to move them to helper functions or expand code into multiple lines.

## **Day 5:**
Know how to slice sequences.
Python 3 allows for easy bracket notation sequence slicing. It can be used on built-in types list, str and bytes. It can also be used on any class that implements special methods __getitem__ and __setitem__ which we will discuss on Day 28 (will Chris remember to link back to this? :thinking_face:).
The syntax is mylist[ start : end ] where start is inclusive and end is exclusive. Examples:
```
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

mylist[0:5]             # ['a', 'b', 'c', 'd', 'e']
mylist[1:3]             # ['b', 'c']
mylist[5:len(mylist)]   # ['f', 'g', 'h']
```
When slicing from the beginning or the end, you can leave off the start or end index respectively!
```
mylist[:5] == mylist[0:5]
mylist[5:] == mylist[5:len(mylist)]
```
You can also use negative values:
```
mylist[2:-1]            # ['c', 'd', 'e', 'f', 'g']
mylist[-3:-1]           # ['f', 'g']
```

Negative values work such that mylist[:5] returns the first 5 items and mylist[-5:] returns the last 5 items!
The result of a slice creates a new list so modifications made on a slice won't change the original list.
Lastly, when assigning, a slice will replace the range in the original list. The list will resize to match:
```
mylist[1:6] = ["HI", "JG!"]
print(mylist)           # ['a', 'HI', 'JG!', 'g', 'h']
```

## **Day 6:**
Using strides in your slices.
The slices discussed on day 5 also allow for a stride argument with the following syntax my_list[ start : end : stride ]. The stride allows you to only take every nth item with slicing. For example, you can get every odd and even index in a list.
```
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

odds = my_list[::2]         # ['a', 'c', 'e', 'g']
evens = my_list[1::2]       # ['b', 'd', 'f', 'h']
```
Personally, I use this most to quickly reverse lists, since strides allow negative arguments:
```
reversed = my_list[::-1]    # ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
```
Try not to use all three arguments (start, end, stride) in a single slice. It can lead to confusing behavior and code. Try splitting the slice into two lines to make it more clear.

### POP QUIZ 
Give this kata a try using Python slicing: https://www.codewars.com/kata/586ec0b8d098206cce001141
Jarrin Dahnel was exploring the Amazon (Web Services) rainforest and stumbled across an ancient temple to the Python gods. Inside, he found a riddle. Help him solve it using Python string slicing!
What did the Python gods forget when creating their language?
```
riddle = 'ymclripovxzxlhqiwodmgjneudksbf'

# Every 4th letter from 16 to 28, reversed
# Every 5th letter starting at the second
```
(You can use an online Python editor for quick testing)

## **Day 7:**
Use list comprehension over map and filter.
List comprehensions in Python allow you to create one list from another by applying some logic. For example, you can square all the items in an array using the following syntax:
```
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x**2 for x in my_list]

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
```
This arguably easier to read than using the map function which requires implementing a lambda function:
```
squares = map(lambda x: x ** 2, my_list)
```
You can also filter items using list comprehension. Say you only wanted to find the even squares in a list:
```
even_squares = [x**2 for x in my_list if x % 2 == 0]

print(even_squares)  # [4, 16, 36, 64]
```
The above example is much easier to read than using the map and filter functions seen below. In fact, the example almost reads like English “x squared for x in my_list where x mod 2 is 0”
```
even_squares = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, my_list))
```
Python also allows for comprehension of dict and set types. See the example below where I swap the key and value in a dictionary:
```
pop_quiz_scores = {"Mike T.": 100, "Ryan L.": 99, "Everyone Else": 0}
swapped = {score: name for name, score in pop_quiz_scores.items()}

print(swapped)  # {100: 'Mike T.', 99: 'Ryan L.', 0: 'Everyone Else'}
```

## **Day 8:**
Avoid nested expressions in list comprehensions.
The author appears to be trying to pad his numbers at this point… Essentially nested list comprehensions, while useful in code golf, are difficult to read. You should leverage for loops over nested list comprehensions when dealing with nested lists.

## **Day 9:**
Consider generator expressions for large comprehensions.
List comprehensions create an entire new list for every item in the original list. This can be a problem when the input is a REALLY large list or an open network stream. An example would be a list comprehension over the lines of a file. There are no issues with a small file, but a large file could cause the program to run out of memory.
In this example, list comprehensions are used to get the number of characters in each line of an input file:
```
lengths = [len(x) for x in open('my_file.txt')]
print(lengths) # 100, 57, 15, 1, 12
```
To prevent potential issues, we can use generator expressions, which are a combination of list comprehension and generators. They don’t materialize the entire result list, instead, they return an iterator that yields one item at a time. Here is an example of using a generator to complete the same task from above:
```
lengths_itr = (len(x) for x in open('my_file.txt'))
print(next(lengths_itr)) # 100
print(next(lengths_itr)) # 57
```
As you can see, the syntax is very similar, generators just use parentheses over square or curly brackets, without storing everything in memory. Consider them if you need to quickly execute a large comprehension!

## **Day 10:**
Prefer enumerate over range.
This is honestly my favorite part of Python… writing for loops is really easy. In Python, for loops look like:
```
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(len(my_list)):
	print(my_list[i])    # a b c d e f g h
```
Python makes it even easier though, just do:
```
for item in my_list:
	print(item)    # a b c d e f g h
```
But what if you want the index of item at any point in the loop? You could use range, but instead, opt to use enumerate! Enumerate uses a generator (similar to day 9 :wink:) that yields a pair containing the index and value of the next item to the loop:
```
for i, item in enumerate(my_list):
	print(i, item)    # 0,a 1,b 2,c 3,d 4,e 5,f 6,g 7,h 
```
You can even tell enumerate what number you’d like to start counting at so no pesky i+1 required when printing out an index in a list:
```
for i, item in enumerate(my_list, 1):
	print(i, item)    # 1,a 2,b 3,c 4,d 5,e 6,f 7,g 8,h
```

## **Day 11:**
Use zip to process iterators in parallel.
Say we generate two lists:
```
names = ['Givney', 'Pence', 'Treiling']
letters = [len(n) for n in names]   # [6, 5, 8]
```
Now, we can find the longest name by looping over both lists, whose items are related since we made them in a list comprehension (I know this is a horrible example practically, but it does illustrate the point. Plus, 
@Matt Givney
 and I have used the zip function before, it’s useful):
 ```
longest_name = None
max_letters = 0

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
```
The safer, and cleaner way to write this is using zip. The function uses a generator (similar to day 9 again) that returns a tuple containing the next elements in the lists provided.
```
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
```
Now, I know you all write perfect code… but if you happen to give zip two or more lists of different lengths, zip will continue until the shortest list is exhausted.
```
short_list = ['a', 'b']
long_list = [1, 2, 3, 4]

for char, num in zip(short_list, long_list):
    print(char, num)

# a 1
# b 2
```
If you want zip to continue until the longest list is exhausted, use zip_longest in the built-in itertools package.
from itertools import zip_longest
```
for char, num in zip_longest(short_list, long_list):
    print(char, num)

# a 1
# b 2
# None 3
# None 4
```
For those new to Python, None is Python's version of null from languages like Java or JavaScript

## **Day 12:**
Avoid else blocks after for and while loops.
Python has a unique feature not available to most energy-efficient languages. You can put an else block after a loop’s interior block:
```
for i in range(2):
    print(f"Loop {i}")
else:
    print("Else!")

# Loop 0
# Loop 1
# Else!
```
Now, you might assume that the else block would run if the loop wasn’t completed. You’d be wrong… It does the opposite. In fact, the else block will be skipped if you call break inside the loop.
```
for i in range(2):
    print(f"Loop {i}")
    if i == 1:
        break
else:
    print("Else!")

# Loop 0
# Loop 1
```
Because they are rather unintuitive, the book recommends not using the else feature of loops. I didn't know about them until the book mentioned them and now I want to use them... so mission un-accomplished

## **Day 13:**
Take advantage of each block in try, except, else, finally.
Exception handling in Python is fairly similar to other languages. You can play with the basic functionality and syntax of try and except here. Right now, we will focus on the more obscure elements else and finally.
Else:
Used to make it clear which exceptions will be handled by your code and which ones will propagate up. You can use the else block to minimize the amount of code in the try block. Here is an example of loading a JSON object from a string:
```
def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
            raise KeyError from e       # May raise KeyError
    else:
        return result_dict[key]
```
In this code, a KeyError raised in the else clause will propagate up.
Finally:
Essentially clean up code. Will always run, even when exceptions occur. You can see an example of using this to ensure a file connection is closed if an error occurs while reading.
```
file = open('file.txt') # May raise IOError
try:
    data = file.read()  # May raise UnicodeDecodeError
finally:
    file.close()        # Always runs
```

## **Day 14:**
Prefer exceptions to returning None.
Sometimes, it makes sense to return None from a function, but most of the time, prefer not to. Let’s use the example of a function that divides two numbers:
```
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```
There are a few ways we can handle this. The first is to leave it as is.
```
result = divide(5,0)
if result is None:
    print("Invalid inputs")
```
The next solution is to return a tuple, defining whether the inputs were valid or not, along with returning None. This solution is not ideal as someone can easily ignore the first argument and continue operating with a None value.
```
def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

success, result = divide(5,0)
if not success:
    print("Invalid inputs")
```
Lastly, we can return the exception and force the caller to decide what they want to do:
```
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs') from e

try:
    result = divide(5,2)
except ValueError:
    print('Invalid Inputs')
else:
    print(f"Result is {result}")
```
Prefer the final solution (in combination with good documentation) over the first two.

## **Day 15:**
Prefer writing your own generator functions over returning a list.
Say you want to write a function that returns a list of results. You could just return a list, or, you can return an iterator in what’s called a generator function. Here are the pros and cons of generator functions:
### Pros:
-The functions can be more concise.
-The entire result list does not need to be stored in memory. A generator instantly returns an iterator that only yields the next result when iterated on.
-Iterators can quickly be converted into lists if you need them in memory.
### Cons:
-Iterators are stateful, they cannot be reused.
Here is an example of a function that finds the index of every word in a list by returning another list:
```
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

text = "Four score and seven years ago..."
print(index_words(text))   #[0, 5, 11, 15, 21, 27]
```
Here is the same example, but instead we use a generator-style function:
```
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

for itr in index_words_iter(text):
    print(itr)  # 0 5 11 15 21 27
```
You can see it is much cleaner and the result list is not stored in memory, saving space for larger inputs.