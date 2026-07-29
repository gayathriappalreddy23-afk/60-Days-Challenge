class SingleLL:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_begin(head,data):
    new_node=SingleLL(data)
    new_node.next=head
    return new_node
def insert_end(head,data):
    new_node=SingleLL(data)
    if head is None:
        return new_node
    current=head
    while current.next:
        current=current.next
    current.next=new_node
    return head

def insert_position(head,data,position):
    new_node=SingleLL(data)
    if position==1:
        new_node.next=head
        return new_node
    current=head
    for i in range(position - 2):
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head
    
def delete(head,value):
    if head.data==value:
        return head.next
    current=head
    while current:
        if current.next.data==value:
            current.next=current.next.next
            return head
        current=current.next
    return head
    
def ReverseLL(head):
    prev=None
    current=head
    while current:
        current.next,prev,current=prev,current,current.next
    return prev
    
def Middle_node(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

def Has_Cycle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def traverse(head):
    current=head
    while current:
        print(current.data,"-> ",end=" ")
        current=current.next
    print("None")
    
S=SingleLL(8)
S=insert_begin(S,4)
S=insert_end(S,7)
S=insert_position(S,1,1)
S=insert_position(S,6,2)
S=insert_position(S,9,3)
S=delete(S,8)

print("Before Traversal: ")
traverse(S)

S=ReverseLL(S)
print("\n\nAfter Traversal: ")
traverse(S)

print("\n\nMiddle value in a Single Linked List: ")
S=Middle_node(S)
traverse(S)
#Output
# Before Traversal: 
# 1 ->  6 ->  9 ->  4 ->  7 ->  None


# After Traversal: 
# 7 ->  4 ->  9 ->  6 ->  1 ->  None


# Middle value in a Single Linked List: 
# 9 ->  6 ->  1 ->  None


# Cycle status before loop creation: False

print("\n\nCycle status before loop creation:", Has_Cycle(S))
