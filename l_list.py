class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_by_index(self, index):
        if index < 0:
            print("invalid index :(")
            return

        current = self.head
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if not current:
            print("index out of range")
            return

        prev.next = current.next

    def delete_by_value(self, value):
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if not current:
            print("Value not found in linked list")
            return

        prev.next = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def append_at_index(self, data, index):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        if index < 0:
            print("invalid index :(")
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            print("index out of range")
            return

        new_node.next = current.next
        current.next = new_node

    def simple_sort(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

    def insert_into_sorted(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "\n".join(nodes)


# checkedy check
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Initial List:")
print(ll)

print("reversed list")
ll.reverse_list()
print(ll)

print("append at index")
ll.append_at_index(70, 2)
print(ll)

print("\nDelete at index 2:")
ll.delete_by_index(2)
print(ll)

print("\nDelete value 20:")
ll.delete_by_value(20)
print(ll)

print("Unsorted List:")
print(ll)

print("\nSorting the list:")
ll.simple_sort()
print(ll)

print("\nInserting 25 into the sorted list:")
ll.insert_into_sorted(25)
print(ll)

print("\nInserting 5 into the sorted list:")
ll.insert_into_sorted(5)
print(ll)

print("\nInserting 50 into the sorted list:")
ll.insert_into_sorted(50)
print(ll)
