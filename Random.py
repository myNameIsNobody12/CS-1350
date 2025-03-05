import random
li = []
def liRand(lst):
    for i in range(5):
    #    li.append(random.randrange(10,20)) #option 1 (much better)
        lst = lst + [random.randrange(10,20)]
    return lst
li = liRand(li)
print(li)
