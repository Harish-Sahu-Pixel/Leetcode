'''
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.

For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].

If the element is odd, multiply it by 2.

For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.
'''

class Solution:
    def minimumDeviation(self, nums):
        heap, ans = [], float('inf')
        for num in nums:
            n= num
            while not n & 1: 
                n //= 2
            heap.append((n, max(num, n * 2)))
        maxi = max(i for i,j in heap)
        heapify(heap)
        while len(heap) == len(nums):
            n, l = heappop(heap)
            ans = min(ans, maxi - n)
            if n < l:
                heappush(heap, (n * 2, l))
                maxi = max(maxi, n * 2)
        return ans
