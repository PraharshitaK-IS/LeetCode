#https://leetcode.com/problems/partition-list/
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)  
        after_head = ListNode(0)  

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None  
        before.next = after_head.next 

        return before_head.next
