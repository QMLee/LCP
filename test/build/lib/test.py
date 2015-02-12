

#for movie in movies:
	#if  isinstance(movie,list) :
	#	for movunit in movie:
	#		print(movunit)
	#else :
	#	print(movie)
#if isinstance(movies,list):
#	print("Yes")
#else:
#	print("No")

def checkList(var):
	if isinstance(var,list):
		for varlist in var:
			checkList(varlist)
	else:
		print(var)
#for movie in movies:
#	checkList(movie)

def printList(listValue):
	for var in listValue:
		if isinstance(var,list):
			printList(var)
		else:
			print(var)

#printList(movies)
