'''
198. House Robber - 
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
'''
'''
Approach - 
Use Dp. if we choose to rob house 1 then we cant rob house 2
for house 3, we can either have robbbed house 2 or house 1 + house 3
we calculate rob1, and rob2 for each house
and then we get the maximum and return rob2, as rob 2 got updated as the max in last iteration
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
'''
Runtime: 28 ms, faster than 85.31% of Python3 online submissions for House Robber.
Memory Usage: 14.2 MB, less than 77.71% of Python3 online submissions for House Robber.
Time - O(n), Space - O(1)
'''