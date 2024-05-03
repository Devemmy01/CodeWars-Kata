""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def solution(number):
    if number < 0:
        return 0
    else:
        return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

# OR

def solution(number):
    # Return 0 for negative numbers
    if number < 0:
        return 0
    
    sum = 0
    
    for i in range(number):
        # Check if the number is a multiple of 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            sum += i  # Add the multiple itself to the sum
            
    return sum

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
For example,
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def count_sheeps(sheep):
    return sheep.count(True)

# OR

def count_sheeps(sheep):
    return sum(sheep)

"""
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.
You receive an array with your peers' test scores. Now calculate the average and compare your score!
Return true if you're better, else false!
Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def better_than_average(class_points, your_points):
# Return true if my point is greater than the sum of class points divided by the length
    return your_points > sum(class_points) / len(class_points) 

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""

def maskify(cc: str) -> str:
    """
    Masks all but the last four characters of a string with '#'.
    Args:
        cc (str): The input string (e.g., credit card number).
    Returns:
        str: The masked string.
    """
    return '#' * (len(cc) - 4) + cc[-4:]

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
    
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def positive_sum(arr):
    sum_of_positive = 0
    for i in arr:
        if i > 0:
            sum_of_positive += i
    return sum_of_positive

# OR

def positive_sum(arr):
    return sum(i for i in arr if i > 0)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Make a simple function called greet that returns the most-famous "hello world!".   
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def greet():
    return "hello world!"

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def is_pangram(s):
    alphabets = ('abcdefghijklmnopqrstuvwxyz')
    s_lower = s.lower()
    for i in alphabets:
        if i not in s_lower:
            return False
    return True

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0. Your function only needs to return the result, what is shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def summation(num):
    return sum(range(1, num + 1))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def longest(a1, a2):
    add = set(a1 + a2)
    sorted_string = ''.join(sorted(add))
    return sorted_string

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def count_bits(n):
    return bin(n).count('1')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def is_isogram(string):
    # Convert the string to lowercase to ignore letter case
    lower_case_string = string.lower()
    # Create a set to store the unique letters encountered
    unique_letters = set()
    # Iterate through each character in the lowercase string
    for _ in lower_case_string:
        # Check if the character is a letter
        if _.isalpha():
            # If the character is already in the set, return False
            if _ in unique_letters:
                return False
            # Otherwise, add the character to the set
            else:
                unique_letters.add(_)
    return True

# OR

def is_isogram(string):
    return len(string) == len(set(string.lower()))

# OR

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def solution(text, ending):
    return text.endswith(ending)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""

"""