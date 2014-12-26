""" This contains general info, ideas, and random stream of consciousness thoughts.
some things may not be well expressed, some things may make no sense.

so apparently harvard choses the top (~10) people from each region then takes them to committee.
0% chances for most of the caribbean. fun. If this calc gives all of us 0 we're doing it right

25/12/2014 : Will try to make a post on CC and anywhere else to gather people to participate in a
survey to test the effectiveness of the app, just out of curiosity.
Should make clear to them that this makes no money and isn't advertising for my benefit, just an experiment.
no spamerinos 
I just realized i don't have to even do that, can just use old '2017 decision results' threads
enter the users infos and see

Chance Me : To calculate the chances of admission to a specific university
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

"""
Something i did for lulz.

print "What is your gpa?"
gpa = float(raw_input("> "))

print "What is your SATs?"
sats = int(raw_input(">" ))

if (gpa > 3.0) and (sats > 2000):
	print "You aren't completely hopeless :)"

else:
	print "Give up"

exit(0)"""

# old idea
'''class School:
	self.gpa_weight = 20
	self.gpa_reduction_factor = self.gpa_weight/10
	self.school_gpa_points = [self.gpa_weight, self.gpa_weight - self.gpa_reduction_factor, self.gpa_weight - self.gpa_reduction_factor*2, etc]
	#stronger weight = bigger differnece between rnaks.
	#weker weight = less difference between ranks
	self.gpa_ranking = {4.0 = 0, 3.9 = 1, 3.8 = 1 etc.}
	self.user_gpa_points = self.school_gpa_points[self.gpa_ranking(user_inputed_gpa)]
	# a rough idea of how this might work
	#sum of weights = highest possible points , impossible to actually attain.'''
	
	
	
	
#New Concepts

def casefor():
	pass
	#make a case for the candidate
	#look at all the reasons to accept them
	#return some value
	
def caseagainst():
	pass
	#make a case against the candidate
	#look at all reasons not to accept them
	#return some value
	

if casefor >> caseagainst: #>> = far greater, in reality the code would look like if casefor > caseagainst + x 
#so x will determine exactly what fargreater is

	#there will be a probability of instant acceptance
	
elif caseagainst >> casefor:
	#probability of instant rejection
	
else:
	pass
	#carry on to the committee.
	
class comitteemember:
	pass
	

class staff(committeemember):
	pass
	#staff members have slightly less weight inthe decision

class director(comitteemember):
	pass
	#director of admissions has slightly more weight in the decision.


def probabilityrange():
	pass
	#make a calculation based on casefor and caseagainst to determine a range of probabilties
	#of a committee member saying yes.
	
	
def committeedecision():
	pass
	#if a majority of comittee members say yes gt
	#or if half say yes and one is the director (assume 4 comitte members)
	#if not no gt
	#run a hundred times and find the number of times the person gt
	#use that as acceptance chnace %?
