#!/usr/bin/python
#coding:utf-8
from linkedlist import LinkedList

# Yu Zhou
# [2.2] Return Kth to Last: Implement an algorithm to find
# the kth to last element of a singly linked list.

# 方法一
# 超级无敌Brute Force
# 遍历一遍，然后设置一个Counter，通过这个Counter减去Kth位，然后返回
# Space complexity: O(1)
# Time complexity: O(N)

def get_kth_to_last_node(ll, k):
    counter = 0
    cur = ll.head

    while cur:
        cur = cur.next
        counter += 1

    cur = ll.head #重新设置cur

    for _ in xrange(counter - k):
        if cur.next:
            cur = cur.next
    return cur


# 方法二
# 位移K位，CtCi经典解法
# 设置两个pointer，第一个先提前位移k位，然后再两个pointer一同位移
# Space complexity: O(1)
# Time complexity: O(N)
def get_kth_to_last_node_2(ll, k):
    p1 = p2 = ll.head
    for _ in xrange(k):
        try:
            p1 = p1.next
        except AttributeError:
            raise Exception('k must be smaller than length of list - 1')

    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2


ll = LinkedList()
ll.generate()
print(ll)
print(get_kth_to_last_node(ll,3).val)
print(get_kth_to_last_node_2(ll,3).val)
