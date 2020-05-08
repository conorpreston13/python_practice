# Stacks and queues ============================================================
import time
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        print('stack created')
        self.stack_pointer = None

    def push(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        print(f"adding {x.data} to the top of the stack")
        if self.is_empty():
            self.stack_pointer = x
        else:
            x.next = self.stack_pointer
            self.stack_pointer = x

    def pop(self):
        if not self.is_empty():
            print(f"removing node of top of stack")
            current = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            current.next = None
            return current.data
        else:
            return 'Stack is empty'

    def is_empty(self):
        return self.stack_pointer == None

    def peek(self):
        if not self.is_empty():
            return self.stack_pointer.data

    def __str__(self):
        print("Printing Stack state...")
        to_print = ""
        curr = self.stack_pointer
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            print("Stack Pointer")
            print(" |")
            print(" V")
            return "[" + to_print[:-2] + "]"
        return "[]"

class Queue:

    def __init__(self):
        print('Queue created')
        self.head = None
        self.tail = None

    def add(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        print(f"Appending {x.data} to the tail of the queue")
        if self.is_empty():
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def remove(self):
        if not self.is_empty():
            print(f"removing node of head of the queue")
            current = self.head
            self.head = self.head.next
            current.next = None
            return current.data
        else:
            return 'Queue is empty'

    def is_empty(self):
        return self.head == None

    def peek(self):
        if not self.is_empty():
            return self.head.data

    def __str__(self):
        print("Printing Queue state...")
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            if len(to_print) > 4:
                print("Head", " "*(len(to_print)-9),"Tail")
                print(" |", " "*(len(to_print)-6), "|")
                print(" V", " "*(len(to_print)-6), "V")
                return "[" + to_print[:-2] + "]"
            else:
                print("Head & Tail")
                print(" |")
                print(" V")
                return "[" + to_print[:-2] + "]"
        return "[]"

my_stack = Stack()
print("Checking if stack is empty:", my_stack.is_empty())
my_stack.push(1)
time.sleep(2)
my_stack.push(2)
print(my_stack)
time.sleep(2)
my_stack.push(3)
time.sleep(2)
my_stack.push(4)
time.sleep(2)
print("Checking item on top of stack:", my_stack.peek())
time.sleep(2)
my_stack.push(5)
print(my_stack)
time.sleep(2)
print(my_stack.pop())
time.sleep(2)
print(my_stack.pop())
print(my_stack)
time.sleep(2)
my_stack.push(4)
print(my_stack)
time.sleep(2)


my_queue = Queue()
print("Checking if Queue is empty:", my_queue.is_empty())
time.sleep(2)
my_queue.add(1)
print(my_queue)
time.sleep(2)
my_queue.add(2)
my_queue.add(3)
print(my_queue)
time.sleep(2)
my_queue.add(4)
my_queue.add(5)
time.sleep(2)
print("Checking node at head of Queue:", my_queue.peek())
time.sleep(2)
my_queue.add(6)
print(my_queue)
time.sleep(2)
print(my_queue.remove())
time.sleep(2)
print(my_queue.remove())
time.sleep(2)
print(my_queue)
time.sleep(2)
my_queue.add(4)
time.sleep(2)
print(my_queue)
