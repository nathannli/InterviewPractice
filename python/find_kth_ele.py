import time
import random as rand


# create minheap
def minheap(arr, root_index, max_index):
    size = max_index
    l = root_index*2 + 1
    r = root_index*2 + 2
    smallest = root_index

    # find smallest value amongst root and children
    if l < size and arr[root_index] > arr[l]:
        smallest = l
    if r < size and arr[smallest] > arr[r]:
        smallest = r
        
    # if smallest is a child, swap
    if smallest != root_index:
        arr[root_index], arr[smallest] = arr[smallest], arr[root_index]
        # then check again if the swapped child should go further down
        minheap(arr, smallest, max_index)


# create maxheap    
def maxheap(arr, root_index, max_index):
    size = max_index
    l = root_index*2 + 1
    r = root_index*2 + 2
    largest = root_index

    # find largest value amongst root and children
    if l < size and arr[root_index] < arr[l]:
        largest = l
    if r < size and arr[largest] < arr[r]:
        largest = r
        
    # if largest is a child, swap
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        # then check again if the swapped child should go further down
        maxheap(arr, largest, max_index)


def heapsort(arr):
    list_size = len(arr)
    for i in arr:
        # perform minheap to get smallest num at top
        for j in range(list_size // 2 -1, -1 , -1):
            minheap(arr, j, list_size)
            # maxheap(arr, j, list_size)
        
        # move root to end of list
        # if minheap, it will go from largest to smallest
        # if maxheap, it will go from smallest to largest
        arr[0], arr[list_size -1] = arr[list_size -1], arr[0]
        # after every iteration, the total list to sort decreases by 1
        list_size -= 1


def heapsort_findk(arr, k):
    list_size = len(arr)
    for i in arr:
        # perform minheap to get smallest num at top
        for j in range(list_size // 2 -1, -1 , -1):
            # minheap(arr, j, list_size)
            maxheap(arr, j, list_size)
        
        # move root to end of list
        # if minheap, it will go from largest to smallest
        # if maxheap, it will go from smallest to largest
        arr[0], arr[list_size -1] = arr[list_size -1], arr[0]
        # after every iteration, the total list to sort decreases by 1
        list_size -= 1
        if len(arr) - list_size == k:
            # print(arr)
            return arr[list_size]



def main():
    # create random number set
    n = 10000000000000
    question_array = [ rand.randint(-1*n, n) for x in  range(1,n) ]
    # print(question_array)

    # testing if min/max heap works
    # for i in range(len(arr) // 2 - 1, -1, -1):
    #     # minheap(arr, i)
    #     maxheap(arr, i)
    # print(arr)

    # test heapsort
    # arr = question_array.copy()
    # heapsort(arr)
    # print(arr)

    # Q: find kth largest ele from random unsorted list
    start = time.process_time()
    print("start time: {}".format(start))
    arr1 = question_array.copy()
    k = 2
    print(heapsort_findk(arr1, k))
    end = time.process_time()
    print("end time: {}".format(end))
    print(end - start)

    
        




        
        



if __name__ == "__main__":
    main()

