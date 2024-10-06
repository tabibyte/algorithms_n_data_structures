# Single element of the queue (has value and next pointer)
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# Creates queue with linked list (has pointer to head and tail)
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("dequeue from empty queue")
        else:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_value

    def peek(self):
        if self.head is None:
            raise IndexError("peek from empty queue")
        else:
            return self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue)
