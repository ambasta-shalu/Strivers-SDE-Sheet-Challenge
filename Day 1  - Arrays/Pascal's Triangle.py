# Coded by Shalu Ambasta :)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        tri = []
        for i in range(numRows):
            tri.append([1]*(i+1))

        for i in range(2, numRows):
            for j in range(1, i):
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

        return tri
        