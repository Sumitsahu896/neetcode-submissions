class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        if len(s) != len(t):
            return False
            
        for char1, char2 in zip(s, t):
            hashmap1[char1] = hashmap1.get(char1, 0) + 1
            hashmap2[char2] = hashmap2.get(char2, 0) + 1

        return hashmap1 == hashmap2