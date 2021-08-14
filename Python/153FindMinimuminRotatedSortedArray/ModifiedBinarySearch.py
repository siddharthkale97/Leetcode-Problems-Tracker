'''
153. Find Minimum in Rotated Sorted Array -
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''
'''
Approach -
Use a modified Binary search, check if l>r, if not break
if l<r, array is sorted, return left most ele
if not, find mid, if mid is min, set res to mid
check if left array is sorted, if yes check right 
if not check left. Finally return res
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        def binarysearch(l,r,res):
            if l >r: # check to see integrity
                return res
            if nums[l] < nums[r]: # if sorted return left
                return min(res,nums[l])
            mid = (l + r)//2 
            res = min(res,nums[mid]) # if mid min, set res = mid
            if nums[mid] >= nums[l]: # if left sorted
                 res = min(res,binarysearch(mid+1,r,res)) # check right
            else:
                res = min(res,binarysearch(l,mid-1,res)) # else check left
            return res
        return binarysearch(0,len(nums)-1,res)
'''
Runtime: 36 ms, faster than 87.42% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Memory Usage: 14.9 MB, less than 29.41% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
Time - O(logn), Space - O(1)
'''