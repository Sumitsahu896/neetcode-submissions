class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))

        # counter_hash = Counter(nums)
        # return any(i > 1 for i in counter_hash.values())
        
        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         return True
        #     hashmap[num] = 1
        
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False