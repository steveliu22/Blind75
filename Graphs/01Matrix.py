import math


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [-1] * m
        queue = []
        visited = {}
        for i in range(m):
            ans[i] = [-1] * n
        
        for i in range(m):
            for j in range(n):
                val = mat[i][j]
                coord = (i, j)
                ans[i][j] = -1
                if val == 0:
                    ans[i][j] = 0
                    queue.append(coord)
                    visited[coord] = 1
    
        while len(queue) > 0:
            val = queue.pop(0)
            i = val[0]
            j = val[1]
            search = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            for coord in search:
                y = coord[0]
                x = coord[1]

                if y < 0 or y > (m - 1) or x < 0 or x > (n - 1):
                    pass
                else:
                    if visited.get(coord) == None:
                        visited[coord] = 1
                        queue.append(coord)
                        ans[y][x] = ans[i][j] + 1
        return ans

                    



