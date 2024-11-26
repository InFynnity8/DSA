import sys
import os
sys.path.append(os.path.abspath("/Users/DOH/Desktop/dsa/Data_structures"))
from linked_list import LinkedList

def merge_sort(linked_list):
    if linked_list.size() == 1:
        return linked_list
    if linked_list.head is None:
        return linked_list
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def split(linked_list):
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    size = linked_list.size()
    mid = size//2
    mid_node = linked_list.node_at_index(mid-1)
    left_half = linked_list
    right_half = LinkedList()
    right_half.head = mid_node.next
    mid_node.next = None
    return left_half, right_half

def merge(left, right):
    merged = LinkedList()
    merged.add(0)
    left_head = left.head
    right_head = right.head
    current = merged.head
    while left_head or right_head:
        if left_head is None:
            current.next = right_head
            right_head = right_head.next
        elif right_head is None:
            current.next = left_head
            left_head = left_head.next
        else:
            left_value = left_head.value
            right_value = right_head.value
            if left_value < right_value:
                current.next = left_head
                left_head = left_head.next
            else:
                current.next = right_head
                right_head = right_head.next
        current = current.next
    head = merged.head.next
    merged.head = head
    return merged



u = LinkedList()
unsorted = [23,23,54,5,43,1,5,2,5,7,2,45,656,34,100]

for i in unsorted:
    u.add(i)

print(u)
sorted = merge_sort(u)
print(sorted)