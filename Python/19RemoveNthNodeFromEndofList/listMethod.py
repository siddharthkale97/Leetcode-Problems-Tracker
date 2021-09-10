# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def check_left(n,list_n):
    if (len(list_n)-n)>0:
        return True
    else:
        return False

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_n = []
        head_start = head
        list_n.append(head_start)
        cond = 1
        while(cond == 1):
            if head_start.next==None:
                print(len(list_n)-(n+1))
                cond = 0
                # left most case
                if (len(list_n)-n) == 0:
                    print("left most case!")
                    #check if n-1 greater than zero
                    if (n-1)==0:
                        print("left most case, single case!")
                        return None # as no left or right just return None
                    # check right
                    elif (len(list_n)-(n-1))>0: # right exsists
                        print("left most case right is there!")
                        return list_n[(len(list_n)-(n-1))]
                    else: # right doesn't exsists
                        print("left most case, single case!")
                        return None # as no left or right just return None
                # check left, covers middle, and no right position
                elif check_left(n,list_n): # left exists
                    # check if right is there
                    if (n-1) == 0:
                        print("right most case!")
                        list_n[(len(list_n)-(n+1))].next = None
                    elif (len(list_n)-(n-1))>0: # right exists
                        print("middle case!")
                        list_n[(len(list_n)-(n+1))].next = list_n[(len(list_n)-(n-1))]
                    else: # right doesn't exists, right most case
                        print("right most case!")
                        list_n[(len(list_n)-(n+1))].next = None
                
            else:
                head_start = head_start.next
                list_n.append(head_start)
        return head
                
            