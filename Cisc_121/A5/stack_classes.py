"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  Joseph Liao
ID:      20366481
Email: 22jl41@queensu.ca
Section: CISC121 Winter 2023
-------------------------------------------------------
"""
class Stack:
    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """

        self.items = []
    def push(self, item):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self.items.append(item)
    def pop(self):

        return self.items.pop()

    def reverse(self):
        aux_stack = Stack()
        while not self.is_empty():
            aux_stack.push(self.pop())
        self.items = aux_stack.items

        print("reversed:", self)
    def peek(self):
        return self.items[-1] #get the last element

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        return self.items == []
    def __str__(self):
        return str(self.items)

    def split_alt(self):
        """
    -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = split_alt(source)
        -------------------------------------------------------
        Parameters:
        source – a stack object
        Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        i=j=0
        target1=[]
        target2=[]
        while not self.is_empty():
            if i==j:
                target2.append(self.pop())
                i+=1
            else:
                target1.append(self.pop())
                j+=1
        return target2,target1

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are
        interlaced into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
        source1 - an array-based stack (Stack)
        source2 - an array-based stack (Stack)
        Returns:
        None
        -------------------------------------------------------
        """
        cstack=[]

        i=j=0
        while not (source2.is_empty() and source1.is_empty()):
            if i == j:
                cstack.append(source1.pop())
                i += 1
            else:
                cstack.append(source2.pop())
                j += 1
        print(cstack)



A=Stack()
c=Stack()
B=Stack()
B.push(1)
B.push(3)
B.push(4)
A.push(1)
A.push(3)
A.push(4)

c.combine(A,B)

x=[1,2,3,4,5]
x[]


