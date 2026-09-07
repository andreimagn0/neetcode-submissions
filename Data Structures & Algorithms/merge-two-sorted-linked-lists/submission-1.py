# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use a while loop and if statement comparisons to merge the lists into two
        append the entire rest of the linked list once we are done
        '''
        sol = ListNode()
        cur = sol

        cur1, cur2 = list1, list2

        while cur1 and cur2:
            if cur1.val > cur2.val:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next
            else:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            
        cur.next = cur1 if cur1 else cur2
        
        return sol.next