class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i, n):
            for j in range(n):
                if isConnected[i][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j, n)
        provinces=0
        visited= set()
        for i in range(len(isConnected[0])):
            if i not in visited:
                visited.add(i)
                provinces+=1
                dfs(i, len(isConnected))

        return provinces