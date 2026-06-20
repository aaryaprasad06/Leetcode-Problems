class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}

        for s in strs:
            alpha=[0]*26
            for i in s:
                alpha[ord(i)-ord('a')]+=1
            key=tuple(alpha)
            if key not in hashmap:
                hashmap[key]=[s]
            else:
                hashmap[key].append(s)
        return list(hashmap.values())