class Node:
    value = None
    next = None
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "<Node: %s>" % self.value

class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def size(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter
    def find(self, key):
        current = self.head
        while current:
            if current.value == key:
                return f"Were you looking for {current}"
            current = current.next
        return f"{key} can not be found"
    
    def node_at_index(self, key):
        if key == 0:
            return self.head
        current = self.head
        counter = 0
        while counter < key:
            current = current.next
            counter = counter + 1
        return current
    
    def insert(self, value, key):
        if key == 0:
            self.add(value)
            return
        new_node = Node(value)
        current = self.head
        counter = 1
        while current:
            if counter == key:
                new_node.next = current.next
                current.next = new_node
                return
            counter += 1
            current = current.next
        return print("position not found")
    def delete(self, key):
        current = self.head
        if key == current.value:
            self.head = current.next
            return
        found = False
        prev_node = None
        while current and not found:
            if current.value == key:
                prev_node.next = current.next
                found = True
            prev_node = current
            current = current.next
        return current
    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def __repr__(self):
        arr = []
        current = self.head
        while current:
            if current is self.head:
                arr.append(f"[Head: {current}]")
            elif current.next is None:
                arr.append(f"[Tail: {current}]")
            else:
                arr.append(f"[{current}]")
            current = current.next
        return " -> ".join(arr)

 
# n = LinkedList()
# n.add(56)
# n.add(23)
# n.add("book")
# n.add(57)
# n.insert(6762, 3)
# n.delete(23)
# print(n)