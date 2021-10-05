'''
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
'''
Approach - 
Use Dp. if we choose to rob house 1 then we cant rob house 2
for house 3, we can either have robbbed house 2 or house 1 + house 3
we calculate rob1, and rob2 for each house
and then we get the maximum and return rob2, as rob 2 got updated as the max in last iteration
We use dp two time here, once for 0 to n - 1 and for 1 to n
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            return max(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        def dp(knums):
            r1, r2 = 0,0
            for x in knums:
                #print(r1,r2,x)
                temp = max(r1 + x, r2)
                r1 = r2
                r2 = temp
            #print(r2)
            return r2
        a1 = dp(nums[0:len(nums) - 1])
        a2 = dp(nums[1:len(nums)])
        return max(a1, a2)

'''
Runtime: 28 ms, faster than 89.13% of Python3 online submissions for House Robber II.
Memory Usage: 14.3 MB, less than 23.64% of Python3 online submissions for House Robber II.
Time - O(n), Space - O(1)
'''