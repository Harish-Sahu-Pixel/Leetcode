'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        
        pa, pb = headA, headB
        while True:
            if pa == pb and pa.next is not None and pb.next is not None:
                return pa
            elif pa is not pb and pa.next is None and pb.next is None:
                return None
            elif pa is pb and pa.next is None and pb.next is None:
                return pa
            else:
                if pa.next is None:
                    pa = headB
                else:
                    pa = pa.next
                if pb.next is None:
                    pb = headA
                else:
                    pb = pb.next
        return None
                
        
