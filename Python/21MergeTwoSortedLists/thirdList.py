class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        rethead = None
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        if (l1.val<=l2.val):
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        rethead = head
        while (l1 !=None and l2!=None):
            if (l1.val<=l2.val):
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        while(l1!=None):
            head.next = l1
            l1 = l1.next
            head = head.next
        while(l2!=None):
            head.next = l2
            l2 = l2.next
            head = head.next
        return rethead