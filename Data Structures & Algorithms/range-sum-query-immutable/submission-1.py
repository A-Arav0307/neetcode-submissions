class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(num + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        val = self.prefix[right+1] - self.prefix[left]
        return val



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)