#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to handle edge cases like duplicates at the beginning
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Detect duplicates
            if current.next and current.val == current.next.val:
                # Skip all nodes with this value
                val = current.val
                while current and current.val == val:
                    current = current.next
                prev.next = current  # Link to the next distinct node
            else:
                prev = current
                current = current.next

        return dummy.next
