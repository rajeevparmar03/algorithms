#flood cycle detect
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
    

def has_cycle(head):
    if not head or head.next:
        return False
        
    slow =head
    fast= head.next

    while slow!=fast:
        if not fast or fast.next :
            return False
            slow=slow.next
            fast=fast.next.next
        return True
        

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3 
        
hascycle= has_cycle(head)

if has_cycle:
    print("have a cycle ")
else:
    print("doesn't have any cycle ")
