'''
54. Spiral Matrix -
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
'''
Approach - 
Maintain 4 pointers up down left right
so spiral and store the sequence
then shrink the pointers to a smaller matrix, and recurssion 
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.outputarray = []
        self.visited = []
        def spiral(left,right,up,down):
            if up-down-1 == 0 or left-right-1 ==0 or up==down or left==right:
                return
            i = left
            while(i<right):
                if (up,i) not in self.visited:
                    self.outputarray.append(matrix[up][i])
                    self.visited.append((up,i))
                i+= 1
            i = up + 1
            while(i<down):
                if (i,right-1) not in self.visited:
                    self.outputarray.append(matrix[i][right-1])
                    self.visited.append((i,right-1))
                i+= 1
            up += 1
            i= right -2
            while(i>=left):
                if (down-1,i) not in self.visited:
                    self.outputarray.append(matrix[down-1][i])
                    self.visited.append((down-1,i))
                i-=1
            i = down - 2
            while(i>=up):
                if (i,left) not in self.visited:
                    self.outputarray.append(matrix[i][left])
                    self.visited.append((i,left))
                i-=1
            spiral(left + 1, right -1, up, down -1)
        spiral(0,len(matrix[0]),0,len(matrix))
        return self.outputarray
'''
Runtime: 31 ms, faster than 58.90% of Python3 online submissions for Spiral Matrix.
Memory Usage: 14.4 MB, less than 27.97% of Python3 online submissions for Spiral Matrix.
'''