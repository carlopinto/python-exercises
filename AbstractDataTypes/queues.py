import time
import random

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

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo
    
class QueueList:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self): 
        return (self.items == [])
  
class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0
    
    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo
    
def check_performance():
    print("Compare queue implementations with lists and linked lists:")
    n = 200000

    t0 = time.time()
    queue = QueueList()
    for i in range(n):
        queue.push(i)

    while not queue.is_empty():
        queue.pop()

    t1 = time.time()
    print("it took {0} seconds - [List] queue".format(t1-t0))

    t0 = time.time()
    improved_queue = ImprovedQueue()
    for i in range(n):
        improved_queue.insert(i)

    while not improved_queue.is_empty():
        improved_queue.remove()

    t1 = time.time()
    print("it took {0} seconds - IMPROVED queue".format(t1-t0))

    # Improved queue is way quicker when we have 100,000+ items

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

class ImprovedPriorityQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0
    
    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # TODO find where it should go, so the queue is already sorted after the insertion
            current = self.head
            previous = self.head

            # check if it is the highest already
            if node.cargo >= self.head.cargo:
                node.next = self.head
                self.head = node
            else:
                flag = True
                while current.cargo > node.cargo:
                    if current.next is None:
                        # end of queue
                        current.next = node
                        self.last = node
                        self.length += 1
                        return
                    else:
                        if flag:
                            # update current (and not previous) the first time you are in the loop
                            current = current.next
                            flag = False
                        else:
                            current = current.next
                            previous = previous.next
                # Node found
                node_found = previous            
                # Append the new node
                node_found.next = node
                if current is not None:
                    node.next = current
                else:
                    # we need to update the last node too
                    self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

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

def check_performance_priority():
    print("Compare priority queue implementations with lists and linked lists:")
    n = 10000

    t0 = time.time()
    priority_queue = PriorityQueue()
    for i in range(n):
        num = random.randint(0, n + 1)
        priority_queue.insert(num)

    while not priority_queue.is_empty():
        priority_queue.remove()

    t1 = time.time()
    print("it took {0} seconds - [list] priority queue".format(t1-t0))

    t0 = time.time()
    improved_priority_queue = ImprovedPriorityQueue()
    for i in range(n):
        num = random.randint(0, n + 1)
        improved_priority_queue.insert(num)

    while not improved_priority_queue.is_empty():
        improved_priority_queue.remove()

    t1 = time.time()
    print("it took {0} seconds - IMPROVED priority queue".format(t1-t0))


class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score= score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)
    
    def __gt__(self, other):
        return self.score < other.score    # Less is more

if __name__ == "__main__":
    check_performance()

    check_performance_priority()

    tiger = Golfer("Tiger Woods", 61)
    phil = Golfer("Phil Mickelson", 72)
    hal = Golfer("Hal Sutton", 69)

    pq = PriorityQueue()
    for g in [tiger, phil, hal]:
         pq.insert(g)

    while not pq.is_empty():
         print(pq.remove())