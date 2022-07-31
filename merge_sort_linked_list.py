from linked_list import LinkedList

# l = LinkedList()
# l.add(1)
# print(l)

def merge_sort(linked_list):
  """
  Function sorts a linked list in ascending order
    Recursibly divides the linked list into sublists containting a single node
    repeadily merge the sublists to produce sorted sublists until one remains

  Returns the sorted linked list
  """

  if linked_list.size() == 1:
    return linked_list
  elif linked_list.head is None:
    return linked_list

  # split list into left and right half, via traversing list
  left_half, right_half = split(linked_list)
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)