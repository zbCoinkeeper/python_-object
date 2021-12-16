def  remove_at_index(l,index):
    if l.get_head() == None:
        return
    if index>l.size():
        return 

    if index == 0 :
        newHead=l.get_head().get_next()
        l.set_head(newHead)
    else:
        preHead=None
        delNode=l.get_head()
        while index>0:
            preHead=delNode
            delNode=delNode.get_next()
            index=index-1
        preHead.set_next(delNode.get_next() if delNode!=None else None)



def find_maximum(l):
    if l.get_head() == None:
        return
    max=0
    newHead=l.get_head()
    while newHead!=None:
        if max < newHead.get_data():
            max=newHead.get_data()
        newHead=newHead.get_next()
    return max




ll1 = LinkedList()
ll1.add(5)
ll1.add(4)
ll1.add(3)
ll1.add(2)
ll1.add(1)
print(find_maximum(ll1))