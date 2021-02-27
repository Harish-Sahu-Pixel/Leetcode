'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].

For this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d, div, count = abs(dividend), abs(divisor), 0
        def check(d, div):
            i, count, c = 0, 0, 0
            while d >= div:
                if i == 0:
                    count = 1
                d -= div
                div += div
                if i != 0 :
                    count += count
                c += count
                i += 1
            return d, c
        while d >= abs(divisor):
            d, c = check(d, div)
            print(d, c)
            count += c
        if dividend < 0 or divisor < 0:
            if not (dividend < 0 and divisor < 0):
                sign = count + count
                count = count - sign
                
        if -(2) ** 31 > count or count > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return count
