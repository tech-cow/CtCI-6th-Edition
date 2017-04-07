#!/usr/bin/python
#coding:utf-8
#=======================================================================
# [2.5] Sum Lists: You have two numbers represented by a linked
# list, where each node contains a single digit. The digits
# are stored in reverse order, such that the 1's digit is at
# the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.

# Example: (7, 1, 6) + (5, 9, 2) -> (2,1,9)

# Space complexity: O(N)
# Time complexity: O(N)
#=======================================================================
from linkedlist import LinkedList

# 思路
# 设置一个Result，用来加每次循环出来的carry
def add_lists(ll_a,ll_b):
    n1, n2 = ll_a.head, ll_b.head
    ll = LinkedList()

    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.val
            n1 = n1.next
        if n2:
            result += n2.val
            n2 = n2.next

        ll.insert_tail(result%10)
        carry = result / 10

    #Edge case最后一个carry，当某个linkedlist没数了以后
    if carry:
        ll.insert_tail(carry)
    return ll


#Follow Up思路
#主要就是要pad两个list，写一个Lengh Compare的方法
#然后位移完了以后，写一个result来存数
#最后把int转成str，然后一个一个的往新创建的List里面塞
def add_lists_follow_up(ll_a,ll_b):
    dummy1, dummy2 = ll_a.head, ll_b.head
    len_a, len_b = ll_length(dummy1), ll_length(dummy2)

    if len_a > len_b:
        for _ in xrange(len_a-len_b):
            ll_b.insert_head(0)
    elif len_a < len_b:
        for _ in xrange(len_b-len_a):
            ll_b.insert_head(0)

    n1, n2 = ll_a.head, ll_b.head
    result = 0

    while n1 and n2:
        result = (result * 10) + n1.val + n2.val
        n1 = n1.next
        n2 = n2.next

    ll = LinkedList()
    ll.insert_multiple([int(i) for i in str(result)])

    return ll



def ll_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count



ll_a = LinkedList()
ll_a.insert_multiple([6, 9 ,9])
ll_b = LinkedList()
ll_b.insert_multiple([3, 0, 2])
print ll_a
print ll_b
print add_lists(ll_a, ll_b)
print add_lists_follow_up(ll_a, ll_b)
