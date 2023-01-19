from itertools import zip_longest

l1 = [1,2,3,4,5,6,8]
l2 = [1,2,3,4]

# def soma_listas(l1, l2):
#     max_interval = min(len(l1), len(l2))
#     return [
#         l1[i] + l2[i]
#         for i in range(max_interval)
#     ]
# OldSchool Solution
def wich_min_list(li1, li2):
   if len(li1) < len(li2):
      return li1
   return li2

#print(wich_min_list(l1, l2))

def old_way_sum(l1, l2):
    min_list = wich_min_list(l1, l2)
    soma_list = []
    for i in range(len(min_list)):
        soma_list.append(l1[i] + min_list[i])
    print(f'From Function OldWay: {soma_list}')

old_way_sum(l1, l2)

def sum_with_enumerate(l1, l2):
    sumed = []
    for i, _ in enumerate(l2):
        sumed.append(l1[i] + l2[i])
    print(f'With Enumerate: {sumed}')


sum_with_ziptool = [
    x + y
    for x,y in zip(l1, l2)]
print(f'With Zip and ListComp {sum_with_ziptool}')

sum_with_enumerate(l1, l2)

# Fill value para itens restantes em ZIP_LONGEST
sum_with_ziplongest = [
    x + y
    for x,y in zip_longest(l1, l2, fillvalue=0)
]

print(f'With ZipLongest {sum_with_ziplongest}')

# ln = soma_listas(l1, l2)
# print(soma_listas(l1, l2))
