
import os

def santif(var):
	spliter = ''
	if '-' in var:
		spliter = '-'
	elif ':' in var:
		spliter = ':'
	else :
		return var
	(mi,sec)=var.split(spliter)
	return mi+'.'+sec

def readFile(file_name):
	try:
		with open(file_name) as data:
			return data.readline().strip().split(',')
	except ValueError as value_error:
		print "Value Error:"+str(value_error)
#return value is needed
		return None
		
jameslist=[]
julielist=[]
mikeylist=[]
sarahlist=[]

os.chdir('LeePython/ch5')
try:
#	with open('james.txt') as james_data:
#		print(sorted(set([santif(t) for t in james_data.readline().strip().split(',')]))[0:3])

#	with open('julie.txt') as  julie_data:
#		for julie_value in julie_data.readline().strip().split(','):
#			julielist.append(santif(julie_value))
#	with open('mikey.txt') as mikey_data:
#		for mikey_value in mikey_data.readline().strip().split(','):
#			mikeylist.append(santif(mikey_value))
#	with open('sarah.txt') as sarah_data:
#		for sarah_value in sarah_data.readline().strip().split(','):
#			sarahlist.append(santif(sarah_value))
#	print(sorted(set(julielist))[0:3])
#	print(sorted(set(mikeylist))[0:3])
#	print(sorted(set(sarahlist))[0:3])


	jameslist = readFile("james.txt")
	julielist = readFile("julie.txt")
	mikeylist = readFile("mikey.txt")
	sarahlist = readFile("sarah.txt")
	print(sorted(set([santif(t) for t in jameslist]))[0:3])
	print(sorted(set([santif(t) for t in julielist]))[0:3])
	print(sorted(set([santif(t) for t in mikeylist]))[0:3])
	print(sorted(set([santif(t) for t in sarahlist]))[0:3])
except ValueError as valueError:
	print 'Error:'+str(valueError)
