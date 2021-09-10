class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = list(filter(lambda a: a != None or a!=[], lists))
        lists =list(filter(lambda a: a != [], lists))
        
        if len(lists) == 0:
            return None
        
        currlist = [x.val for x in lists]
        minheadindex = currlist.index(min(currlist))
        head = lists[minheadindex]
        mainhead = head
        prev = lists[minheadindex]
        lists[minheadindex] = lists[minheadindex].next
        if lists[minheadindex] == None:
            lists.remove(lists[minheadindex])
            del currlist[minheadindex]
        else:
            currlist[minheadindex] = lists[minheadindex].val
            
        while(len(lists)>0):
            minheadindex = currlist.index(min(currlist))
            head.next = lists[minheadindex]
            head = head.next
            prev = lists[minheadindex]
            lists[minheadindex] = lists[minheadindex].next
            if lists[minheadindex] == None:
                lists.remove(lists[minheadindex])
                del currlist[minheadindex]
            else:
                currlist[minheadindex] = lists[minheadindex].val
        return mainhead