class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            if target-n in nums_map:
                return [i, nums_map[target-n]]
            nums_map[n] = i