class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups= {} 
        for word in strs:
            alpha=[0]*26 
            for char in word:
                idx= ord(char)- ord('a')
                alpha[idx]+=1 
            alpha= tuple(alpha)
            if alpha in groups:
                groups[alpha].append(word)
            else:
                groups[alpha]= [word]
        return list(groups.values())