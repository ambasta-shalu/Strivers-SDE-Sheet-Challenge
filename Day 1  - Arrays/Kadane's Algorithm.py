# Coded by Shalu Ambasta :)
# Kadane's Algorithm 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = -sys.maxsize - 1
        temp = 0

        for i in range(len(nums)):
            temp += nums[i]
            ans = max(ans, temp)
            if temp < 0:
                temp = 0

        return ans
        