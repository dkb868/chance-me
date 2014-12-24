#how much of a match is the person for a particular school?
#an **extremely** dumbed down version of this module
#match points will be included in the main program and add to students' chances
#at the same time this module should well be able to stand as its own program

print "What kind of location do you prefer?"
print "Urban or Rural?"
locationpref = raw_input("> ")

class SchoolProfile:
	def __init__(self,name, location):
		self.name = name
		self.location = location
		
		
harvard = SchoolProfile('harvard', 'Urban')


def locationcalc(schoollocation, pref):
	if schoollocation == pref:
		locationpoints = 10	
		return locationpoints

	else:
		locationpoints = -10
		return locationpoints
		
		
		
def matchcalc(school):
	
	matchpercent = (locationpoints/10) * 100
	print "You are a %d percent match for %s" %(matchpercent, school.name)
	
locationpoints = locationcalc(harvard.location, locationpref)
matchcalc(harvard)

	