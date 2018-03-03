"""
选择排序：选择-交换-再选择-再交换……
每一轮
（1）选择最小的项
（2）放到最前面
（3）看条件是否进入下一轮

"""



def swap(lst,i,j):
	temp=lst[j]
	lst[j]=lst[i]
	lst[i]=temp

def selectionSort(lst):
	i=0
	while i<len(lst)-1:##这里只需要保证i=len(lst)-2，即倒数第二个元素是最小就可以结束了 外层每一轮目标：选出本轮最小，并交换，
		min=i
		j=i+1
		while(j<len(lst)):#内存循环结束选出本轮最小

			if lst[j]<lst[min]:
				min=j
			j+=1
		swap(lst,i,min)
		i+=1

"""
【差别】
1、我的外层循环进行了len(lst)次，书上最后一次不用？

因为在进行了len(lst)-1此排序后，已经可以保证坐标为len(lst)-2的值比len(lst)-1的值要小，不需要再比较了

2、书上是先判断min和i不相等再swap，多了一次判断，但如果相等就节约了swap运算，不知道哪种效率高？
"""

lst=[3,5,6,2,3,7]

selectionSort(lst)
print(lst)

""""
开销：
外层循环n-1次，内层循环视i而定
(n-1)+(n-2)+……+1=n(n-1)/2,
所以主要开销的复杂度是【n的平方】
另外有额外的swap的开销，最多n-1次，最少0次，平均是线性的
"""