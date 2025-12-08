class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        d={}
        i=0
        j=0
        seen=[]
        while i< len(s) and j< len(t):
            if s[i] not in d:
                if t[j] in seen:
                    return False
                else:
                    d[s[i]]= t[j]
                    seen.append(t[j])
            else:
                if d[s[i]] != t[j]:
                    return False
            i+=1
            j+=1
        return True