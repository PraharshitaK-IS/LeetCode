# https://leetcode.com/problems/reverse-nodes-in-k-group/
#  Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head                       # nothing to do

        # Helper to check whether k nodes remain starting from 'node'
        def has_k_nodes(node, k):
            steps = 0
            while node and steps < k:
                node = node.next
                steps += 1
            return steps == k

        dummy = ListNode(-1, head)
        group_prev = dummy

        while has_k_nodes(group_prev.next, k):
            # Identify the k‑th node to become the group's new head
            group_end = group_prev
            for _ in range(k):
                group_end = group_end.next        # after loop: points to kth node

            next_group_start = group_end.next     # store (k+1)th node

            # Reverse the current k‑block
            prev, curr = next_group_start, group_prev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev, curr = curr, nxt           # advance

            # Re‑connect reversed block
            old_group_start = group_prev.next     # this is now the tail
            group_prev.next = group_end          # new head of this block
            group_prev = old_group_start         # move group_prev to tail for next loop

        return dummy.next