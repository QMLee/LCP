

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

def printList(listValue,level=0):
	#if level < 0:
	#	level = 0
	for var in listValue:
		if isinstance(var,list):
			printList(var,int(level)+1)
		else:
#			print("\t"*int(level),end=" ")
#			print(var)
			print("\t"*int(level)+str(var))

#printList(movies)
