from typing import Optional
import math

class LLNode :

    def __init__(self , data ):

        self.data = data
        self.next: Optional[LLNode] = None
        
class DLLNODE(LLNode):
    def __init__(self, data):
        super().__init__(data)
        self.next : Optional[DLLNODE] = None
        self.prev: Optional[DLLNODE] = None

class LinkedList:
  
  def __init__(self):
      self.head : Optional[LLNode] = None
      
    
  def search(self , x):
      
      return self._search_recursively(self.head , x)

  def _search_recursively(self , node : Optional[LLNode] , x):
      
      if node is None:
         print("item not found")
         return None
    
      if node.data == x:
        return node
    
      else:
         return self._search_recursively(node.next , x)


  def insert(self , x):
    
    newnode = LLNode(x)

    newnode.next = self.head
    self.head = newnode


  def itemAhead(self , node : Optional[LLNode] , x):
    # helper method to find the predeccessor of a node in a linked list
      if node == None or node.next == None:
        return None
    
      if node.next.data == x:
        return node 
      else: 
          return self.itemAhead(node.next , x)

  def delete(self , x):
    
    if self.head is None:
        return None
    
    if self.head.data == x:
        self.head = self.head.next
        return None
    
    pred  = self.itemAhead(self.head , x)

    if pred is not None and pred.next is not None: 
        pred.next =pred.next.next
        print(f"ITEM {x} DELETED LOL")
    else:
        print(f"ITEM {x} NOT FOUND")


  def reverselist(self):
    
    pred = None
    current = self.head

    if self.head is None or self.head.next is None:
        return self.head

    
    while current is not None:

        nextnode = current.next
        current.next = pred

        pred = current
        current = nextnode

    self.head = pred
    print("LIST REVERSED :) HOPE U LOVE SMELLING ASS")

class DoubleLinkedList(LinkedList):
      def __init__(self):
          super().__init__()

          self.head : Optional[DLLNODE] = None 
          self.tail :Optional[DLLNODE] = None

      def insert(self , x):
          newnode = DLLNODE(x)

          if self.head is None:
              self.head = newnode
              self.tail = newnode
          else:
              newnode.next = self.head
              self.head.prev =  newnode
              self.head = newnode  

      def Addtoend(self , x):
          newnode = DLLNODE(x)

          if self.tail is None:
              self.head = newnode
              self.tail = newnode
          else:
              self.tail.next = newnode
              newnode.prev = self.tail
              self.tail = newnode                 
      def delete(self , x):
          
          current = self.head

          while current is not None:
              if current.data == x:
                  
                  if current == self.head:
                      
                      self.head = current.next
                      if self.head:
                          self.head.prev = None
                      else:
                          self.tail = None

                  elif current == self.tail:
                      self.tail = current.prev
                      
                      if self.tail:
                        self.tail.next = None  

                  else:

                      current.prev.next = current.next  # type: ignore
                      current.next.prev = current.prev   # type: ignore

                  return
              current = current.next

          print("item Not FOUND")  

      def reverseDLL(self):
          current = self.head
          temp = None
          self.tail = self.head

          while current is not None:
              temp = current.prev
              current.prev = current.next
              current.next = temp
              current = current.prev
          if temp is not None:
              self.head = temp.prev
                           
class TreeNode:

    def __init__(self , data):

        self.data = data 
        self.parent: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.left: Optional[TreeNode] = None

