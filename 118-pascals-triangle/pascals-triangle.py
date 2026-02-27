class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        sol=[[1], [1,1]]
        if numRows==2:
            return sol 
        count=2
        while count < numRows:
            a= sol[count-1]
            s=0
            res=[1]
            first=0
            end=1 
            res.append(a[first]+ a[end])
            while end != len(a)-1:
                first=end 
                end+=1 
                res.append(a[first]+ a[end])
            res.append(1)
            sol.append(res)
            count+=1
        return sol
       
                
        
                

