"""
返回最小项的index。
思路：
默认第一个最小，再一次比较

Python有内置函数min，这里我们自己实现它

"""
def IndexOfMin(lst):
	min=0
	#用for和while都行
	# for i in range(1,len(lst)):
	# 	if (lst[i]<lst[min]):
	# 		min=i
	current_index=1
	while current_index<len(lst):
		if(lst[current_index]<lst[min]):
			min=current_index
		current_index+=1
	return min
a_lst=[6,5,4,3,1,5]
min=IndexOfMin(a_lst)
print(min)

"""
用到了两个变量：min和current_index
这个算法的复杂度是O(n)，列表大小为n，比较n-1次。n-1是确定的，必须从头到尾
"""