# Coded by Shalu Ambasta :)

class Solution:
    def reverse(self, nums, start, stop):
        size = stop + start
        for i in range(start, (size + 1) // 2):
            nums[i], nums[size - i] = nums[size - i], nums[i]
    
    def nextPermutation(self, nums: List[int]) -> None:
        ind = -1
        # find breakpoint from back
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i     # breakpoint found
                break
        if ind == -1:   # no breakpoint found
            nums.reverse()  # in-place
            # nums[:] = nums[::-1] # also works but is not in-place
        else:
            for i in range(len(nums)-1, ind, -1):
                if nums[i] > nums[ind]:
                    nums[i], nums[ind] = nums[ind], nums[i]
                    break
            
            # reverse list elements on the right of breakpoint
            self.reverse(nums, ind+1, len(nums)-1) # in-place
            # nums[ind+1:] = nums[ind+1:][::-1] # also works but is not in-place
            