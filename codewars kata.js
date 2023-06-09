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

// Given an array of ones and zeroes, convert the equivalent binary value to an integer.
// Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

// Examples:

// Testing: [0, 0, 0, 1] ==> 1
// Testing: [0, 0, 1, 0] ==> 2
// Testing: [0, 1, 0, 1] ==> 5
// Testing: [1, 0, 0, 1] ==> 9
// Testing: [0, 0, 1, 0] ==> 2
// Testing: [0, 1, 1, 0] ==> 6
// Testing: [1, 1, 1, 1] ==> 15
// Testing: [1, 0, 1, 1] ==> 11
// However, the arrays can have varying lengths, not just limited to 4.

const binaryArrayToNumber = arr => parseInt(arr.join(''), 2)

//////////////////////////////////////////////////

// Write a javascript program to create a new string from a given string
// taking the first 3 characters and the last 3 characters of a string and 
// adding them together. The string length must be 3 or more, if Notification, the 
// original string is returned.

const newString = (str) => str.length < 3 ? str : str.slice(0, 3) + str.slice(-3)

//////////////////////////////////////////////////

// Write a javascript program to extract the first half of a string 
// of even length 

const firstHalf = (str) => str.slice(0, str.length / 2);

//////////////////////////////////////////////////

// Write a javascript program to concatenate two strings except their first Character.Character

const concatenate = (str1, str2) => str1.slice(0) + str2.slice(0);

//////////////////////////////////////////////////

// Given two values, write a javascript program to find out which one 
// is nearest to 100

const near100 = (num1, num2) => (100 - num1) < (100 - num2) ? num1 : num2;

//////////////////////////////////////////////////

// Write a javascript program that checks a given string contains 2 to 4 occurrences of a specified character.

const countChars = (str, char) => str.split('').filter(ch => ch === char).length;
const has2To4 = (str, char) => countChars(str, char) >= 2 && countChars(str, char) <= 4;