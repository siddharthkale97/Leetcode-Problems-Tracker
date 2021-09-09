class solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pmap = {}
        for i,x in enumerate(nums):
            if (target - x) in pmap:
                return[pmap[target - x], i]
            pmap[x] = i
        return