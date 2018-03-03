"""
为了使复杂度降低至线性，用循环来解除递归
"""

def fib(n):
	i=1
	last_one=1
	last_two=1
	while (i<=n):
		if i==1:
			current=1
		elif i==2:
			current=1
		else:
			current=last_one+last_two
			last_two=last_one
			last_one=current
		i+=1
	return current
print(fib(1))#1
print(fib(2))#1
print(fib(3))#2
print(fib(4))#3
print(fib(5))#5
print(fib(6))#8
