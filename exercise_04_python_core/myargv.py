import sys

a = sys.argv
a.pop(0)
a = map(lambda x: int(x), a)
print(sum(a))
