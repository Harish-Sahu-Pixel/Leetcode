'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        heapq.heapify(nums)
        i = 1
        while i <= length - k + 1:
            ans = heapq.heappop(nums)
            i += 1
        return ans
