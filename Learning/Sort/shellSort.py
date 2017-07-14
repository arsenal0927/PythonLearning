# -*- coding: utf-8 -*-

'''
类似合并排序和插入排序的结合体，二路合并排序将原来的数组分成左右两部分，希尔排序则将数组按照一定的间隔分成几部分，每部分采用插入排序来排序，
有意思的是这样做了之后，元素很多情况下就差不多在它应该呆的位置，所以效率不一定比插入排序差。时间复杂度为$[O(n),O(n^2)]$。
'''

def shellSort(alist):
    #how many sublists,also how many elements in a sublist
    sublist_count = len(alist)  //2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist,start_position,sublist_count)
        print("after increments of size",sublist_count,"The list is",alist)
        sublist_count = sublist_count   //2

def gap_insertion_sort(alist,start,gap):
    #start+gap is the second element in this sublist
    for i in range(start + gap,len(alist),gap):
        current_value = alist[1]
        position = i
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap] #move backward
            position = position -gap
            alist[position] = current_value


alist = [54,26,93,17,77,31,44,55,20,88]
shellSort(alist)
print(alist)