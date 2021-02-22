'''
On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;

Decrement: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.
'''

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while True:
            if Y > X and Y & 1:
                Y += 1
                ans += 1
            elif Y > X and not Y & 1:
                Y //= 2
                ans += 1
            else:
                ans += X - Y
                break
        return ans
