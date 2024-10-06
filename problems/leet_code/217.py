class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            hash_map[num] = None
        return False