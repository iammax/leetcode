class MyStack(object):
    
    def __init__(self):
        self.stack = []
        self.length = -1
        
    def push(self, x):
        self.stack.append(x)
        self.length += 1
        
    def pop(self):
        top = self.stack[self.length]
        self.stack = self.stack[:self.length]
        self.length -= 1
        return top

    def top(self):
        return self.stack[self.length]

    def empty(self):
        return self.length == -1

