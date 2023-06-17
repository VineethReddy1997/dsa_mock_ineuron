# ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to add two numbers represented as linked lists
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        curr.next = ListNode(carry % 10)
        carry //= 10
        curr = curr.next

    return dummy.next

# user to enter the values for the first linked list

l1_values = input("Enter the values for the first linked list in reverse order (separated by comma): ").split(',')
l1 = ListNode(int(l1_values[0]))
current_node = l1
for val in l1_values[1:]:
    current_node.next = ListNode(int(val))
    current_node = current_node.next

# user to enter the values for the second linked list
l2_values = input("Enter the values for the second linked list in reverse order (separated by comma): ").split(',')
l2 = ListNode(int(l2_values[0]))
current_node = l2
for val in l2_values[1:]:
    current_node.next = ListNode(int(val))
    current_node = current_node.next

# Call the function to add the two numbers
result = addTwoNumbers(l1, l2)

# Print the resulting linked list
while result:
    print(result.val, end=" ")
    result = result.next
