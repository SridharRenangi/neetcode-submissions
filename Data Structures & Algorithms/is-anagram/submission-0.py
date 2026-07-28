class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        count2 = {}
        for bh in t:
            if bh in count2:
                count2[bh] += 1
            else:
                count2[bh] = 1
        
        return count == count2