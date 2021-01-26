'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,

where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell,

(0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 

You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
'''

class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        arr = [[float('inf')] * n for i in range(m)]
        heap = []
        heap.append((0, 0, 0))
        ways = [0, 1, 0, -1, 0]
        while heap:
            a, b, c = heapq.heappop(heap)
            if a > arr[b][c]:
                continue
            if b == m - 1 and c == n - 1:
                return a
            for i in range(4):
                bb, cc = b + ways[i], c + ways[i + 1]
                if 0 <= bb < m and 0 <= cc < n:
                    l = max(a, abs(heights[bb][cc] - heights[b][c]))
                    if arr[bb][cc] > l:
                        arr[bb][cc] = l
                        heapq.heappush(heap, (arr[bb][cc], bb, cc))
