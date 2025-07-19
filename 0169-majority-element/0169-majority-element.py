class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)

        for number in nums:
            count[number] +=1

        for key, value in count.items():
            if value > (n // 2):
                return key
        
        return 0