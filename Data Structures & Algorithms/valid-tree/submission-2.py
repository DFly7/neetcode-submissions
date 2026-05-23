from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i:[] for i in range(n)}

        for fir, sec in edges:
            if fir == sec:
                return False
            edgeMap[fir].append(sec)
            edgeMap[sec].append(fir)

        que = deque()
        visited = set()
        
        que.append(0)

        while que:
            for _ in range(len(que)):
                cur = que.popleft()

                if cur in visited:
                    return False
                visited.add(cur)


                for node in edgeMap[cur]:
                    if node in visited:
                        continue
                    que.append(node)
        
        for i in range(n):
            if i not in visited:
                return False
        return True

        
            

        