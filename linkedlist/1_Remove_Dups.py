from linkedlist import LinkedList

# Yu Zhou
# [2.1] Write code to remove duplicates from an
# unsorted linked list. What if a temporary buffer
# is not allowed?

# Hash Table
# Space complexity: O(N)
# Time complexity: O(N)
def remove_dups(ll, prev=None):
    head = ll.head
    cur = ll.head
    hash = {}

    while cur:
        if cur.val in hash:
            prev.next = cur.next
        else:
            hash[cur.val] = 1
        prev = cur
        cur = cur.next
    return head


# 2 Pointers (Runner Methods)
# Space complexity: O(1)
# Time complexity: O(N^2)
def remove_dups_2(ll, val):
    head = ll.head
    cur = ll.head
    runner = ll.head

    while cur:
        prev = runner
        runner = runner.next

        if runner and runner.val == cur.val:
            prev.next = runner.next
            runner = runner.next

        if runner == None:
            cur = cur.next
            runner = cur
    return head


#Some Tests:
ll = LinkedList()
ll.generate()
print(ll)
remove_dups_2(ll, 3)
print(ll)
