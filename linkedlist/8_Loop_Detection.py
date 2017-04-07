#!/usr/bin/python
#coding:utf-8
#=======================================================================
# Yu Zhou
# [2.8] Loop Detection: Given a circular linked list, implement
# an algorithm that returns the node at the beginning of the
# loop.

# Space complexity: O(1)
# Time complexity: O(n)
#=======================================================================

# 思路
# 先让他们转，通过快慢pointer的运作
# 当他们想等后，设置slow和first为pointer，再次循环，找到相交的点

def get_start_loop_node(node):
    first = node
    slow = node
    fast = node

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            loop_start_node = find_intersection(slow, first)
            return loop_start_node

    return None

def find_intersection(node1, node2):
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next

    return node1
