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
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def row_sum_odd_numbers(n):
    # Calculate the first number of the nth row
    first_number = n * (n - 1) +1
    
    row_sum = 0
    
    for i in range(n):
        row_sum += first_number + 2 * i

    return row_sum

# OR

def row_sum_odd_numbers(n):
    return n ** 3

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def bmi(weight, height):
    
    bmi = weight / height ** 2
    
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0: 
        return "Normal"
    elif bmi <= 30.0: 
        return "Overweight"
    elif bmi > 30: 
        return "Obese"

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def number_to_string(num):
    return str(num)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def square_digits(num):
    squared_numbers = ''
    for i in str(num):
        squared_numbers += str(int(i) ** 2)
    
    result = int(squared_numbers)
    return result

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
import math
def cockroach_speed(s):
    return math.floor(s * (100000 / 3600))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def find_short(s):
    short = s.split()
    return min(len(word) for word in short)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def get_middle(s):
    length = len(s)
    middle_index = length // 2
    
    # Check if the length is odd
    if length % 2 != 0:
        return s[middle_index]
    else:
        # If even, return the middle 2 characters
        return s[middle_index - 1:middle_index + 1]
    
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# OR

def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
Sam Harris => S.H
patrick feeney => P.F
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def abbrev_name(name):
    words = name.split()
    cap_first_letters = [i[0].upper() for i in words]
    initial = '.'.join(cap_first_letters)
    return initial

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Complete the solution so that it reverses all of the words within the string passed in.

Words are separated by exactly one space and there are no leading or trailing spaces.

Example(Input --> Output):

'The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The'
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

"""
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    
def count_by(x, n):
    multiples = []
    for i in range(1, n + 1):
        multiples.append(x * i)
    return multiples
    
"""
Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
"""

def opposite(number):
    return -number

"""
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
"""

def array_plus_array(arr1,arr2):
    arr1.extend(arr2)
    return sum(arr1)

# OR

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)
    
"""
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
"""

def sum_array(a):
    if not a:
        return 0
    return sum(a)

# OR

def sum_array(a):
  return sum(a)

"""
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
"""

def make_negative( number ):
    if number > 0:
        return -number
    return number

# OR

def make_negative( number ):
    return -abs(number)

"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# OR

def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'

"""
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12
"""

def quarter_of(month):
    if month in (1, 2, 3):
        return 1
    elif month in (4, 5, 6):
        return 2
    elif month in (7, 8, 9):
        return 3
    else:
        return 4
    
"""
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0
"""

def paperwork(n, m):
    if n < 0 or m < 0: 
        return 0
    return n * m

# OR

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""

def litres(time):
    return int(time * 0.5)

# OR

def litres(time):
    return time // 2

"""
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

S
e
r
i
e
s
:
1
+
1
4
+
1
7
+
1
10
+
1
13
+
1
16
+
…
Series:1+ 
4
1
​
 + 
7
1
​
 + 
10
1
​
 + 
13
1
​
 + 
16
1
​
 +…
You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

Examples (Input --> Output)
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""

def series_sum(n):
    if n == 0:
        return "0.00"
    sum = 1
    denominator = 4
    for i in range(1, n):
        sum += 1 / denominator
        denominator += 3

    return f"{sum:.2f}"

# OR

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
