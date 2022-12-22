# https://www.codewars.com/kata/56747fd5cb988479af000028 
# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
def get_middle(s):
    middle = len(s) / 2
    if len(s) % 2 == 0:
        s1 = slice(int(middle - 1), int(middle + 1))
        return s[s1]
    else:
        return s[int(middle)]

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b 
import math
def declare_winner(fighter1, fighter2, first_attacker):
    fighter1roundsalive = math.ceil(fighter1.health/fighter2.damage_per_attack)
    fighter2roundsalive = math.ceil(fighter2.health/fighter1.damage_per_attack)
    if fighter1roundsalive == fighter2roundsalive:
        return first_attacker
    else:
        return fighter1.name if fighter1roundsalive > fighter2roundsalive else fighter2.name


# https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python
# If　a = 1, b = 2, c = 3 ... z = 26
# Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
def words_to_marks(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)


# https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5
# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
def reverse_number(num):
    num_string = str(num)
    if num_string[0] != '-':
        rev = num_string[::-1]
        return int(rev)
    else:
        num_num = int(num_string) * -1
        num_string2 = str(num_num)
        rev = num_string2[::-1]
        return int(rev) * -1

def reverseNumber(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return int(str(n).strip('-')[::-1])*-1


# https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce
# Write a small function that returns the values of an array that are not odd.
# All values in the array will be integers. Return the good values in the order they are given.
def no_odds(values):
    value = []
    for i in values:
        if i % 2 != 1:
            value.append(i)
    return value

def no_odds(values):
    return [i for i in values if i % 2 == 0]


# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
def invert(lst):
    return [i*-1 for i in lst]


# https://www.codewars.com/kata/56f69d9f9400f508fb000ba7 
# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just 
# appreciate the full number, he has to start counting them from 1. As a good parent, you will sit and count with him. Given the number (n), 
# populate an array with all numbers up to and including that number, but excluding zero.
def monkey_count(n):
    return [*range(1,n +1,1)]


# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039 
# This time no story, no theory. The examples below show you how to write function accum
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
# enumerate adds to a constant


# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need 
# to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning 
# or the end of the sentence!
def smash(words):
    return" ".join(words); 


# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/python
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
def count_sheep(n):
    sheep = ''
    for i in range(n):
        sheep+=f"{i+1} sheep..."
    return sheep

# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has 
# an even number of petals and the other has an odd number of petals it means they are in love. Write a function that will take the number of 
# petals of each flower and return true if they are in love and false if they aren't.
def lovefunc( flower1, flower2 ):
    if (flower1 + flower2) % 2 != 1:
        return False
    else:
        return True