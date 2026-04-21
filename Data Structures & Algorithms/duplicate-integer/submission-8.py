class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))

        counter_hash = Counter(nums)
        return any(i > 1 for i in counter_hash.values())