# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy
        for _ in range(n+1):
            ahead = ahead.next # move ahead by n+1 times
        while ahead: #Move both pointers together
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return dummy.next # we won't return head as it may point to garbage node

        