# Coded by Shalu Ambasta :)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # TRANSPOSE
        for i in range(n):
            for j in range(n):
                if i == j :
                    break
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # REVERSING ROWS
        for i in range(n):
            matrix[i] = matrix[i][::-1]
            