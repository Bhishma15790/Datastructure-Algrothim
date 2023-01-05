class stack:


    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    

    def pop(self ):
        if (self.stack_size < 1):
            return -1
        data = self.stack[-1]
        del self.stack[-1]

        return data
    
    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)


s = stack()
s.push(3)
s.push(4)
s.push(6)
s.push(9)
print("the size of stack :%d" % s.stack_size())
print ("the last item in stack: %d" % s.peek())
