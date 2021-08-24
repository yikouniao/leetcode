class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        r0 = ListNode()
        r = r0
        while p and q:
            if p.val < q.val:
                r.next = ListNode(p.val)
                r = r.next
                p = p.next
            else:
                r.next = ListNode(q.val)
                r = r.next
                q = q.next
        if p:
            r.next = p
        if q:
            r.next = q
        return r0.next
