#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Singly Linked List
#=======================================================================
from random import randint

class Node(object):
    #Constructor
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList(object):
    #Constructor
    def __init__(self, head = None, size = None):
        self.head = head
        self.size = size

    #Display
    def display(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print "->".join(res)

    #在头Insert
    def insert_head(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp = Node(val) #创建Temp Node
            temp.next = (self.head)  #指向Head
            self.head = temp #把head的reference改到这个Temp Node

    #在末尾Insert
    def insert_tail(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            cur = self.head
            temp = Node(val)
            while cur.next:  #位移
                cur = cur.next
            cur.next = temp

    #Random多位数Insert
    def insert_multiple(self):
        for _ in xrange(10):
            self.insert_tail(randint(0,9))

    


#   Search: 寻找LinkedList拥不拥有某个数，没有则返回Error
#   Delete: 先调用Search，然后删除。Search不到则返回Error

#Test
ll = LinkedList()
ll.insert_multiple()
ll.display()
