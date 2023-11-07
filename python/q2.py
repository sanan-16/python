class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    # Merge the sorted halves
    return merge(left, right)


def find_middle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    current.next = left or right

    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original linked list:")
print_linked_list(head)

sorted_head = merge_sort_linked_list(head)
print("\nSorted linked list:")
print_linked_list(sorted_head)
