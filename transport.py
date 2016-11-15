# costwalk=1
# costtram=2

def min_cost(n):
	if n==1:
		return 1
	if(n%2==1):
		cost=min_cost(n-1)+1
	else:
		cost=min(min_cost(n/2)+2, min_cost(n-1)+1)
	return cost
print min_cost(41)