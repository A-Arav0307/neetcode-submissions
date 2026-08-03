class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[1]

        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

        return slow