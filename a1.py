import math
import random
from binarytree import build
start = int(input("Start : " ))
end = int(input("End : " ))

n = int(input("Enter number of numbers  : "))

numbers = []
numbers = random.sample(range(start,end),n)

tree = build(numbers)
print(tree)

def dls():
    limit = int(input("ENter limit : "))
    target = int(input("Enter target "))
    path =""
    fd = 0
    maxl = 2**limit-1
    arr1 = numbers[:maxl]
    fd = dlstraversal(arr1, target, 0, path, fd)
    
    if fd==0:
        print("NOT FOUND ")
    
    print(path)

def dlstraversal(arr, target, root, path, fd):
    if root<len(arr):
        path += str(arr[root])+"--"
        if arr[root] == target:
            print(path)
            return 1
        else:

            t1 = dlstraversal(arr, target, root*2+1, path, fd)
            t2 = dlstraversal(arr,target, root*2+2, path, fd)

            if t1==1 or t2==1:
                return 1
            else:
                return 0


        
    
dls()
ids()


