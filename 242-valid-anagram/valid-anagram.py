class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha1= [0]* 26 
        alpha2= [0]* 26 
        for ch in s:
            idx= ord(ch)- ord('a')
            alpha1[idx]+=1 
        
        for ch in t:
            idx= ord(ch)- ord('a')
            alpha2[idx]+=1 
        
        return alpha1==alpha2