import os

mycwdss = os.getcwd()
print mycwdss
os.chdir("LeePython/ch3/")
mycwd = os.getcwd()
print mycwd
data = open('sketch.txt')
for eachline in data:
	try:
#		(role, spoken)=eachline.split(":",1)
		(role, spoken)=eachline.split(":")
		print role,   
		print  'said: '
		print spoken
	except:
		pass
data.close()
