class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        presMap = {i: [] for i in range(numCourses)}
        self.result = []
        visit = set()
        for src, des in prerequisites:
            presMap[src].append(des)
        
        def dfs(crs, visited):
            if crs in visited:
                return False
            if presMap[crs] == []:
                if crs not in self.result:
                    self.result.append(crs)
                return True
            visited.add(crs)
            res = True
            for crs2 in presMap[crs]:
                res = res and dfs(crs2, visited)
            
            if not res:
                return False
            
            presMap[crs] = []
            visited.remove(crs)
            self.result.append(crs)

            return res

        for i in range(numCourses):
            if not dfs(i, visit):
                return []
        return self.result
