"""
顺序搜索-
针对无序列表，如果是有序的，可以二分法提高效率

Python有内建的in，这里我们自己实现它
默认返回-1，找到更改
(好几次忘记写i++，陷入死循环……注意了！）



def SequentialSearch(target,lst):
	#for 和while都可以，但我尽量不用for 吧
	position=-1
	i=0
	while i<len(lst):
		if lst[i]==target:
			position=i
		i+=1
	return position

a_target=6
lst1=[1,2,3,4]
lst2=[1,2,6,4]
position1=SequentialSearch(a_target,lst1)
position2=SequentialSearch(a_target,lst2)

print(position1)#-1
print(position2)#2


我这里函数内定义了两个变量，i和position，书上只用了1个

他是如何做到的？
position=0开始，如果遇到就立即返回；搜索到最后还没有，才返回-1.
确实高明很多，而且我写的逻辑不对：都找到了干嘛还继续找啊？


"""



def SequentialSearch(target,lst):
	#for 和while都可以，但我尽量不用for 吧
	position=0
	while position<len(lst):
		if lst[position]==target:
			return position
		position+=1#这么多年第一次体会到+=写法的好处……
	return -1

a_target=6
lst1=[1,2,3,4]
lst2=[1,2,6,4]
position1=SequentialSearch(a_target,lst1)
position2=SequentialSearch(a_target,lst2)

print(position1)#-1
print(position2)#2

"""
这个算法的复杂度就不一定了
for循环中随时可以返回
最好情况，一次返回O（1）
最坏情况，n次返回O（n)
平均：
可能出现的所有情况是：1次找到，2次找到，3次找到……n次找到
所以平均是（1+2+……+n)/n=(1+n)/2=0.5+0.5n，还是n的线性关系，O（n）

"""