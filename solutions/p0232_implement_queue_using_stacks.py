class MyQueue(object):

    def __init__(self):
        self.queue = []
        

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        a = self.queue[0]
        self.queue = self.queue[1:]
        return a
        

    def peek(self):
        return self.queue[0]
        

    def empty(self):
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
