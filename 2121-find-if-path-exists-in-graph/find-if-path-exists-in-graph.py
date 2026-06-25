from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph= defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        
        def traverse(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if traverse(neighbor, visited):
                        return True
        
        visited= set()
        return True if traverse(source, visited) else False      
        