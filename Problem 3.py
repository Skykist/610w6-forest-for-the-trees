#Michael Chau
#Problem 3
#from http://interactivepython.org/runestone/static/pythonds/Trees/ParseTree.html

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    #inserted/changed pretty much only this part
    fplist = []
    num = ''
    
    for char in fpexp:
        if char not in ['(', '+', '-', '*', '/', ')']:
            if num == '': 
                num = char #replace num with char
            else: #if num is not an empty string
                num = num + char #add char strings
        else:
            if num != '': #to not append empty strings
                fplist.append(num) 
            fplist.append(char)
            num = '' #reset num
    
    #print(fplist)
    
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("((10+5)*3)")
pt.postorder()  #defined and explained in the next section
