class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        presMap = {i: [] for i in range(numCourses)}

        for src, des in prerequisites:
            presMap[src].append(des)
        
        def dfs(crs, visited):
            if crs in visited:
                return False
            if presMap[crs] == []:
                return True
            visited.add(crs)
            res = True
            for crs2 in presMap[crs]:
                res = res and dfs(crs2, visited)
            
            if not res:
                return False
            
            presMap[crs] = []
            visited.remove(crs)

            return res
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        return True
        
            

        