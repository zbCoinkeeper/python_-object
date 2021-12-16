class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items ==[]:
            return print('this is empty')
        else :
            return print('裡面還有值')
    def enqueue(self, item): # 從list index = 0 處開始加入item
        self.items.insert(0,item)

    def dequeue(self):       # 從list index = -1 處del item
        return self.items.pop()

    def size(self):
        return len(self.items)

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right
    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, left=self.__left)
            self.__left = tree
    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, right=self.__right)
            self.__right = tree
    def get_left(self):
        return self.__left
    def get_right(self):
        return self.__right
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data
    def set_left(self, left):
        self.__left = left
    def set_right(self, right):
        self.__right = right


def sum_leaves(l):
    sum=left_num=right_num=0
    if l.get_left() == None and l.get_right() == None:
        sum=l.get_data()+sum
    if l.get_left() !=None:
        left_num=sum_leaves(l.get_left())
    if l.get_right() !=None:
        right_num=sum_leaves(l.get_right())
    return  sum+left_num+right_num



def breadth_traversal(root):
    nodeQuene = []
    result = []
    if not root:
        return result
    nodeQuene.append(root)
    while nodeQuene:
        queneLength = len(nodeQuene)
        for i in range(0, queneLength):
            currentNode = nodeQuene.pop(0)
            if currentNode.get_left():
                nodeQuene.append(currentNode.get_left())
            if currentNode.get_right():
                nodeQuene.append(currentNode.get_right())
            result.append(currentNode.get_data())
    return result

t1 = BinaryTree(5)
t1.insert_left(2)
t1.insert_left(3)
t1.insert_right(1)
t1.insert_right(4)
print(breadth_traversal(t1))


