class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)==0 or len(t)==0 or len(s) < len(t):
            return ""
        
        mapT={}
        mapS={}

        for i in t:
            if i not in mapT:
                mapT[i]=1
            else:
                mapT[i]+=1 

        required= len(mapT)
        l=0
        r=0
        create=0
        ans=[-1, 0, 0]

        while (r<len(s)):
            c= s[r]
            if c in mapS:
                mapS[c]+=1
            else:
                mapS[c]=1
            if c in mapT and mapS[c]==mapT[c]:
                create+=1
            while l<=r and required==create:
                c= s[l]
                if ans[0]==-1 or ans[0]>= r-l+1:
                    ans[0]= r-l+1 
                    ans[1]= l
                    ans[2]= r
                if mapS[c]==1:
                    del mapS[c]
                else:
                    mapS[c]-=1
                if c in mapT and mapS.get(c, 0) < mapT[c]:
                    create-=1
                l+=1
            r+=1
        if ans[0]==-1:
            return "" 
        return s[ans[1]:ans[2]+1]


