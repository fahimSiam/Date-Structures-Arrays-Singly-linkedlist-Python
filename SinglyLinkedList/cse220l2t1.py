# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:18:02 2021

@author: My Baby
"""
class Node: 
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    
    def printNode(self):
        print(self.value)
        

        
class MyList:
   head= None
   def __init__(self, arr=None):
       # self.list = []
        
        if arr is None:
            self.head=None
            
        elif isinstance(arr, list):
            if len(arr) == 0:
                raise ValueError('Array cannot be empty')
            else:
               
                tail = None
                for i in range(0, len(arr)):
                    newNode = Node(arr[i], None)
                    if(self.head == None):
                        self.head = newNode
                        tail = newNode
                    else:
                        tail.next = newNode
                        tail = newNode
            
            
        elif isinstance(arr, MyList):
         
            tail = None
            if len(arr.list) == 0:
                raise ValueError('List cannot be empty')
            else:
                n=arr.head
                newNode = Node(n.value, None)
                self.head=newNode
                tail=newNode
                while(n is not None):
                    newNode1 = Node((n.next).value, None)
                    tail.next=newNode1
                    n=n.next
        else:
            raise TypeError('Unknown type for a')
    
    
    
   def countNode(self):
        count=0
        currentNode=self.head
        while(currentNode is not None):
            currentNode=currentNode.next
            count+=1
        return count
    
    
    
   def nodeAt(self,size, index):
        if(index<0 or index>=size):
            raise Exception("Invalid index")
        n = self.head
        for i in range(0,index):
            n = n.next
        return n        


   def showList(self):
        n= self.head
        while(n is not None):
            n.printNode()
            n=n.next
            
    
   def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False

   def insert(self,elem,index=None):
        if(index==None):
            currentNode=self.head
            newNode= Node(elem, None)
            while currentNode.next is not None:
                currentNode=currentNode.next
            currentNode.next=newNode
        else:
            newNode= Node(elem, None)
            if (index==0):
                newNode=self.head
            else:
                index1=0
                currentNode=self.head
                while index1 is not index-1:
                    currentNode=currentNode.next
                    index1+=1
                temp=currentNode
                newNode.next= currentNode.next
                temp.next =newNode
        
   def clear(self):
        temp = self.head
        while(temp is not None):
            temp2 = self.head
           # head=head.next
            temp2.value=None
            temp2.next=None
            temp=temp.next
        print("is empty done")
        
        
   
    
    
   def remove(self,elem):
       
        removedNode = None
        temp=self.head
        if (temp.value==elem):
    
            removedNode = temp.value
            self.head = temp.next
    
        else:
            temp = self.head
            while(temp.next is not None):
                if (temp.next.value==elem):
                    removedNode = temp.next.value  
                    temp.next = temp.next.next
                temp=temp.next
        return removedNode


#TASK 3
        
 #TASK3.1   
   def evenNumber(self):
       temp=self.head
       if(temp.value%2!=0):
           list2.remove(temp.value)
       while(temp.next is not None):
           if(temp.value%2!=0):
               list2.remove(temp.value)
           
           temp=temp.next
       list2.showList()
       
       
           
  #TASK 3.2 
   def find(self, elem):
       temp=self.head
       if (temp.value==elem):
            return True
    
       else:
            temp = self.head
            while(temp.next is not None):
                if (temp.next.value==elem):
                    return True
                temp=temp.next
       return False
    

#TASK.3.5
   def printSum(self):
       sum=0
       temp=self.head
       while(temp.next is not None):
           sum=sum+temp.value
           temp=temp.next
       sum+=temp.value
       return sum
       
   
   #TASK3.3 
   def reverse(self):
        prev = None
        currentNode = self.head
        while(currentNode is not None):
            next = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = next
        self.head = prev


#TASK 3.4
   def sortList(self):
      currentNode = self.head;  
      index = None;  
        
      if(self.head == None):  
          return;  
      else:  
          while(currentNode != None):  
              index = currentNode.next;  
                
              while(index != None):  
                  if(currentNode.value > index.value):  
                      temp = currentNode.value;  
                      currentNode.value = index.value;  
                      index.value = temp;  
                  index = index.next;  
              currentNode = currentNode.next;  



    

   def rotateLeft(self):

       oldHead = self.head
    
       self.head = self.head.next
    
       tail = self.head
    
       while(tail.next is not None):
    
           tail = tail.next
    
       tail.next = oldHead
    
       oldHead.next = None

   def rotateRight(self):
      
       tail=self.head
       while(tail.next.next is not None):
    
           tail = tail.next
       n=tail
       tail=tail.next
       tail.next=self.head
       self.head=tail
       n.next=None

 #TASK 3.6:
   def rotate(self, a, n):
       for i in range(0,n):
           if(a=='left'):
               list2.rotateLeft()
           elif(a=='right'):
               list2.rotateRight()
    

list1= [1,2,4,4,5,6]
list2= MyList(list1)
print("array to list and list to list")
list2.showList() 
print("check if list is empthy")
print(list2.isEmpty())
list2.showList() 
print("insert at end")
list2.insert(7) 
list2.showList()
print("insert at 3rd index")
list2.insert(7,3) 
list2.showList()
print("remove element")
print(list2.remove(4))
print("Only keep even number")
list2.evenNumber()
print("check if value exsist")
print(list2.find(7))
print("print sum:")
print(list2.printSum())
print("reverse:")
list2.reverse()
list2.showList()
print("Sorting list:")
list2.sortList()
list2.showList()
print("Rotating the List right By 2")
list2.rotate('right',2)
list2.showList()
print("Rotating the left right By 2")
list2.rotate('left',2)
list2.showList()
print("Kept the clear method at the last")
list2.clear()

