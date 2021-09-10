class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumx = 0
        maxsum = nums[0]
        for x in nums:
            if sumx<0:
                sumx = 0
            sumx+= x
            maxsum = max(maxsum,sumx)
        return maxsum
                