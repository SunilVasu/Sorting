def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       split = partition(alist,first,last)

       quickSortHelper(alist,first,split-1)
       quickSortHelper(alist,split+1,last)

def partition(alist,first,last):
   pivot = alist[first]
   left = first+1
   right = last
   done = False
   while not done:

       while left <= right and alist[left] <= pivot:
           left = left + 1

       while left <= right and alist[right] >= pivot:
           right = right -1

       if left > right:
           done = True
       else:
           temp = alist[left]
           alist[left] = alist[right]
           alist[right] = temp
   temp = alist[first]
   alist[first] = alist[right]
   alist[right] = temp
   return right

alist = [54,26,93,17,77,31,44,55,20]
print alist
quickSort(alist)
print(alist)
