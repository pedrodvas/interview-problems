
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(f"total elem: {len(matrix)**2}")
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()

if __name__ == "__main__":
    sol = Solution()
    sol.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])