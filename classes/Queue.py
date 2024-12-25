"""

Script name: "classes\Queue.py"\n
Goal of the script: Contains the Queue class definition.\n
Part of project: "futureTLVAxioma"\n
Description of project: A taxi system simulator.\n
Ways to contact me if something went wrong in the code: itay.rimmler@gmail.com\n
Made by: Itay Rimmler.\n

"""

# Imports
from collections import deque


class Queue:
    """
    Credit to ChatGPT!.\n
    """
    def __init__(self):
        """
        Contructor.\n
        """
        self.q = deque()

    def e(self, item):
        """
        enqueue.\n
        """
        self.q.append(item)  # Add to the end

    def d(self):
        """
        dequeue.\n
        """
        if self.i():
            return None
        return self.q.popleft()  # Remove from the front

    def i(self):
        """
        is_empty.\n
        """
        return len(self.q) == 0