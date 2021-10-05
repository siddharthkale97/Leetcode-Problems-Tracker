'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        a = [0] * 26
        b = [0] * 26
        
        for i in range(len(s)):
            temp1 = ord(s[i]) - ord("a")
            a[temp1] += 1
            temp2 = ord(t[i]) - ord("a")
            b[temp2] += 1
        if a==b:
            return True
        return False
'''
Runtime: 87 ms, faster than 12.63% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.6 MB, less than 32.25% of Python3 online submissions for Valid Anagram.
'''