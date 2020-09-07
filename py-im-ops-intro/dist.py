def calculateDist(p1,p2):
	dist=0
	c=zip(p1,p2)
	for i in c:
		dist = dist+pow(i[0]-i[1],2)
	dist = pow(dist,0.5)
	return dist

p1 = (3,6,1)
p2 = (2,4,5)