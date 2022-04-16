class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)
    
    def __eq__(self, other:"Node"):
        return self.data == other.data
    
    def __ne__(self, other:"Node"):
        return self.data != other.data
    
    def __lt__(self, other:"Node"):
        return self.data < other.data
    
    def __le__(self, other:"Node"):
        return self.data <= other.data
    
    def __gt__(self, other:"Node"):
        return self.data > other.data
    
    def __ge__(self, other:"Node"):
        return self.data >= other.data
    
    def __hash__(self):
        return hash(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __str__(self):
        return 'Empty list' if self.head is None else str(self.head)
    
    def __repr__(self):
        return str(self.head)
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __getitem__(self, index):
        if index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def __setitem__(self, index, value):
        if index >= self.size:
            raise IndexError('Index out of range')
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value
    
    def __contains__(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError('Can only concatenate LinkedList with LinkedList')
        if self.head is None:
            return other
        if other.head is None:
            return self
        self.tail.next = other.head
        other.head.previous = self.tail
        self.tail = other.tail
        self.size += len(other)
        return self
    
    def __iadd__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError('Can only concatenate LinkedList with LinkedList')
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
            self.size = len(other)
            return self
        if other.head is None:
            return self
        self.tail.next = other.head
        other.head.previous = self.tail
        self.tail = other.tail
        self.size += len(other)
        return self
    
    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            return False
        if self.size != other.size:
            return False
        current = self.head
        other_current = other.head
        while current:
            if current != other_current:
                return False
            current = current.next
            other_current = other_current.next
        return True
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError('Can only compare LinkedList with LinkedList')
        if self.size < other.size:
            return True
        if self.size > other.size:
            return False
        current = self.head
        other_current = other.head
        while current:
            if current < other_current:
                return True
            if current > other_current:
                return False
            current = current.next
            other_current = other_current.next
        return False
    
    def __gt__(self, other):
        return not self < other
    
    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __bool__(self):
        return self.size > 0
    
    def __nonzero__(self):
        return self.size > 0
    
    def __hash__(self):
        return hash(self.head)
    
    def AddFirst(self, node):
        """
        Add node to the beginning of the list
        """
        if not isinstance(node, Node):
            raise TypeError('Can only add Node to LinkedList')
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.size += 1
        
    def AddAfter(self, node, new_node):
        """
        Add new node after the specified node
        """
        if not isinstance(node, Node):
            raise TypeError('Can only add Node to LinkedList')
        if not isinstance(new_node, Node):
            raise TypeError('Can only add Node to LinkedList')
        if self.head is None:
            raise ValueError('LinkedList is empty')
        if node == self.tail:
            self.AddLast(new_node)
            return
        new_node.next = node.next
        node.next.previous = new_node
        node.next = new_node
        new_node.previous = node
        self.size += 1
        
    def AddBefore(self, node, new_node):
        """
        Add new node before the specified node
        """
        if not isinstance(node, Node):
            raise TypeError('Can only add Node to LinkedList')
        if not isinstance(new_node, Node):
            raise TypeError('Can only add Node to LinkedList')
        if self.head is None:
            raise ValueError('LinkedList is empty')
        if node == self.head:
            self.AddFirst(new_node)
            return
        new_node.previous = node.previous
        node.previous.next = new_node
        node.previous = new_node
        new_node.next = node
        self.size += 1
        
    def AddLast(self, node):
        """
        Add node to the end of the list
        """
        if not isinstance(node, Node):
            raise TypeError('Can only add Node to LinkedList')
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.previous = self.tail
        self.tail = node
        self.size += 1

    def Clear(self):
        """
        Remove all nodes from the list
        """
        self.head = None
        self.tail = None
        self.size = 0
        
    def Find(self, value):
        """
        Returns the first node with the given value.
        """
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None
    
    def FindLast(self, value):
        """
        Returns the last node with the given value.
        """
        current = self.tail
        while current:
            if current.data == value:
                return current
            current = current.previous
        return None
    
    def Remove(self, node):
        """
        Remove the specified node from the list.
        """
        if not isinstance(node, Node):
            raise TypeError('Can only remove Node from LinkedList')
        if self.head is None:
            raise ValueError('LinkedList is empty')
        if node == self.head:
            self.RemoveFirst()
            return
        if node == self.tail:
            self.RemoveLast()
            return
        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1
        
    def RemoveFirst(self):
        """
        Remove the first node from the list.
        """
        if self.head is None:
            raise ValueError('LinkedList is empty')
        self.head = self.head.next
        self.head.previous = None
        self.size -= 1
        
    def RemoveLast(self):
        """
        Remove the last node from the list.
        """
        if self.tail is None:
            raise ValueError('LinkedList is empty')
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1
        
    def ToList(self):
        """
        Returns a list of the values in the list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    