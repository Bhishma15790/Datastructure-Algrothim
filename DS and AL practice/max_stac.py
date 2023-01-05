
# THis is the solution to find the max in the stack 

class max_stack:

    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        self.main_stack.append(data)

        if (len(self.main_stack) == 1):
            self.max_stack.append(data)
            return
        
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.main_stack.pop()
        return self.max_stack.pop()

    def get_max(self):
        return self.max_stack.pop()


max = max_stack()

max.push(2)
max.push(6)
max.push(7)
max.push(1)
max.push(8)

print("maximum number in stack: %d" % max.get_max())

        
