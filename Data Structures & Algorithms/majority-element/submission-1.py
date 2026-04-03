class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap = defaultdict(int)
        # max_count = 0
        # max_value = nums[0]
        # for num in nums:
        #     hashmap[num] += 1
        #     if hashmap[num] > max_count:
        #         max_count = hashmap[num]
        #         max_value = num
        # return max_value

        # Boyer-Moore algorithm
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate