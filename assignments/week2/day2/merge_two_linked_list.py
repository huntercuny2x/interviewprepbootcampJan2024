class ListNode():
    def __init__(self):
        self.val=0
        self.next=None

        

def mergeTwoLists():    
    dummy=node=ListNode()
    
    while list1 and list2:
        if list1.val < list2.val:
            node.next=list1
            list1=list1.next
        else:
            node.next=list2
            list2=list2.next
        node=node.next
    
    node.next=list1 or list2
    return dummy.next
        