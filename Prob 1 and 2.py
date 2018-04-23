#Michael Chau

class MinBinHeap:#taken from the implementation in section 6.10
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i): #percolates the new item up
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]: #check to swap with parent
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp #swap with parent
          i = i // 2

    def percDown(self,i): #percolates a node down the tree
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i) #get index of min child
          if self.heapList[i] > self.heapList[mc]: #if greater than min child
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp #swap with min child
          i = mc
          
    def insert(self,k):
      self.heapList.append(k) #item first becomes last leaf
      self.currentSize = self.currentSize + 1 #update size
      self.percUp(self.currentSize) #percolate it up while smaller than parents

    def minChild(self,i): #returns smallest child index
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self): #deletes minimum and returns it
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize] #root equals last leaf
      self.currentSize = self.currentSize - 1 #update size 
      self.heapList.pop() 
      self.percDown(1) #swaps down that new root while its bigger than children
      return retval

    def buildHeap(self,alist): #builds heap for inputted list
      i = len(alist) // 2 #for tree levels/indices
      self.currentSize = len(alist) #update size
      self.heapList = [0] + alist #replaces list
      while (i > 0): #keeps bringing the root down while they're bigger than child nodes
          self.percDown(i)
          i = i - 1
          
    def getList(self): #returns the heap array
        return self.heapList[1:]
    

randomList = [12,4,6,3,15,9,28,2,5]

#Problem 1
'''
Generate a random list of integers.  
Show the binary heap tree resulting from inserting
the integers on the list one at a time.
'''
prob1Heap = MinBinHeap()

for x in randomList:
    prob1Heap.insert(x)
    
print("For problem 1:")
print(prob1Heap.getList())

#Problem 2
'''
Using the list from the previous question,
show the binary heap tree resulting from the list as
a parameter to the buildHeap method.  
Show both the tree and list form.
'''
prob2Heap = MinBinHeap()

prob2Heap.buildHeap(randomList)

print("For problem 2:")
print(prob2Heap.getList())