from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate

solution = Solution()

# Test case 1: Simple case with majority element
nums1 = [3, 2, 3]
assert solution.majorityElement(nums1) == 3, f"Test case 1 failed: {solution.majorityElement(nums1)} != 3"
print("All tests passed!")
      