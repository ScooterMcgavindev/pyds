from hashlib import new


new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list: print(True)

for n in new_list:
  if n == 1:
    print(True)

    break

# add to a list
new_list.append(4)
new_list.extend([5, 6, 7])

# inserting in a list
new_list.insert(0, 10)

# delte specific value in a list
new_list.remove(4)
print(new_list)