'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.

Integers in each column are sorted in ascending from top to bottom.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, ele):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == ele:
                    return True
                elif ele < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        for mat in matrix:
            if binary_search(mat, target):
                return True
        return False
    
             
