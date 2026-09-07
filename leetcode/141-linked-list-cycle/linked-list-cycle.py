# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=set()
        node=head
        while node:
            if node.next  in temp:
                return True
            temp.add(node.next)
            node=node.next

        return False

        