class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEndOnePass(head, n):
    count = 0
    p1 = head
    while p1:
        count+=1
        p1=p1.next

    dummy = p1 = ListNode(0,head)
    for i in range(count-n):
        p1=p1.next

    p1.next=p1.next.next
    return dummy.next 



def removeNthFromEndTwoPass(head, n):
    dummy=l=ListNode(0,head)
    r=head
    for i in range(n):
        r=r.next

    while r:
        r=r.next
        l=l.next

    l.next=l.next.next
    return dummy.next