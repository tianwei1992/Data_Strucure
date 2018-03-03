"""

数组与连续内存：实现随机访问
数组的大小在产生时就固定了，程序员不能随意改变长度，不能加一项或者删一项
"""

class Array:
	def __init__(self, capacity, fillVaule=None) :
		self._items=list()

		self._defaultCapacity=capacity
		#初始化时分情况，由于None不是有效值，因此如果用None填充逻辑大小为0；如果不用None填充，逻辑大小为数组实际长度
		if fillVaule!=None:
			for i in range(capacity):
				self._items.append(fillVaule)
			self._logicalSize = len(self._items)
		else:
			for i in range(capacity):
				self._items.append(None)
			self._logicalSize=0
	def __len__(self):
		return len(self._items)
	def __str__(self):#当print(a)时，对a._items进行str()
		return str(self._items[:self._logicalSize])
	def __iter__(self):#对a用for in时调用
		return iter(self._items)
	def __getitem__(self, index):#a[index]调用
		return self._items[index]
	def __setitem__(self, index, value):#a[index]='a'时调用
		i=0
		#赋值合法性检查
		while(i<index):
			if self._items[i]==None:
				print('不连续赋值')
				return -1
			i+=1
		#如果是新增元素，逻辑大小+1；如果是替换，不变
		if index==self._logicalSize:
			self._logicalSize+=1
		self._items[index]=value
		#照理说这里还需要改变逻辑大小，但是……这里无法yo懂代码做到
	def expand(self):

		if self._logicalSize==self._defaultCapacity:
			temp=Array(len(self)*2)
			for i in range(len(self)):
				temp[i]=self._items[i]
			temp._logicalSize=len(temp)
			return temp
		return -1
	def reduce(self):
		#物理大小，逻辑大小，初始容量
		#由于expand时是新建了数组，初始容量也在变化，条件2好像无法满足，去掉吧
		#if self._logicalSize <= len(self) // 4 and len(self) >= self._defaultCapacity * 2:
		if self._logicalSize<=len(self)//4 :
			temp=Array(self._defaultCapacity//2)


			for i in range(self._defaultCapacity//2):
				temp[i]=self._items[i]
			#temp._logicalSize = len(temp)
			return temp
		return -1


	def insert(self,value,index):
		#1检查长度是否够用
		if self._logicalSize+1<=self._defaultCapacity:

			#2把后面的挪走，挖洞
			i=self._logicalSize
			while(i>index):
				self._items[i]=self._items[i-1]
				i-=1
			#3填坑

			self._items[index]=value
			self._logicalSize+=1
		return -1
	def delete(self, index):
		i=index
		while (i<self._logicalSize-1):
			self._items[i]=self._items[i+1]
			i+=1
		self._items[self._logicalSize-1]=None
		self._logicalSize-=1


"""
通过__开头的方法实现的操作：
"""

if __name__=="__main__":
	print('__开头的方法实现的操作：')
	a=Array(4,'a')
	a[1]=1
	print(len(a))#4
	print(a)#['a', 'a', 'a', 'a']
	print(a[3])#a
	""""
	以下是自己实现的操作
	"""
	DefautCapacity=5
	a=Array(DefautCapacity,fillVaule=1)
	#增加数组大小
	print('增加数组大小:',a)
	new_array=a.expand()#表面效果看似是在原数组后面加了一项，但由于数组大小不可改变，实际上是重新建了一个数组，然后把a引用的数组换掉
	print(new_array)#[1, 1, 1, 1, 1, None, None, None, None, None]

	#减小一项
	print(' 减少一项:')
	a.delete(3)
	print(a)
	#插入一项
	print(' 插入一项:')
	a.insert('insert',2)
	print(a)



	print('减小数组大小:')
	#先减少数组中的元素，使其满足减大小条件
	a=Array(5,)
	a.insert(1,0)
	print('原始的数组:',a._items)#[1, None, None, None, None]
	new_array=a.reduce()#表面效果看似是在原数组后面加了一项，但由于数组大小不可改变，实际上是重新建了一个数组，然后把a引用的数组换掉
	print(new_array._items)#[1, None]#直接打印new_array看不出效果，._items才是内存里的形式
	print(len(new_array))

""""
注意：
1、logicalSize这个变量在初始时为0，然后每次操作实际长度有变化时记得也要修改它的值。这个值的大小会影响到数组的物理大小len(a)，要不要调整
2、从数组中删除一项或插入一项。都涉及改logicalSize。插入一项前要检查物理大小是否够用，删除后要检查是否需要减小数组大小。照理说是这样的，但是本例没有在操作前后去调用检查。
3、物理大小可以扩充或减小，减小时需要满足一定条件：条件1and 条件2。
涉及到：逻辑长度、物理长度、创建时的长度
4、数组大小的增加或者减小，是创建了新数组，然后进行了数据复制。元素的插入和删除是原数组，移位于赋值的操作。
5、一点思考……越来越复杂了
后面关于逻辑大小，也就是实际有意义的元素。那么[1,None]这种，逻辑大小算0还是1呢？如果算1，[1,None,2]这种又算几呢？必须算3把。不过这种情况在数组这个概念里应该不允许出现。那么这样每次a[2]=5的赋值操作里，首先要进行输入检查，确定0-1都不为空才可以继续，然后还需要确定是新增还是改变。这将决定逻辑大小是+1还是保持原样.

6、关于a=Array（），a和a._items，形式上都是序列，但a是类的实例，有很多的附加属性；而a._items是其中一个属性，表示数组在内存里的情况，print(a)和print（a._items）不一样，前者只显示到有意义的数据，对于分配了内存但是为赋值的None则不显示,在这里len(a)不是逻辑大小，而是物理大小，因为值为None的元素也上算了
"""