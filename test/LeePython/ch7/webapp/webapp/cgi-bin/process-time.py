#! /usr/bin/python3

import os
import cgi
import yate
import sys

print(yate.start_response('text/plain'))
form = cgi.FieldStorage()
print (form["time_value"].value,file=sys.stderr)
#print timeing_value
print (file=sys.stderr)
print('OK')