class binarysearchtree:

    def __init__(self):
        self.root:Optional[TreeNode] = None
    



    def  _search_recursivly(self , Node : Optional[TreeNode] , x):
      if Node is None:
        return None
      if Node.data == x:
        return Node
      if x < Node.data :
         return self._search_recursivly(Node.left , x)
      else:
         return self._search_recursivly(Node.right , x)

    def searchTree(self , x):

        return self._search_recursivly(self.root , x)


    def findMin(self , Node : Optional[TreeNode]):

        if Node == None :
            return None

        min = Node

        while min.left != None:
            min = min.left
        return min

    def findMax(self,node : Optional[TreeNode]):

        if node == None:
            return None
        
        max = node

        while max.right != None:
            max = max.right
        return max


    def get_inorder_traversal(self):
       
       result_list = []
       
       self._traversetree(self.root , result_list)
       
       return result_list


    def _traversetree(self , node : Optional[TreeNode] , resultlist : list):
 
        if node is not None:
            self._traversetree(node.left , resultlist)
            print(f"{node.data}" , end="")
            resultlist.append(node.data)
            self._traversetree(node.right , resultlist)
          

    def inserttree(self , x):
        newnode = TreeNode(x)

        if self.root == None:
            self.root = newnode
            return
        
        current = self.root

        while current is not None:

            parent = current

            if newnode.data < current.data:
                current = current.left
            elif newnode.data > current.data:
                current = current.right
            else: 
                return
        if newnode.data < parent.data :
            
            parent.left = newnode 
        else:
            parent.right = newnode
        newnode.parent = parent    


    def _deleteleafnode(self , Nodetodelete : TreeNode):
        parent = Nodetodelete.parent

        if parent is None :
            self.root = None
        elif parent.left == Nodetodelete:
            parent.left = None 
        else: 
            parent.right = None

    def _delet_node_with_one_child(self , node : TreeNode):

        parent = node.parent 

        if node.left is not None:
            child = node.left
        else:
            child = node.right    
        
        if parent is None:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child  
      

        child.parent = parent            # type: ignore
    

    def _deletewith2children(self , node : TreeNode):
        
        successor = self.findMin(node.right)

        if successor is not None:

          node.data = successor.data

          if successor.left is None and successor.right is None :
            self._deleteleafnode(successor)
          else:
            self._delet_node_with_one_child(successor)

        else:
            return        

    def deletenode(self , x):

        node_to_delete = self.searchTree(x)

        if node_to_delete is None:
            print(f"node with value {x} is not found ")
            return
        
        if node_to_delete.left is None and node_to_delete.right is None:
            self._deleteleafnode(node_to_delete)
        elif node_to_delete.left is None or node_to_delete.right is None:
            self._delet_node_with_one_child(node_to_delete)
        else:
            self._deletewith2children(node_to_delete) 

    def findDepth(self):
        if self.root == None:
            return 0
        
        depth = 1
        maxdepth = 0
        unvistednodes = Stack()
        olddepths = Stack()
        
        current = self.root

        while current:
            
            if depth > maxdepth:
                maxdepth = depth

            if  current.left != None and current.right != None:
                unvistednodes.push(current.left)
                olddepths.push(depth+1)
                current = current.right
                depth += 1

            elif current.left != None:
                current = current.left
                depth += 1
            elif current.right != None:
                current = current.right
                depth += 1
            else:

                if unvistednodes.isempty():
                 break
                
                current = unvistednodes.Pop()
                depth = olddepths.Pop()
            
        return maxdepth     

class Stack:

    def __init__(self):

        self._items = []

    def push(self , item):

        self._items.append(item)    

    def isempty(self):

        return not self._items

    def Pop(self):

        if not self.isempty():

            return self._items.pop()

        raise IndexError("pop from an empty stack")    
    
    def peek(self):

        if not self.isempty():

            return self._items[-1]
        
        raise IndexError("stack is empty")
    
    def findmin(self):

        if not self.isempty():
           champion = math.inf

           for item in self._items:
               if item < champion:
                   champion = item

           return champion           
        
        raise IndexError("stack is empty")

class Queue:

    def __init__(self):
        self.front: Optional[LLNode] = None
        self.rear: Optional[LLNode] = None

    def enqueue(self , item):
        
        newnode = LLNode(item)

        if self.rear is None:
            self.front = newnode
            self.rear = newnode
        else:
          self.rear.next = newnode
          self.rear = newnode

    def dequeue(self): 

       if self.front is None:
           raise IndexError("QUEUE IS EMPTY")
       
       removed_item = self.front.data

       self.front = self.front.next

       if self.front is None:
           self.rear = None

       return removed_item
    
    def isEmpty(self):

        if self.front is None:
            return True
        
        return False
      
    def findmax(self):

        if self.front is None:
            return None
        
        current = self.front

        champion = -math.inf

        while current:
            if current.data > champion:
                champion = current.data
            current = current.next
        return champion        

    def findmin(self):

        if self.front is None:
            return None
        
        current = self.front

        champion = math.inf

        while current:
            if current.data < champion:
                champion = current.data
            current = current.next
        return champion        