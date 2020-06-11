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


permutate = RandomizedQueue()
dequeued = []
while True:
    n = input("Input string (Enter nothing to proceed to next step): ")
    if n == "":
        while True:
            c = input("How much do you want to permutate: ")
            if not c.isdigit():
                print("You may only input integers!")
                continue
            c = int(c)
            for i in range(0, c):
                dequeued.append(permutate.dequeue())
            print(" ".join(dequeued))
            break
    else:
        permutate.enqueue(n)
        continue
    break
