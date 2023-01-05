class queue:

    def __init__(self):

        self.stack = []
    

    def enqueue(self, data):
        self.stack.append(data)

    def dequeue(self):

        if len(self.stack) == 1:
            return self.stack.pop()

        item = self.stack.pop()

        dequeue_item = self.dequeue()

        self.stack.append(item)

        return dequeue_item
if __name__ == '__main__':
    q = queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())