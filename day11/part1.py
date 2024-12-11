
# linked list node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(-1)

def print_linked_list(node):
    print("Printing linked list")
    while node.next:
        print(node.value)
        node = node.next
    print(node.value)

with open('input.txt', 'r') as file:
    for line in file:
        input = list(map(int, line.strip().split(' ')))
        curr = head
        for num in input:
            new_node = Node(num)
            curr.next = new_node
            curr = new_node

# print_linked_list(head)

for i in range(25):
    curr = head.next
    while curr:
        next_node = curr.next
        if curr.value == 0:
            curr.value = 1
            # curr = curr.next
            
        elif len(str(curr.value)) % 2 == 0:
            index = len(str(curr.value)) // 2
            currVal = curr.value
            curr.value = int(str(currVal)[:index])
            new_node = Node(int(str(currVal)[index:]))
            new_node.next = curr.next
            curr.next = new_node
        else:
            curr.value = curr.value * 2024
        curr = next_node

# print_linked_list(head)

# calculate len(linked list)
length = 0
curr = head.next
while curr:
    length += 1
    curr = curr.next
print("length is", length)