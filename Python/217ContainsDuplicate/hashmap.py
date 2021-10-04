'''
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        knum = {}
        for x in nums:
            if x not in knum:
                knum[x] = 1
            else:
                return True
        return False