
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)
    
    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")
    
def print_list(node):
    print("[", end="")
    if node is None or node == []: 
        print("]", end="")
        return
    while node is not None:
        if node.next is None: 
            print(node, end="")
            print("]", end="")
            return
        else:
            print(node, end=", ")
            node = node.next

# helper
def print_backward(list):
    if list is None or list == []: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")

# wrapper
def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")
    
### The fundamental ambiguity theorem describes the ambiguity that is inherent 
### in a reference to a node: A variable that refers to a node might treat the 
### node as a single object or as the first in a list of nodes.

def remove_second(list):
    if list is None or list == []: return
    first = list
    second = list.next
    if second is None: return None
    # Make the first node refer to the third
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
        print("]", end="")

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3

    print_list(node1)

    linkedList = LinkedList()
    linkedList.add_first(1)
    linkedList.add_first(2)
    linkedList.print_backward()

    