#!/usr/bin/python
#coding:utf-8
#=======================================================================
# Yu Zhou
# [2.6] Palindrome: Implement a function to check if
# a linked list is a palindrome.

# Time Complexity: O(N)
# Space Complexity: O(N)
#=======================================================================

# 思路：
# Reverse the list and compare
from linkedlist import LinkedList

def is_palindrome(node):
    if not node:
        raise ValueError("Must enter a list")

    list_original = copy_list(node)
    list_reversed = reverse_list(node)
    list_length = get_length(node)

    #Compare
    for _ in xrange(list_length):
        if list_original.val != list_reversed.val:
            return False

        list_original = list_original.next
        list_reversed = list_reversed.next
    return True

def copy_list(node):
    new_list = LinkedList()
    while node:
        new_list.insert_tail(node.val)
        node = node.next
    return new_list.head


def reverse_list(head, prev=None):
    cur = head
    while cur:
        #print head.val
        next = cur.next #把cur这个pointer先移到next
        cur.next = prev
        prev = cur #prev reference移到head现有的位置，供下次循环使用
        print prev.val
        cur = next #把head reference移到下次循环的位置
    head = prev
    return head #这个prev也就是reverse完了以后的head

def get_length(node):
    count = 0
    while node:
        node = node.next
        count += 1
    return count


#Test
ll_false = LinkedList()
ll_false.insert_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false.head))

ll_true = LinkedList()
ll_true.insert_multiple([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true.head))
