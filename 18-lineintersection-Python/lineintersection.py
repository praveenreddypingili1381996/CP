# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	# if m1 == m2 or abs(m2-m1) == abs(b1-b2):
	# 	return None
	for x in range(max(m1,m2,b1,b2)):
		if (m1*x + b1) == (m2*x + b2):
			return x
	return None
	pass
