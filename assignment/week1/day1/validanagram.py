# Syfur Rahman
# Date: Jan 2, 2023
# Technical interview prep Winter 2024
# Leetcode - 242 Valid Anagram 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): # check if the strings are equal if not return false
            return False
        
        # sorting both strings
        ssorted = sorted(s)
        tsorted = sorted(t)

        #compare both sorted strings
        for i in range(len(s)):
            if ssorted[i] != tsorted[i]:
                return False
        return True

        # the time complaxity would be O(n log n) since there is only one for loop which is O(n) but then it is dominated by the sorting operation which is O(n log n)


