def reverseList(head):
    p1,p2=None,head
    while p2:
        tmp = p2.next
        p2.next=p1
        p1 = p2
        p2=tmp
    
    return p1


def reverseListRecursive(head):
    if not head or not head.next:
            return head 
    
    p1=reverseList(head.next)
    head.next.next=head
    head.next=None
    return p1
    