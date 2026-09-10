from collections import deque

list = deque()
a = "a"
b = "b"
c = "c"
print(f"list is {list}")
list.append(a)
list.append(b)
list.append(c)
print(f"list is {list}")
list.remove(b)
print(f"list is {list}")