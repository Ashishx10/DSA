# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode()
        dummy.next=head
        slow=fast=head # Floyd's cycle detecting Algorithm (Slow and fast pointers)
        while fast and fast.next:
            fast=fast.next.next # 2 moves
            slow=slow.next# 1 move
            if slow is fast:
                return True
        return False

        