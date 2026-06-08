class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        ds1={}
        ds2={}

        for i in range(len(s1)):
            if s1[i] not in ds1:
                ds1[s1[i]]=1
            else:
                ds1[s1[i]]+=1 
        window= len(s1)

        for i in  range(window):
            if s2[i] not in ds2:
                ds2[s2[i]]= 1
            else:
                ds2[s2[i]]+=1 
        
        if ds1==ds2:
            return True 
        
        for i in range(window, len(s2)):
            incoming= s2[i]

            if incoming not in ds2:
                ds2[incoming]=1 
            else:
                ds2[incoming]+=1 

            outgoing=s2[i-window]

            if ds2[outgoing]<=1:
                ds2.pop(outgoing, None)
            else:
                ds2[outgoing]-=1 
            if ds1==ds2:
                return True 
        return False