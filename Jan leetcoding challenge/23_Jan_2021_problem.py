'''
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going 
in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], 
where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def diagonal(i, j):
            order, temp = [], []
            while i < len(mat) and j < len(mat[0]):
                order.append((i, j))
                temp.append(mat[i][j])
                i += 1
                j += 1
            temp.sort()
            for i, o in enumerate(order):
                mat[o[0]][o[1]] = temp[i]
        for i in range(len(mat)):
            diagonal(i, 0)
        for i in range(1, len(mat[0])):
            diagonal(0, i)
        return mat
                
