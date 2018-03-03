"""
快速排序：
（1）随机选取一个基准点，并与最后一项交换
（2）通过遍历前面n-1个元素，把小于基准点的元素全部放到最前面，然后列表分割成两半
（3）对子列表继续重复

复杂度分析：
每一轮分割以后，对子列表除基准点以外的所有元素都要进行遍历，所以合起来近似是n（近似是因为这里没有减去基准点）
所以关键在于分割多少轮
最好的情况下，每次都恰好选择不大不小中间的那个数，使得列表长度减半。类似二分，这种情况下经过log2（n）次分割，就会结束。撑起来是n*log2（n）
但最差情况下，假如你选取的基准恰好是最小或最大的那个数，那么就要分（n-1）次。乘起来是n*(n-1)
两者差别很大

"""
def swap(lst,i,j):
	temp=lst[j]
	lst[j]=lst[i]
	lst[i]=temp


def fast_sort(lst):
	left=0
	right=len(lst)-1
	if (left<right):
		divide(lst,left,right)



def divide(lst,left,right):

	pivot_index = (left + right) // 2

	pivot = lst[pivot_index]
	print("基准值是{0},index是{1}".format(pivot,pivot_index))
	swap(lst, pivot_index, right)
	print(lst)


	# 开始把小的排左边，大的排右边
	i = left
	while (True):  # 每一轮开始，找到一个就结束，去下一轮，找不到就没有下一轮
		position = i
		found = False
		while (position < right):  # 没有=是因为right已经是基准值了
			if lst[position] < pivot:  # 如果找到一个，就放开头去，然后从下一个开始扫描
				swap(lst, position, i)
				i += 1
				found = True
				break
			position += 1
		if found == True:  # 如果在内层循环中找到了就continue下一轮，找不到就没有下一轮了
			continue
		else:
			swap(lst,i,right)
			print('这一次分割完成了')
			print(lst)
			print()
			break
	#递归

	if left<i-1:
		divide(lst,left,i-1)
	if i+1<right:
		divide(lst,i+1,right)


a_lst=[2,5,6,9,4,7,1,5,11,0,8]
a_lst=[28,1,75,9,24,4,86,48,55,12,3]
a_lst=[]
fast_sort(a_lst)
print('排序后:',a_lst)


"""
上面的测试列表是我们手写的，现在我们用生成随机数来写
random.randint(1,100)产生一个1-100之间的int(随机）
"""
import random
lst=[]
for count in range(20):
	lst.append(random.randint(1,100))
print('raw lst:',lst)
fast_sort(lst)
print('after fast sort:',lst)

"""
但是我写的这段不够简洁，书上把分割的过程单独装成了一个函数,，看起来更清楚，
然后这一段下面是书上的写法，我一开始理解错了（理解成只要找到1个小于pivot的就和left交换然后从头开找，这样光是查找我就写了两层循环，实际上这里一直遍历下去，循环一次就好了。
我开始的理解也可以实现功能，但是效率拉低了

	while (i < right):  # 没有=是因为right已经是基准值了
		if lst[position] < pivot:  # 如果找到一个，就放开头去，然后从下一个开始扫描
			swap(lst, position, position)
			position += 1
		i+=1
"""
def partition2(lst,left,right):

	pivot_index = (left + right) // 2
	pivot = lst[pivot_index]
	swap(lst, pivot_index, right)

	# 开始把小的排左边，大的排右边
	i=left
	position = left
	while (i < right):  # 没有=是因为right已经是基准值了
		if lst[position] < pivot:  # 如果找到一个，就放开头去，然后从下一个开始扫描
			swap(lst, position, position)
			position += 1
		i+=1

	swap(lst, i, right)
	return position



def divide2(lst,left,right):
	if (left<right):
		dv=partition2(lst,left,right)
		divide(lst,left,dv-1)
		divide(lst,dv+1,right)

def fast_sort2(lst):
	left=0
	right=len(lst)-1
	divide2(lst,left,right)


lst=[]
for count in range(20):
	lst.append(random.randint(1,100))
print('raw lst2:',lst)
fast_sort2(lst)
print('after fast sort2:',lst)