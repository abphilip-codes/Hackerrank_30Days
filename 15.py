# https://www.hackerrank.com/challenges/30-linked-list/problem

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        n = Node(data)
        if head == None:
            return n
        else:
            p = head   
            while p.next != None:
                p = p.next
            p.next = n    
            return head    

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  