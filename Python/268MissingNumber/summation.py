'''
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for i in range(0,len(nums)):
            sum1 += nums[i]
            sum2 += i
        sum2 += i + 1
        
        return sum2 - sum1

'''
Runtime: 216 ms, faster than 23.49% of Python3 online submissions for Missing Number.
Memory Usage: 15.4 MB, less than 48.04% of Python3 online submissions for Missing Number.
'''