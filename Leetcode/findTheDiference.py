"""
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
"""
def findTheDifference(s, t):
    add_letter = ""
    for i in t:
        if t.count(i) != s.count(i):
            add_letter = str(i)
    print(add_letter)
    return add_letter

findTheDifference("","y")