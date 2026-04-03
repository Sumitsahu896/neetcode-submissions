class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a...z
            for char in string:
                count[ord(char) - ord("a")] += 1

            answer[tuple(count)].append(string)

        return list(answer.values())