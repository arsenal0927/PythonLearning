# -*- coding: utf-8 -*-

'''
典型的是二路合并排序，将原始数据集分成两部分(不一定能够均分)，
分别对它们进行排序，然后将排序后的子数据集进行合并，这是典型的分治法策略。
时间复杂度$O(nlogn)$
'''

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) //2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j <len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging ",alist)

alist = [54,34,65,33,56,23,67,21,47,36]
mergeSort(alist)
print(alist)