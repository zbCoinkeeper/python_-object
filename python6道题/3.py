import copy

def mirror_list(l):
    m=copy.deepcopy(l)
    m.reverse()
    for i in range(len(m)):
        l.append(m[i])

l = [1, 2, 3, 4, 5]
mirror_list(l)
print(l)

