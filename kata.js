// Can you find the needle in the haystack?
// Write a function findNeedle() that takes an array full of junk but containing one "needle"
// After your function finds the needle it should return a message (as a string) that says:
// "found the needle at position " plus the index it found the needle, so:
// Example(Input --> Output) ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

// ANSWER
function findNeedle(haystack) {
  for (var i of haystack){
    return "found the needle at position " + haystack.indexOf("needle");
  }
}

//////////////////////////////////////////////////////


/* Create a function finalGrade, which calculates the final grade of a student depending on two parameters:
 a grade for the exam and a number of completed projects.
 This function should take two arguments: exam - grade for exam (from 0 to 100); projects - 
 number of completed projects (from 0 and above);
This function should return a number (final grade). There are four types of final grades:
100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
0, in other cases
Examples(Inputs-->Output):

// 100, 12 --> 100
// 99, 0 --> 100
// 10, 15 --> 100
// 85, 5 --> 90
// 55, 3 --> 75
// 55, 0 --> 0
// 20, 2 --> 0 */

// ANSWER

function finalGrade (exam, projects) {
    return (
      exam > 90 || projects > 10 ? 100 :
      exam > 75 && projects >= 7 ? 90 :
      exam > 50  && projects >= 2 ? 75: 0
    )
}

//////////////////////////////////////////////////////

// Given an array of integers, return a new array with each value doubled.

// For example:

// [1, 2, 3] --> [2, 4, 6]

//  ANswer

function maps(x){
    let newArray = [];
    for(let i = 0; i < x.length; i++){
        newArray.push(x[i] * 2);
    }
    return newArray;
}

//////////////////////////////////////////////////////

// Return the number (count) of vowels in the given string.

// We will consider a, e, i, o, u as vowels for this Kata (but not y).

// The input string will only consist of lower case letters and/or spaces.

function getCount(str) {
    let vowelCount = 0;
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    for(let i of str){
      if(vowels.includes(i)){
        vowelCount++
      }
    }
    return vowelCount;
}

///////////////////////////////////////////////////////

// Given a set of numbers, return the additive inverse of each. Each positive becomes 
// negatives, and the negatives become positives.

// invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
// invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
// invert([]) == []
// You can assume that all values are integers. Do not mutate the input array/list.

function invert(array) {
  array.forEach((n, index) => {
      array[index] *= -1;
   });
  return array;
};

//////////////////////////////////////////////////////

// A hero is on his way to the castle to complete his mission. However, he's been told 
// that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 
// bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming 
// he's gonna grab a specific given number of bullets and move forward to fight another specific 
// given number of dragons, will he survive?

// Return True if yes, False otherwise :) 

function hero(bullets, dragons){
	return bullets >= dragons * 2 ? true : false
}

////////////////////////////////////////////////////

// Your function takes two arguments:

// current father's age (years)
// current age of his son (years)
// Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). 
// The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

function twiceAsOld(dadYearsOld, sonYearsOld) {
  let twice = dadYearsOld - sonYearsOld * 2;
  return twice < 0 ? twice * (-1) : twice;
}

//////////////////////////////////////////////////

// Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

// The binary number returned should be a string.

// Examples:(Input1, Input2 --> Output (explanation)))

// 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
// 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in

function addBinary(a,b) {
  return (a + b).toString(2)
}

//////////////////////////////////////////////////

// You ask a small girl,"How old are you?" She always says, "x years old", where x is a random number between 0 and 9.

// Write a program that returns the girl's age (0-9) as an integer.

// Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

function getAge(inputString){
	return parseInt(inputString)
}

//////////////////////////////////////////////////

/*
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
However, the arrays can have varying lengths, not just limited to 4. */

const binaryArrayToNumber = arr => parseInt(arr.join(''), 2)

//////////////////////////////////////////////////

/* 
Write a javascript program to create a new string from a given string
taking the first 3 characters and the last 3 characters of a string and 
adding them together. The string length must be 3 or more, if Notification, the 
original string is returned. */

const newString = (str) => str.length < 3 ? str : str.slice(0, 3) + str.slice(-3)

//////////////////////////////////////////////////

// Write a javascript program to extract the first half of a string of even length 

const firstHalf = (str) => str.slice(0, str.length / 2);

//////////////////////////////////////////////////

// Write a javascript program to concatenate two strings except their first Character.Character

const concatenate = (str1, str2) => str1.slice(0) + str2.slice(0);

//////////////////////////////////////////////////

// Given two values, write a javascript program to find out which one is nearest to 100

const near100 = (num1, num2) => (100 - num1) < (100 - num2) ? num1 : num2;

