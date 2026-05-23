from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i:[] for i in range(n)}

        for src, dest in edges:
            edgeMap[src].append(dest)

        visited = set()

        def bfs(node, visited):
            que = deque()
            que.append(node)

            curVisit = set()
            curVisit.add(node)
            con = False
            while que:
                for i in range(len(que)):
                    cur = que.popleft()
                    if cur in visited:
                        con = True
                    visited.add(cur)
                    for node in edgeMap[cur]:
                        if node in curVisit:
                            continue
                        que.append(node)
                        curVisit.add(node)
            if con:
                self.res -= 1

        self.res = 0
        for i in range(n):
            if i not in visited:
                bfs(i, visited)
                self.res += 1
        return self.res


