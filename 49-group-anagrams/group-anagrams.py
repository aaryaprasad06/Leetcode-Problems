class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}

        for s in strs:
            alpha=[0]*26
            for char in s:
                alpha[ord(char)- ord('a')]+=1 
            key= tuple(alpha)
            if key not in hashmap:
                hashmap[key]= []
            hashmap[key].append(s)
        return list(hashmap.values())