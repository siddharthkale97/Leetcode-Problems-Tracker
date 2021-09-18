def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #print(len(nums))
        if len(nums) == 0:
            return 0
        mergeSort(nums)
        len_ = 1
        max_ = 0
        last = nums[0]
        print(nums)
        for i in nums:
            print(len_)
            if i == last+1:
                len_ += 1
                if len_>max_:
                    max_ = len_
                last = i
            elif i == last:
                if len_>max_:
                    max_ = len_
                last = i
            else:
                len_ = 1
                last = i
        return max_