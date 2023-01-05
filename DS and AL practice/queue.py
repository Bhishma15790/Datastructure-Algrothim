from ctypes import sizeof


class queue:

    def __init__(self):
        self.queue = []

    def sizeof_queue(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.sizeof_queue != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            -1
    
    def peek(self):
        return self.queue[0]



q = queue()

q.enqueue(2)
q.enqueue(22)
q.enqueue(222)
q.enqueue(2222)
q.enqueue(22222)

print("the sizze of queue is :%d"  % q.sizeof_queue())
print("we removw the given data %d" % q.dequeue())
print("we removw the given data %d" % q.dequeue())
