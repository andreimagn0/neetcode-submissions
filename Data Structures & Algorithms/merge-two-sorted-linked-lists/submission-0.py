# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #we use a while loop with two pointers on each list, the base case is if the p.next = null
        #if either equals null, then append the rest of the numbers into list until it is p.next = null
        #compare each of the pointers if one is bigger than the other, then add
        prev = ListNode(-1)
        tail = prev
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
                tail = tail.next
            else:
                tail.next = p2
                p2 = p2.next
                tail = tail.next
        if p1 is None:
            tail.next = p2
        else:
            tail.next = p1
        return prev.next



        