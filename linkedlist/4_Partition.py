#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
# [2.4] Partition: Write code to partition a linked list around
# a value x, such that all nodes less than x come before all
# nodes greater than or equal to x. If x is contained within
# the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear
# anywhere in the "right partition"; it does not need to appear
# between left anr right partitions.

# EXAMPLE
# Input: 3, 5, 8, 5, 10, 2, 1 (partition = 5)
# Output: 3, 1, 2, 10, 5, 5, 8

# Space complexity: O(1)
# Time complexity: O(N)
#=======================================================================

# High level
# keep track of two lists
# add nodes less than partition to one list
# add remaining nodes to the second
# append them and return the head

from linkedlist import LinkedList
from linkedlist import Node

def partition_list(ll, x):
    dummy1, dummy2 = Node(0), Node(0)
    cur1, cur2 = dummy1, dummy2
    head = ll.head

    while head:
        if head.val < x:
            cur1.next = head
            cur1 = cur1.next
        else:
            cur2.next = head
            cur2 = cur2.next
        head = head.next

    cur2.next = None
    cur1.next = dummy2.next

    return dummy1.next


#多谢了个display的方程，LinkedList自带的方程打印出来很诡异
def display(dummy1):
    arr = []
    while dummy1:
        arr.append(str(dummy1.val))
        dummy1 = dummy1.next
    print " -> ".join(arr)


ll = LinkedList()
ll.insert_multiple([6, 7, 8, 9, 5, 2, 1, 3, 4])
print(ll)
display(partition_list(ll, 6))
