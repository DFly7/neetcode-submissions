class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.edges = {}

        if prerequisites == []:
            return True

        for edge in prerequisites:
            if edge[0] not in self.edges:
                self.edges[edge[0]] = []
            if edge[1] not in self.edges:
                self.edges[edge[1]] = []
            self.edges[edge[0]].append(edge[1])

        def dfs(num, visited):
            if num in visited:
                return False
            if self.edges[num] == []:
                return True
            visited.add(num)
            res = False
            for n in self.edges[num]:
                if n in visited:
                    return False
                res = dfs(n, visited) or res
            
            return res
        
        for i in range(numCourses):
            if i not in self.edges:
                self.edges[i] = []
            if not dfs(i, set()):
                return False
        return True
        
            

        