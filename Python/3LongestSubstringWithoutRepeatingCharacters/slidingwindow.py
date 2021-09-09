class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        curr = set()
        for i in range(len(s)):
            while(s[i] in curr):
                curr.remove(s[l])
                l += 1
            curr.add(s[i]) 
            count = max(count,len(curr))
        return count