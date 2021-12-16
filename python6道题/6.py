class Node:
    def __init__(self, init_data, init_next=None):
        self.__data = init_data
        self.__next = init_next
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    def set_data(self, new_data):
        self.__data = new_data
    def set_next(self, new_next):
        self.__next = new_next
    def __str__(self):
        return str(self.__data)  
    def add_after(self, value):
        new_node = Node(value,self.__next )
        self.__next = new_node
    def remove_after(self):  
        self.__next = self.__next.get_next()


class LinkedList:
    
    def __init__(self):
        self.__head = None		
    def add(self, item): #add to the beginning of the list
        new_node = Node(item, self.__head)
        self.__head = new_node
    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    def get_head(self):
        return self.__head
    def set_head(self, new_node):
        self.__head = new_node
    def __len__(self):
        return self.size()
    def is_empty(self):
        return self.__head == None 
    def __str__(self):
        result = ""
        if self.__head != None:    	
            current = self.__head
            while current != None:
                result = result + str(current.get_data()) + ", "
                current = current.get_next()
        return '[' + result[:-2] + ']'
    def __contains__(self,item):
        current = self.__head
        while current != None:
            if current.get_data() == item:
                return True
            else:            
                current = current.get_next()
        return False 
        
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

ll1 = LinkedList()
ll1.add(5)
ll1.add(4)
ll1.add(3)
ll1.add(2)
ll1.add(1)
print(find_maximum(ll1))


