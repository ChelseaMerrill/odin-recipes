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
