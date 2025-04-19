#2. Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # value from l1 node
            val2 = l2.val if l2 else 0  # value from l2 node

            total = val1 + val2 + carry
            carry = total // 10         # update carry
            digit = total % 10          # get last digit

            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next