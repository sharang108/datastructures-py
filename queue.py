class CustomQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.current = None

    def enqueue(self, value):
        node = {'value': value, 'next': None}
        if not(self.front and self.rear):
            self.front = node
            self.rear = node
        else:
            self.rear['next'] = node
            self.rear = node

    def dequeue(self):
        self.front = self.front['next']

    def traverse_queue(self):
        
        pass
