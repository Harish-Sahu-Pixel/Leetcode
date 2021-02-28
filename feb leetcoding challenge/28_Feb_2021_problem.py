'''
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.

pop(), which removes and returns the most frequent element in the stack.

If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
'''

from collections import Counter
class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.Dict = collections.defaultdict(list)
        self.Max = 0

    def push(self, x: int) -> None:
        freq, Dict = self.freq, self.Dict
        freq[x] += 1
        self.Max = max(self.Max, freq[x])
        Dict[freq[x]].append(x)

    def pop(self) -> int:
        freq, Dict, Max = self.freq, self.Dict, self.Max
        temp = Dict[Max].pop()
        if not Dict[Max]:
            self.Max = Max - 1
        freq[temp] -= 1
        return temp

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
