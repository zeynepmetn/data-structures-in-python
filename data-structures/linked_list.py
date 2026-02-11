class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None
    
    def setNextNode(self, node):
        self.nextnode = node

    def setPrevNode(self, node):
        self.prevnode = node
    
    def getNextNode(self):
        return self.nextnode
    
    def getPrevNode(self):
        return self.prevnode
    
    def getNodeValue(self):
        return self.value
    
Ankara = DoublyLinkedList("06")
Corum = DoublyLinkedList("19")
Samsun = DoublyLinkedList("55")

Ankara.setNextNode(Corum)
Corum.setPrevNode(Ankara)
Corum.setNextNode(Samsun)
print(Samsun.getPrevNode())