# Coded by Shalu Ambasta :)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[0]
        
        slow = nums[slow]
        fast = nums[nums[fast]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        start = nums[0]
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return slow
        