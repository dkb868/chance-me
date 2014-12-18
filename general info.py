""" Chance Me : To calculate the chances of admission to a specific university 
based on a derpload of criteria. NOTE WELL THIS IS A RECREATIONAL TOOL.

Will have to account for different colleges within a school -> 
e.g Carnegie Mellon acceptance = 29, SCS acceptance = 7 LOL

75th percentile gpa/sat will give a certain amount of points

result will be : reach, low reach, high reach, implausible, high match, match, low match, high safety, safety, 100% fking safe
what if it can tell you what percentile of all applicants you are in based on the total score from
everything.

can use CC chance me threads for test data LOL

**(New thought: Could include an actual useful (non recreational) section where they could 
just enter test scores and get a list of colleges that they are in the top 75th
percentile of , in order of rankings? Wonder what other possiblities like this their are?
could this site then be combined with the international finacnial aid website idea)

What if different schools ahd different weights. e.g UCLA weights gpa more than sat and 
UCSB weights sat more than gpa. ?
the point values will be part of the school objects and not the general code?
gpa = 3.0
weightedGpa = school().weight(gpa)  #LOL IS THAT EVEN LEGIT but just a rough idea.
state schools wieght gpa more than ivy.
ivy more holisitc than state.
for example ^

The basic idea is that each criteria will have a point system of varying weights, 
e.g 4.0 gpa = 10 points, international volleyball player =  15 points
Points will then be added up and a calculation made based on the particular school.

Will need to make classes like 'ivy league' or for differnt admission
policies such as 'hollistic', 'merit based'.

Below is a list of proposed criteria:
gpa
AP
IB
sats/act

external exams

percentile in class

valedictorian

sports -> level (National? school? state?)

employment

extracurricular -> position -> level
 
'match' : determined by short answer questions or multiple choice,
based on information taken from the colleges website.
e.g "would you describe yourself as 'quirky' or 'respectful' (has to be 2 postives
otherwise bias . yeah probably a shit example) Perhaps this will be the make or break of this entire algorithm

teacher recommendations rating (rated by user, can be scaled down for bias)

guidance counceller recommendations rating

community servcice.

first generation in college

URM

International

Applying for financial aid (is the school need blind or not, adjust depending)

interview required? did you take it? rate it (adjust for bais)

awards obtained -> level

started business? created website? etc?

reason for poor academics? circumstances

development? (rich as fk)

essays * could ask to rate essay, subtract points for bias

give each school different amount of points and use that to determine chances

what if people who got in previous years and could enter their marks and such to adjust
the system. The system would have an 'adjustment factor' that would increase chances if
it realizes it was too strict in the past or decrease chances if it was too liberal in the 
past. 
"""

print "What is your gpa?"
gpa = float(raw_input("> "))

print "What is your SATs?"
sats = int(raw_input(">" ))

if (gpa > 3.0) and (sats > 2000):
	print "You aren't completely hopeless :)" 
	
else:
	print "Give up"
	
exit(0)

class School:
	pass
	self.gpa_weight = 20
	self.gpa_reduction_factor = self.gpa_weight/10
	self.school_gpa_points = [self.gpa_weight, self.gpa_weight - self.gpa_reduction_factor, self.gpa_weight - self.gpa_reduction_factor*2, etc]
	#stronger weight = bigger differnece between rnaks.
	#weker weight = less difference between ranks
	self.gpa_ranking = {4.0 = 0, 3.9 = 1, 3.8 = 1 etc.}
	self.user_gpa_points = self.school_gpa_points[self.gpa_ranking(user_inputed_gpa)]
	# a rough idea of how this might work
	#sum of weights = highest possible points , impossible to actually attain.
	

	
