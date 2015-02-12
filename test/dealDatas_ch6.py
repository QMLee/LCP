import os
import test



class Athlete:
	def __init__(self, a_name=None, a_birthday=None, a_times=[]):
		self.name = a_name
		self.birthday = a_birthday
		self.times=a_times
	def get_coach_data(self,file_value):
		list_value=readFile(file_value)
		self.name=list_value.pop(0)
		self.birthday=list_value.pop(0)
		self.times=sorted(set([santif(t) for t in list_value]))[0:3]
		return self


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
		return None
#return value is needed
	
def formatData(list_value):
	name = list_value.pop(0)
	birthday = list_value.pop(0)
	data_value=sorted(set([santif(t) for t in list_value]))[0:3]	
	print name
	print birthday
	print data_value
	print 
	
		
jameslist=[]
julielist=[]
mikeylist=[]
sarahlist=[]

os.chdir('LeePython/ch6')
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


#	jameslist = readFile("ja.txt")
#	julielist = readFile("ju.txt")
#	mikeylist = readFile("mi.txt")
#	sarahlist = readFile("sa.txt")
	
#	formatData(jameslist)
#	formatData(julielist)
#	formatData(mikeylist)
#	formatData(sarahlist)

#	jalist=[jameslist[0],jameslist[1],sorted(set([santif(t) for t in jameslist[2:]]))[0:3]]
#	print test.printList(jalist,0)
#print None     ,have no idear why... find it out~

#	julist=[julielist[0],julielist[1],sorted(set([santif(t) for t in julielist[2:]]))[0:3]]
#	print test.printList(julist,0)
	
#	milist=[mikeylist[0],mikeylist[1],sorted(set([santif(t) for t in mikeylist[2:]]))[0:3]]
#	print test.printList(milist,0)
	
#	salist=[sarahlist[0],sarahlist[1],sorted(set([santif(t) for t in sarahlist[2:]]))[0:3]]
#	print test.printList(salist,0)	
	a =Athlete()
	a.get_coach_data("ja.txt")
	print a.name
	print a.birthday
	print a.times
	print 
	

except ValueError as valueError:
	print 'Error:'+str(valueError)
