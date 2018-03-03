"""
合并排序：
（1）数组对半分成2个，再分成4个……一直到只有1个 从上到下
（2）对最小的列表排序  在最下
（3）合并  从下到上
写起来有点困难，主要是各个功能怎么配合

具体是两个子列表怎么按有序的方式合并：
开第三个列表作为结果列表，然后两个指针，分别指向两个子列表的开头，两者相比值较小的放进结果列表，然后指针后移

"""
#一个思路：像这种不知道要拆分多少次的适合用递归而不是循环
#明确：在一个递归里完成的事情是，当前列表拆分成2个与这2个列表的合并


def mergeSort(lst):
	left=0
	right=len(lst)-1
	copyBuffer = list(range(len(lst)))#必须提前指定大小，否则不能直接对下标为index的元素赋值
	if (left < right):
		divide(lst,left,right, copyBuffer)

def divide(lst,left, right, copyBuffer):
	if (left<right):#如果列表不止1个元素，就拆成两个列表，然后以排序的方式合并
		mid=(left+right)//2
		divide(lst,left,mid,copyBuffer)
		divide(lst,mid+1,right,copyBuffer)
		merge(lst,left,mid,right,copyBuffer)

def merge(lst,left,mid,right,copyBuffer):
	#两个子列表lst[left：mid+1]和[mid+1：right+1]
	l1=left
	l2=mid+1
	i=left
	while (i<right+1):#填满下标为left-right的元素
		if (l1>mid):#l1 exausted
			copyBuffer[i]=lst[l2]
			l2+=1
		elif (l2>right):#l2 exausted
			copyBuffer[i]=lst[l1]
			l1+=1
		elif (lst[l1]<lst[l2]):
			copyBuffer[i]=lst[l1]
			l1+=1
		else:

			copyBuffer[i]=lst[l2]
			l2+=1
		i+=1
	for i in range(left,right+1):
		lst[i]=copyBuffer[i]



#测试
import random
lst=[]
for count in range(20):
	lst.append(random.randint(1,100))
print('raw lst:',lst)
mergeSort(lst)
print('after fast sort:',lst)

"""
复杂度分析：
n*log（n）？
"""