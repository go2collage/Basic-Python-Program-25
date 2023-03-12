# Basic Python Program

# Add / Remove one item to a list
# Reverse a list

from audioop import reverse


list4 = [10, 20, 30, 40, 50]

print("Original List is: ", list4)

list4.append(60)            # append() method
print("After Adding 60 in List is: ", list4)

list4.remove(50)            # remove() method
print("After Removing 50 in List is: ", list4)

# reverse list using reverse() method

list4.reverse()             # here reverse list4 using reverse() method
print("Reverse List is: ", list4)           # now, list4 is [60, 40, 30, 20, 10]


