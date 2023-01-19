
from itertools import count

c1 = count(1,8)  # Contador infinito
r1 = range(5, 10,2) #Contador que tem um fim

# print('c1', hasattr(c1,'__iter__'))
# print('c1', hasattr(c1,'__next__'))
# print('r1', hasattr(r1,'__iter__'))
# print('r1', hasattr(r1,'__next__'))

print('Count')
for i in c1:
    if i >=8:
        break
    print(i)
print()

print('Range')
for i in r1:
    print(i)
