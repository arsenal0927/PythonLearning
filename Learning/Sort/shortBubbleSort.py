# -*- coding: utf-8 -*-

'''
每个回合都从第一个元素开始和他后面的元素比较，如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。
每次遍历都将剩下的元素中最大的那个放到了序列的“最后”（除去了前面已经排好的那些元素）。
注意检测是否已经完成了排序，如果已完成就可以退出了。
时间复杂度O(n^2)。

python支持对两个数字同时进行交换a,b = b,a就可以交换a和b的值了。
'''

def short_bubble_sort(alist):
    exchanges = True
    pass_num = len(alist) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                exchanges = True
                # temp = alist[i]
                # alist[i] = alist[i + 1]
                # alist[i + 1] = temp
                alist[i],alist[i + 1] = alist[i + 1],alist[i]   #superise!~_~
        pass_num = pass_num - 1


if __name__ == '__main__':
    alist = [20,40,30,90,60,80,70,50,110,100]
    short_bubble_sort(alist)
    print(alist)

            
