print("Hello "*3+"5")

#2
items = [10, 20, 30]
items.append([40, 50])
print(items)

#3
print(bool(0) or bool(""))


#4
class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None  # Pointer to the next node (initially None)


class LinkedList:
    """Manages the nodes and structural operations of the list."""
    def __init__(self):
        self.head = None  # Points to the first node in the list

    def insert_at_head(self, data):
        """Inserts a new node at the very beginning. Time Complexity: O(1)"""
        new_node = Node(data)
        new_node.next = self.head  # Link new node to current head
        self.head = new_node       # Move head pointer to new node

    def insert_at_tail(self, data):
        """Inserts a new node at the end. Time Complexity: O(N)"""
        new_node = Node(data)
        if not self.head:          # If list is empty, make it the head
            self.head = new_node
            return
        
        current = self.head
        while current.next:        # Traverse to the last node
            current = current.next
        current.next = new_node    # Link the last node to the new node

    def delete_value(self, target):
        """Deletes the first node containing the target value. Time Complexity: O(N)"""
        if not self.head:          # Case 1: Empty list
            return

        if self.head.data == target:  # Case 2: Target is at the head
            self.head = self.head.next
            return

        current = self.head
        # Case 3: Search for target, keeping track of previous node
        while current.next and current.next.data != target:
            current = current.next

        if current.next:           # If target was found, bypass it
            current.next = current.next.next

    def print_list(self):
        """Traverses and prints the list elements sequentially."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# Create an empty Linked List
ll = LinkedList()

# 1. Insert elements
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_tail(30)
ll.insert_at_tail(40)

print("\n\nOriginal List:")
ll.print_list()  # Output: 20 -> 10 -> 30 -> 40 -> None

# 2. Delete an element from the middle
ll.delete_value(30)
print("\nAfter deleting 30:")
ll.print_list()  # Output: 20 -> 10 -> 40 -> None

# 3. Delete the head element
ll.delete_value(20)
print("\nAfter deleting head (20):")
ll.print_list()  # Output: 10 -> 40 -> None


#output
Hello Hello Hello 5
[10, 20, 30, [40, 50]]
False


Original List:
20 -> 10 -> 30 -> 40 -> None

After deleting 30:
20 -> 10 -> 40 -> None

After deleting head (20):
10 -> 40 -> None
