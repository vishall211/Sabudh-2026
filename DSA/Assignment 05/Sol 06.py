class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        # Add new element to stack1
        self.stack1.append(x)

    def pop(self):
        # Move elements to stack2 if it is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        # Move elements to stack2 if it is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Create a queue
myQueue = MyQueue()

# Input operations
myQueue.push(1)
myQueue.push(2)

print("\nFront element:", myQueue.peek())
print("Removed element:", myQueue.pop())
print("Is queue empty:", myQueue.empty())
print("\n")
