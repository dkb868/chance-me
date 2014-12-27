""" This contains general info, ideas, and random stream of consciousness thoughts.
some things may not be well expressed, some things may make no sense.
----------------------------------------------------------
27/12/14 new ideas:
so adcoms don't want people with only academics. They want people who are involved
in and our of the calssroom.
Therfore the reader should see how much of the top 10 point contributors are academic
and how much are not. Too much academic r not good. in fact, what if at a certain point
academics was meaningless.
That's how MIT admission works after all. If the user scores are good enuf they are no longer
a part of the admission process.
i.e only the firstreader actually sees your academics and determines it to be good enough.
maybe gpa and sat should just be weighted extremely lower.
or certain gpas give 0 and bad gpas give -ve points
WTF WHAT IF IT USES THE TOP 10 THINGS THAT ARENT ACADEMIC.
Then this would truly be unlike any other admission chances calculator

"No one can give you a meaningful chance extimation:
Because the factors of admissions readily apprehended in a forum post (GPA, SAT. etc.)
are in many ways the least important in our process - MITChris

"But once students have demonstrated academic prepardness, then the additional returns
acrrued by marginal increases in academic performance diminsh markedly" - MITChris

Should gpa points be completely deleted and just have the firstread check
that the person is academically capable?
Should it change depending on the school?
class HighlySelective(school) ?

"AdmissionSplash may be more accurate at some schools than at others, depending on their
selectivity, competitiveness, and how their admission process works. But if you're thinking
of applying to selective schools , please do not pay attention to these sites" - MITChris

Many things to consider moving forward (all quotes taken from a post MITChris made criticizing
a facebook app which does exactly what this program does. Use them for guidance)
-----------------------------------------------------------------------------


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
	
def firstread(user, school): 
	#now the point calculator can use a simple school.gpa_points[user.gpa]
	#ec and other double list will require a loop in pointcalculator
'''this is the point calculator
	 this needs to make a dictionary of points and where they are from
	would be lovely if that dictionary also sorted points and contributors in descending order 
	use the pointscalculator dictionary to find the 10 biggest point contributors.
	because being a member of 100 clubs will never be equal to being leader of internaitonal organization.
	therefore even though each of those 100 clubs may contribute 2 points fora total of 200.
	the int'l organizaiton that gives 150 in itself is worth way more to the adcoms'''
	
	'''STOLEN FROM OTHER FUNCTION def points_calculator(user, school):
	user.gpa_points = school.gpa_points[school.gpa_ranking.index(user.gpa)] 
	
	#find the index i.e ranking of the user gpa.
	#use that rank as the index in gpa_points 
	#i.e 4.0 = a = rank 0 = index 0 = full gpa weight.
	
	#etc 
	
	#add upp all points and bazinga, moar calculations required to find chances.
	#actually still need to create the actual chance % calculator algorithm.'''
	
	
def committeedecision():
	pass
	#if a majority of comittee members say yes gt
	#or if half say yes and one is the director (assume 4 comitte members)
	#if not no gt
	#run a hundred times and find the number of times the person gt
	#use that as acceptance chnace %?
