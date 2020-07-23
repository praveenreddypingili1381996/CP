# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math
def iskaprekar(n):
	a1=0
	a2=10
	if n==0:
		return False
	a=str(n**2)
	l=len(a)
	for i in range(1,l+1):
		if a2==n:
			continue
		a1=(int(a)//a2)+(int(a)%a2)
		if a1==n:
			return True
		a2= a2*10
	# a=a+a
	# for i in range(l):
	# 	if sum(list(map(int,str(a[i:i+l]))))==n:
	# 		return True
	# if len(a)>1:
	# 	a1=(int(a[:len(a)//2]))+(int(a[len(a)//2:]))
	# 	a2=(int(a[len(a)//2:]))+(int(a[:len(a)//2]))
	# else:
	# 	a1=int(a)
	# if n==a1 or n==a2:
	# 	return True
	return False
	
def fun_nth_kaprekarnumber(n):
	L=[]
	j=0
	while(len(L)<=n):
		if iskaprekar(j):
			L.append(j)
		j+=1
	print (L)
	# return L[n]
