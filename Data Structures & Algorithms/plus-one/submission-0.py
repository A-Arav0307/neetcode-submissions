class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1

        while digits[i] > 9:
            if i == 0:
                digits[i] = 0
                digits.insert(0, 1)

                break
            digits[i] = 0
            digits[i-1] += 1
            i -= 1

        return digits