'''
76. Minimum Window Substring -
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character 
in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.
'''
'''
Approach -
Use sliding window and hashmaps - create for both window and t string (initialize)
2 variable have and need = length(t)
add incease character count in window for each character in s
if character count <= need, have ++
when have == need, remove character from left of window and decrease have
if chracter count is below the corresponding value in map of t
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t=="":
            return ""
        tmap = {}
        windowmap = {}
        
        for x in t:
            if x not in tmap:
                tmap[x] = 1
            else:
                tmap[x] += 1
        start = 0
        need, have = len(t), 0
        l,r = 0,0
        minlen = float("inf")
        for i in range(len(s)):
            if s[i] in windowmap:
                windowmap[s[i]] +=  1
            else:
                windowmap[s[i]] =  1
            if s[i] in tmap and windowmap[s[i]] <= tmap[s[i]]:
                have += 1
            while (have == need):
                if (i-start+1<minlen):
                    minlen = i-start+1
                    l = start
                    r = i
                windowmap[s[start]] -= 1
                
                if s[start] in tmap and windowmap[s[start]]< tmap[s[start]]:
                    have -= 1
                start += 1
        if minlen != float("inf"):
            return s[l:r+1]
        return ""
'''
Runtime: 88 ms, faster than 94.13% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.9 MB, less than 30.00% of Python3 online submissions for Minimum Window Substring.
Time - O(n+m), Space - O (n+m)
'''