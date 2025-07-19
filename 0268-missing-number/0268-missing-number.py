class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        expectedTotal = n*(n+1)/2

        currentTotal = sum(nums)

        return int(expectedTotal - currentTotal)
        
