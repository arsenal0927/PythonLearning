
def insertionSort(alist):
    for index in range(1,len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position = position-1
        alist[position] = current_value


def insertionSortBinarysearch(alist):
    for index in range(1,len(alist)):
        current_value = alist[index]
        position = index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)/2
            if alist[mid]>current_value:
                high=mid-1
            else:
                low=mid+1
        
        while position > low:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = current_value


alist = [54,26,93,15,77,44,55,20]
insertionSort(alist)
print(alist)
insertionSortBinarysearch(alist)
print(alist)