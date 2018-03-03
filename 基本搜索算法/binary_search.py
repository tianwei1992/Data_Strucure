"""
对有序列表，用二叉搜索可以提高效率
"""


def binarySearch(target,sorted_lst):
	#mid=int(len(sorted_lst)/2)这里不要用长度来算mid，因为要保留index
	#这里不用递归
	left=0
	right=len(sorted_lst)-1#开两个指针，分别指向第一个元素和最后一个元素

	while left<=right:#有等号，等于的时候还需要比较，有交叉跨越才结束
		mid = (left + right) //2#//表示整除
		if target==sorted_lst[mid]:
			return mid
		if target>sorted_lst[mid]:
			left=mid+1
		elif target<sorted_lst[mid]:
			right=mid-1
	return -1

sorted_lst1=[1,2,3,4,5,6,7,8]
sorted_lst2=[]

position1=binarySearch(7,sorted_lst1)#6
position2=binarySearch(0,sorted_lst1)#-1
position3=binarySearch(0,sorted_lst2)#-1

print(position1)
print(position2)
print(position3)


"""
复杂度：log2（n）
最好：1轮
最差：第一轮n/2,第二轮再/2，第三轮再/2……一直到结果为1.（严格说结果为1以后，还有一轮比较：在得到结果为1这一轮代表着还剩下2个或3个元素，本轮比较可以排除1个元素，那么剩下1或2个元素是不是target还需要下一轮
n除以2的k次方=1，那么n=2的k次方，k=log2（n），实际的次数是log2(n)+1，不过在复杂度这里+1就省略了吧。当n趋近于无穷大的时候，常数算不了什么的
"""