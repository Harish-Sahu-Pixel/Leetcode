'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        p, ans =[], []
        for head in lists:
            if head:
                p.append(head)
        while True:
            mini = float('inf')
            for i in range(len(p)):
                if p[i]:
                    if p[i].val < mini:
                        mini = p[i].val
                        loc = i
            if mini != float('inf'):
                ans.append(p[loc])
                p[loc] = p[loc].next
            else:
                break
        for i in range(len(ans) - 1):
            ans[i].next = ans[i + 1]
        if ans:
            ans[-1].next = None
            return ans[0]
        return 
