'''
143. Reorder List -

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

'''
Approach -
Create a list to store each individual head. Traverse and add the each node to the list.
Find mid point, then use two points, front and end.
Add the last element to the current pointer and set the next on last element
to the next front pointer
set the last most element next to None
Set first element of list as head
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = [] # Create list
        headm = head
        while(headm!=None):
            l.append(headm) # Get all nodes in list
            headm = headm.next 
        if len(l)%2==0: # For even
            n = len(l)//2
            last = len(l) - 1
            for i in range(n-1):
                #print(i)
                l[i].next = l[last] # add the last to the front
                l[last].next = l[i+1] # add next in front the the .next of last
                last -= 1 # Decrement last pointer
            l[n-1].next = l[last]
            l[last].next = None # Set the last most linkedlist node as None
            
        else: # For odd
            n = len(l)//2 + 1
            last = len(l) - 1
            for i in range(n-1):
                #print(l[i])
                l[i].next = l[last]
                l[last].next = l[i+1]
                last -= 1
            l[n-1].next = None
        
        
        head = l[0] # Set list's first element as head

'''
Runtime: 80 ms, faster than 98.31% of Python3 online submissions for Reorder List.
Memory Usage: 23.3 MB, less than 49.20% of Python3 online submissions for Reorder List.

Time - O(2n), Space O(n)
'''
