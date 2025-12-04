class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        i=0
        j=len(s)-1
        s= list(s)
        while i<j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j]= s[j], s[i]
                i+=1
                j-=1
            elif s[i] not in vowels:
                i+=1
            else:
                j-=1
        s= "".join(s)
        return s