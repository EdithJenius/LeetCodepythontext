class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])  # m表示num_row，n表示num_col
        row, col = False, False

        for i in range(n):
            if matrix[0][i] == 0:
                row = True
        for i in range(m):
            if matrix[i][0] == 0:
                col = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0
        for i in range(m):
            if matrix[i][0] == 0:
                matrix[i][:] = [0 for _ in range(n)]
        if row :matrix[0][:] = [0 for _ in range(n)]
        if col:
            for j in range(m):
                matrix[j][0] = 0