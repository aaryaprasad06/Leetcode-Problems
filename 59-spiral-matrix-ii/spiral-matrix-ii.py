class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat= []
        for i in range(n):
            row=[0]*n
            mat.append(row)
        num=1 
        top, left= 0, 0
        right, bottom= n-1, n-1 

        while top<=bottom and left<=right:
            # First row left to right
            for j in range(left, right+1):
                mat[top][j]= num
                num+=1 
            top+=1
            # Last col top to bottom
            for i in range(top, bottom+1):
                mat[i][right]= num
                num+=1
            right-=1
            # Last row right to left
            if top<=bottom:
                for j in range(right, left-1, -1):
                    mat[bottom][j]= num
                    num+=1
                bottom-=1
            # First col bottom to atop
            if left<=right:
                for i in range(bottom, top-1, -1):
                    mat[i][left]= num
                    num+=1
                left+=1
        return mat
