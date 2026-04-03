class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        max_count = 0
        max_value = nums[0]
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] > max_count:
                max_count = max(max_count, hashmap[num])
                max_value = num
        return max_value