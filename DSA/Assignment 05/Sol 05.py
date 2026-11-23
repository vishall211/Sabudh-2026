from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        # Move existing elements to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Add the new element
        self.q1.append(x)

        # Move all elements back to q1
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# Create a stack
myStack = MyStack()

# Input operations
myStack.push(1)
myStack.push(2)

print("\nTop element:", myStack.top())
print("Removed element:", myStack.pop())
print("Is stack empty:", myStack.empty())
print("\n")
