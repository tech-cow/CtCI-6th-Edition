#!/usr/bin/python
#coding:utf-8
#=======================================================================
# Yu Zhou
# [2.7] Intersection: Given two (singly) linked lists,
# determine if the two lists intersect. return the
# intersecting node. Note that the intersection is
# defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same
# (by reference) as the jth node of the second linked
# list, then they are intersecting.

# Space complexity: O(1)
# Time complexity: O(n)
#=======================================================================
from linkedlist import LinkedList
from linkedlist import Node

#先pad，然后比对
def find_intersection(node1, node2):
    dummy1, dummy2 = node1, node2
    len1, len2 = get_length(dummy1), get_length(dummy2)
    diff = abs(len1 - len2)

    #Set Node
    shorter_node = node1 if len1 < len2 else node2
    longer_node = node2 if len1 < len2 else node1

    #Padding
    for _ in range(diff):
        longer_node = longer_node.nexts

    while shorter_node != longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def get_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count

#Test
intersection = Node(5)
ll1 = LinkedList()
ll1.insert_multiple([1,2,3])

ll2 = LinkedList()
ll2.insert_multiple([1,2,3])

#位移
cur1 = ll1.head
while cur1.next:
    cur1 = cur1.next
cur1.next = intersection

#位移
cur2 = ll2.head
while cur2.next:
    cur2 = cur2.next
cur2.next = intersection

#两个链表都指向5了，expect to get 5
print find_intersection(ll1.head, ll2.head).val
