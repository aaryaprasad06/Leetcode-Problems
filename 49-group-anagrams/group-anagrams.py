class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d= {} 

        for word in strs:
            alpha= [0]* 26 
            for ch in word:
                idx= ord(ch)- ord('a')
                alpha[idx]+=1 
            alpha= tuple(alpha)
            if alpha in d:
                d[alpha].append(word)
            else:
                d[alpha]= [word] 
        return list(d.values())