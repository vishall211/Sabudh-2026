class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        # Store the minimum value at each position
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Create a stack
minStack = MinStack()

# Input operations
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print("\nMinimum:", minStack.getMin())

minStack.pop()

print("Top element:", minStack.top())
print("Minimum:", minStack.getMin())
print("\n")
