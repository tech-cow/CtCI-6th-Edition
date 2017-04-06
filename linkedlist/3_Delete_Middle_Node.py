#!/usr/bin/python
#coding:utf-8
from linkedlist import LinkedList

# [2.3] Delete Middle Node: Implement an algorithm to delete a
# node in the middle (i.e., any node but the first and last
# node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.

# Space complexity: O(1)
# Time complexity: O(N)

#因为题目有说，确定不是tail，所以这里可以直接node.next.next，否则会 null.next出错
def delete_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next


#Test
ll = LinkedList()
ll.insert_multiple([1,2,3,9,10,11])
#Get mid point:
cur = ll.head
for _ in xrange(3):
    cur = cur.next
ll.display()

#This should delete 9
delete_middle_node(cur)
ll.display()
