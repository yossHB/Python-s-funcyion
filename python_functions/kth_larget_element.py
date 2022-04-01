import heapq #complexity O(n+klogn)
def kth_larget(arr,k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
print(kth_larget_element([4,2,1,9,5,6,7,3],4))

#This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
