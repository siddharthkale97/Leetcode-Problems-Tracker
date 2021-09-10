class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        array_i = []
        array_j = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    array_i.append(i)
                    array_j.append(j)
        array_i = set(array_i)
        array_j = set(array_j)
        for x in array_i:
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
        for x in array_j:
            for j in range(len(matrix)):
                matrix[j][x] = 0
        