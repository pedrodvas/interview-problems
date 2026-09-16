from collections import deque

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_pos = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros_pos.append((i,j))

        while zeros_pos:
            curr = zeros_pos.pop()
            null_row_col(curr[0], curr[1], matrix)
        return

def null_row_col(row: int, col: int, matrix: list[list[int]]):
    #null row first
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
    for i in range(len(matrix)):
        matrix[i][col] = 0

if __name__ == "__main__":
    sol = Solution()
    sol.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])