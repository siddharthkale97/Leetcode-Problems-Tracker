class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r = 0, len(matrix) -1
        max_runs = len(matrix) -2
        if max_runs == 0:
            max_runs+= 1
        for j in range(max_runs):
            for i in range(r-l):
                top = l
                bottom = r
                
                temp = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = temp
            r -=1
            l += 1
                