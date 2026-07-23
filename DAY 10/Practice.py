class Solution(object):
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count >= majority_count: 
                return num

s = Solution()
nums = [2, 3, 1, 2, 2, 2, 3, 1, 1]
result = s.majorityElement(nums)
print(result)  # Output: 2
