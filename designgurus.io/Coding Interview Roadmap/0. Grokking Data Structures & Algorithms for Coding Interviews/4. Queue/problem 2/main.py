from queue import Queue
import json

class Solution:
    def __init__(self):
        # ToDo: Write Your Code Here.
        self.main = Queue()
        self.aux = Queue()

    def push(self, val):
        # ToDo: Write Your Code Here.
        self.aux.put(val)
        
        while not self.main.empty():
            self.aux.put(self.main.get())
        
        self.main, self.aux = self.aux, self.main

    def pop(self):
        # ToDo: Write Your Code Here.

        if not self.main.empty():
            return self.main.get()
        return -1
