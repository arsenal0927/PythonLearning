`from **https://github.com/Tony-CCIE/Python_Sort**`
**Table of Contents**
- [Python编写的排序总结](#Python编写的排序总结)
    - [1 插入排序](#1-插入排序)
    - [2 希尔排序](#2-希尔排序)
    - [3 冒泡排序](#3-冒泡排序)
    - [4 快速排序](#4-快速排序)
    - [5 合并排序](#5-合并排序)
    - [6 选择排序](#6-选择排序)
 
# Python编写的排序总结

## 1 插入排序

描述

每次假设前面的元素都是已经排好序了的，然后将当前位置的元素插入到原来的序列中，为了尽快地查找合适的插入位置，可以使用二分查找。时间复杂度$O(n^2)$，别误以为二分查找可以降低它的复杂度，因为插入排序还需要移动元素的操作！

![](https://hujiaweibujidao.github.io/images/insertionsort.png)

代码实现

```
 def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value


def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)/2
            if a_list[mid]>current_value:
                high=mid-1
            else:
                low=mid+1
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position -1
        a_list[position] = current_value


a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
insertion_sort_binarysearch(a_list)
print(a_list)
```

## 2 希尔排序

描述

类似合并排序和插入排序的结合体，二路合并排序将原来的数组分成左右两部分，希尔排序则将数组按照一定的间隔分成几部分，每部分采用插入排序来排序，有意思的是这样做了之后，元素很多情况下就差不多在它应该呆的位置，所以效率不一定比插入排序差。时间复杂度为$[O(n),O(n^2)]$。

![](https://hujiaweibujidao.github.io/images/shellsort.png)

![](https://hujiaweibujidao.github.io/images/shellsort2.png)


代码实现

```
def shell_sort(a_list):
    #how many sublists, also how many elements in a sublist
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    #start+gap is the second element in this sublist
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap] #move backward
            position = position - gap
            a_list[position] = current_value


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 88]
shell_sort(a_list)
print(a_list)
```

## 3 冒泡排序

描述

每个回合都从第一个元素开始和他后面的元素比较，如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。每次遍历都将剩下的元素中最大的那个放到了序列的“最后”（除去了前面已经排好的那些元素）。注意检测是否已经完成了排序，如果已完成就可以退出了。时间复杂度O(n^2)。

python支持对两个数字同时进行交换``` a,b = b,a ```就可以交换a和b的值了。

![](https://hujiaweibujidao.github.io/images/bubblesort.png)

代码实现

```
def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]
        pass_num = pass_num - 1


if __name__ == '__main__':
    a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
    short_bubble_sort(a_list)
    print(a_list)
 ```

## 4 快速排序

描述

通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

代码实现

```
def quick_sort(lists, left, right):
  # 快速排序
  if left >= right:
    return lists
  key = lists[left]
  low = left
  high = right
  while left < right:
    while left < right and lists[right] >= key:
      right -= 1
    lists[left] = lists[right]
    while left < right and lists[left] <= key:
      left += 1
    lists[right] = lists[left]
  lists[right] = key
  quick_sort(lists, low, left - 1)
  quick_sort(lists, left + 1, high)
  return lists
``` 

## 5 合并排序

描述

典型的是二路合并排序，将原始数据集分成两部分(不一定能够均分)，分别对它们进行排序，然后将排序后的子数据集进行合并，这是典型的分治法策略。时间复杂度$O(nlogn)$

![](http://interactivepython.org/courselib/static/pythonds/_images/mergesortA.png)

![](http://interactivepython.org/courselib/static/pythonds/_images/mergesortB.png)

代码实现

```
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

```


## 6 选择排序

描述

选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。
 
![](http://interactivepython.org/courselib/static/pythonds/_images/selectionsortnew.png)

代码实现

```
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)

```

