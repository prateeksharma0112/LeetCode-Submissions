class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)

        while left < n:

            if nums[left] == 0:
                nums.pop(left)
                nums.append(0)
                n-=1
            else:
                left+=1


        