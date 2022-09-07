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
