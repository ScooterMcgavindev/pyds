from turtle import left, right
from linked_list import LinkedList
from merge_sort import merge

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

  return merge(left,right)

def split(linked_list):
  """
  Divide unsorted list @ midpoint into sublists (Sub-Linked-List)
  """
  # With list type, you can rely on midpoint using an index then list splicing into two list
  # even with an empty list passed, since no auto matic behavor have to account


  # Condition 1: if the ll is none, or empty = none
  if linked_list == None or linked_list.head = None:
    # if we call split on a linked list containing a single node
    # Left contains the node, right is none
    left_half = linked_list
    right_half = None

    return left_half, right_half

  else:
    size = linked_list.size()  # calulate size of linked list
    mid = size // 2            # find midpoint via size using floor operator % 2

    # subtract 1 as as we use size to return the midpoint
    # like the len func, size returns a value greater than the max index value (index start at zero, therfor deduct 1 to get the value)
    mid_node = linked_list.node_at_index(mid - 1)

    # assign entire ll to lefthalf
    left_half = linked_list
    # right half, assign new instance
    right_half = LinkedList()

    # after midpoint of OG ll, assign the node that comes AFTER the midpoint as the head
    right_half.head = mid_node.next_node
    # assign midpoint as tail of left list
    mid_node.next_node = None
    
    return left_half, right_half

