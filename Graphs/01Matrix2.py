class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [0] * m
        queue = []
        for i in range(m):
            ans[i] = [0] * n
        
        for i in range(m):
            for j in range(n):
                val = mat[i][j]

                if val == 0:
                    ans[i][j] = 0
                    queue.append((i, j))
                
                else:
                    ans[i][j] = -1
        
        
        while len(queue) > 0:
            val = queue.pop(0)
            i = val[0]
            j = val[1]
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

            for neighbor in neighbors:
                row = neighbor[0]
                col = neighbor[1]

                if not (row < 0 or row >= m or col < 0 or col >= n):
                    if ans[row][col] == -1:
                        ans[row][col] = ans[i][j] + 1
                        queue.append((row, col))
        
        return ans
