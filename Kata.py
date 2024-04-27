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