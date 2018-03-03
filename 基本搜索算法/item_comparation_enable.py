"""
最小查找、顺序查找、二分查找，都是通过多次比较来查找。
后面的排序，排序的依据也是基于比较。
关于【比较】
通过重写类的__lt__,__gt__，__eq__方法，在方法中指定比较规则，实现类的实例也可以用=<>来比较

"""

class Count(object):
	def __init__(self,name,salary):
		self._name=name
		self._salary=salary
	def __lt__(self,another):
		return self._salary<another._salary
	def __gt__(self,another):
		return self._salary>another._salary
	def __eq__(self,another):
		return self._salary==another._salary

a=Count('tian',500)
b=Count('wei',1000)
c=Count('tt',500)
print(a<b)#True
print(a>b)#False
print(a==b)#False
print(a==c)#True