//////////////////////////////////////////////////

// Write a javascript program that checks a given string contains 2 to 4 occurrences of a specified character.

const countChars = (str, char) => str.split('').filter(ch => ch === char).length;
const has2To4 = (str, char) => countChars(str, char) >= 2 && countChars(str, char) <= 4;

//////////////////////////////////////////////////

/*
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square */

function findNextSquare(sq){
  if(Math.sqrt(sq) % 1 == 0){
    return (Math.sqrt(sq)+1)**2
  } else{
    return -1
  }
}
                            // OR

const findNextSquare = (sq) => Math.sqrt(sq) % 1 == 0 ? (Math.sqrt(sq) + 1)**2 : -1


///////////////////////////////////

/*

Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

*/

function duplicateCount(text){
  const lowerCase = text.toLowerCase();
  const char = {};
  
  for (var strings of lowerCase) {
    if (/[a-z0-9]/.test(strings)) {
      char[strings] = (char[strings] || 0) + 1;
    }
  }
  const countChars = Object.values(char).filter(count => count > 1).length;
  
  return countChars;
}

/*  You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.

*/

function likes(names) {
  names = names || [];
  switch(names.length){
      case 0: return 'no one likes this'; break;
      case 1: return names[0] + ' likes this'; break;
      case 2: return names[0] + ' and ' + names[1] + ' like this'; break;
      case 3: return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'; break;
      default: return names[0] + ', ' + names[1] + ' and ' + (names.length - 2 ) + ' others like this';
  }
}

//////////////////////////////////////////

/*

A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false

*/

const isSquare = (n) => {
  // If the square root of the number is an integer, it's a perfect square
  return Math.sqrt(n) % 1 === 0
}


/*

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

*/
// Function to sort words based on the position number in the string
function order(words) {
  // I check if the input string is empty
  if (words === "") {
    return "";
  }
  
  // I split the string into an array of words
  const wordArr = words.split(" ");
  // I create an empty array to store the result
  const sortedArr = [];
  
  // I iterate through numbers from 1 to 9
  for (let i = 1; i <= 9; i++) {
    // I iterate through each word in the array
    for (let j = 0; j < wordArr.length; j++) {
      // Then check if the word contains the current number
      if (wordArr[j].includes(i)) {
        // Add the word to the sorted array
        sortedArr.push(wordArr[j]);
      }
    }
  }
  
  // Then finally Join the sorted array of words into a string
  return sortedArr.join(" ");
}


/*
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

*/

function toCamelCase(str){
  if (!text) return "";

  // Check if the first character is uppercase
  const isFirstWordUpper = text[0].toUpperCase() === text[0];

  // Convert first word (lowercase if necessary)
  const firstWord = isFirstWordUpper ? text[0] : text[0].toLowerCase();

  // Replace delimiters and capitalize following characters in remaining words
  const remainingWords = text.slice(1).replace(/[-_](.)/g, (match, group1) => group1.toUpperCase());

  // Combine the first word and converted remaining words
  return firstWord + remainingWords;
}

/*
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
*/

function booleanToString(b){
  return b.toString()
}

/*
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
*/

function friend(friends){
  return friends.filter((i) => i.length == 4)
}

/*
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
*/

function getAverage(marks){
  if (!marks.length) return null
  
  const totalSum = marks.reduce((sum, num) => sum + num , 0)
  
  const average = Math.floor(totalSum / marks.length)
  
  return average
}

/*
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
*/

function repeatStr (n, s) {
  if (n < 0 || !s) return ""
  
  if (n === 0) return ""
  
  return s + repeatStr(n - 1, s)
}

// OR

function repeatStr (n, s) {
  return s.repeat(n);
}

// OR

repeatStr = (n, s) => s.repeat(n)

/*
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) === [2,4,6,8,10]
*/

function countBy(x, n) {
  let z = [];
  for (let i = 1; i <= n; i++ ){
    z.push(x * i)
  }

  return z;
}

/*
Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
*/

function opposite(number) {
  return -number
}

/*
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
*/

function arrayPlusArray(arr1, arr2) {
  
  const spread = [...arr1, ...arr2]
  
  const sum = spread.reduce((acc, num) => acc + num , 0)
  
  return sum; 
}

// OR

function arrayPlusArray(arr1, arr2) {
  return arr1.concat(arr2).reduce((acc, cur) => acc + cur);
}

/*
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
*/

function sum (numbers) {
  let sum = 0
  for (let i = 0; i < numbers.length; i++){
    sum += numbers[i]
  }
return sum
};

