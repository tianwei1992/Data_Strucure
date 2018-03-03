"""
冒泡算法
每一轮：通过两两比较将最大值排到最后
"""


def swap(lst,i,j):
	temp=lst[j]
	lst[j]=lst[i]
	lst[i]=temp

def bubbleSort(lst):
	i=len(lst)-1
	while (i>0):
		j=0
		while(j<i):
			if lst[j]>lst[j+1]:

				swap(lst,i,j)
			j+=1
		i-=1



lst=[3,5,6,2,3,7]

bubbleSort(lst)
print(lst)


"""
复杂度：

外层循环n-1轮，第一轮保证下标n-1是最大，第2轮保证n-2轮最大，第n-1轮保证下标1最大
内层循环的轮数不同，j从0开始，到i-1结束
所以总共是(n-1)+(n-2)+……+1=（n-1）n/2
主要开销还是n的平方，额外swap开销最小0次，最坏情况下，也会是n的平方……
"""

"""
改进：上述算法还有可以改进的地方！

假如第一轮冒泡全程没有发生交换，说明列表顺序已经排列好，就不需要进行下一轮了
于是可以改进如下：

不过这种改进也只能改进较好情况下的效率，如果最好最好，第1轮循环后就排好不用再继续的话，复杂度就是线性阶……不过在大多数普通情况下仍然是n的平房
"""


def swap(lst, i, j):
	temp = lst[j]
	lst[j] = lst[i]
	lst[i] = temp


def bubbleSort(lst):
	i = len(lst) - 1
	while (i > 0):
		swapped=False#每一轮加一个标志位，用于标志毛包过程中是否发生了交换
		j = 0
		while (j < i):
			if lst[j] > lst[j + 1]:
				swap(lst, i, j)
				swapped=True
			j += 1
		if (swapped==False):
			return
		i -= 1


lst = [3, 5, 6, 2, 3, 7]

bubbleSort(lst)
print(lst)
