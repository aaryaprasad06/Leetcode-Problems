class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        k=0
        for i in strs[0]:
            flag=True
            for j in range(1, len(strs)):
                if k>= len(strs[j]) or strs[j][k]!=i:
                    flag=False
                    break
            if flag==True:
                prefix+=(i)
                k+=1
            else:
                break                                
        return prefix