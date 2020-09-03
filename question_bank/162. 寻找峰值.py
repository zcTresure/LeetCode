class Solution:
    def findPeakElement(self, nums: list) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if(nums[m] > nums[m + 1]):
                r = m
            else:
                l = m + 1
        return l


nums = [1, 2, 1, 3, 5, 6, 4]
test = Solution()
print(test.findPeakElement(nums))
