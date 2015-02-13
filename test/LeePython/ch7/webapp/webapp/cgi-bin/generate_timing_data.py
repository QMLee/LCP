#! /usr/bin/python3
import athletemodel
import yate
import cgi
import cgitb
cgitb.enable()
#import AthleteList



athletes = athletemodel.get_from_store()
form_data=cgi.FieldStorage()
athelete_name=form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header(athelete_name+"\'s Time Data"))
print(yate.u_list(athletes[athelete_name].top3))
print(yate.include_footer({"Home":"/index.html","SelectAnother":"generate_list.py"}))


