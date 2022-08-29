class Solution:

    """This class implements linear queue.
      Attributes:
          stack: A list which maintains the content of stack.
          queue: A list which maintains the content of queue.
          top: An integer which denotes the index of the element at the top of the stack.
          front: An integer which denotes the index of the element at the front of the queue.
          rear: An integer which denotes the index of the element at the rear of the queue.
          size: An integer which represents the size of stack and queue.
      """

 

    # Write your code here

    def __init__(self, size):

        """Inits Solution with stack, queue, size, top, front and rear.
        Arguments:
          size: An integer to set the size of stack and queue.
        """

       

        self.size = size

        self.lst = [None]*size

        self.queue = [None]*size

        self.top = -1

        self.rear = -1

        self.front = -1

 

    def is_stack_empty(self):

        """
        Check whether the stack is empty.
        Returns:
          True if it is empty, else returns False.
        """

        # Write your code here

        if self.top == -1:

            return 1

        else :

            return 0

    def is_queue_empty(self):

        """
        Check whether the queue is empty.
        Returns:
          True if it is empty, else returns False.
        """

        # Write your code here

        if self.front==-1 or self.front>self.rear:

            return 1

        else:

            return 0

    def is_stack_full(self):

        """
        Check whether the stack is full.
        Returns:
          True if it is full, else returns False.
        """

        # Write your code here

        if self.top == (self.size - 1):

            return 1

        else :

            return 0

    def is_queue_full(self):

        """
        Check whether the queue is full.
        Returns:
          True if it is full, else returns False.
        """

        # Write your code here

        if self.rear==(self.size-1):

            return 1

        else:

            return 0
