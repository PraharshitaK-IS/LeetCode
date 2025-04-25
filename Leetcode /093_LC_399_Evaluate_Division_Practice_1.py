#https://leetcode.com/problems/evaluate-division/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        # Build graph
        for (A, B), val in zip(equations, values):
            graph[A][B] = val
            graph[B][A] = 1 / val

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            visited.add(src)

            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    res = dfs(neighbor, dst, visited)
                    if res != -1.0:
                        return res * weight
            return -1.0

        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))
        
        return results