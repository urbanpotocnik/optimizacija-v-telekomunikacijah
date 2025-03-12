# Data structures

# A simple class stack 
class Stack:

    def __init__(self, name = 'MyStack'):
        self.data = []
        self.name = name

    def pop(self):
        '''Get last item from the stack'''
        if len(self.data) < 1:
            return None
        return self.data.pop()

    def push(self, item):
        '''Add item to the stack/queue'''
        self.data.append(item)

    def indexOf(self, item):
        if item in self.data:
            return self.data.index(item)
        else:
            return None

    def size(self):
        '''Return number of items'''
        return len(self.data)
    
    def print(self):
        '''Print all items'''
        print(self.name, "size:", self.size(), ', data:', self.data)

    def get_data(self):
        '''Return data (list)'''
        return self.data
    
    def empty(self):
        '''Returns True if empty'''
        if len(self.data)==0:
            return True
        else:
            return False

# And a queue that only has enqueue and dequeue operations
class Queue(Stack):

    def __init__(self, name = 'MyQueue'):
        super().__init__()
        self.name = name

    def enqueue(self, item):
        '''Add item to the queue'''
        #self.queue.append(item)
        self.push(item)

    #def push(self, item):
    #    self.enqueue(item)

    def dequeue(self):
        '''Return first item in the queue'''
        if len(self.data) < 1:
            return None
        return self.data.pop(0)

    def pop(self):
        '''Return first item in the queue'''
        return self.dequeue()

    #def size(self):
    #    return len(self.queue) 
    
    #def indexOf(self, item):
    #    if item in self.queue:
    #        return self.queue.index(item)
    #    else:
    #        return None

    #def print(self):
    #    '''Print all items'''
    #    print("Queue : ", self.size(), ': ', self.data)

    #def get_data(self):
    #    return self.queue
