import random


class RandomizedQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            rand = random.randint(0, len(self.queue))
            data = self.queue.pop(rand)
            return data
        else:
            return "Queue is empty."
