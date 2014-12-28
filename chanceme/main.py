
'''import match  <- somebody's job (created a small example)
23/12/2014: fixed extracurriculars and awards 
			also created match module
25/12/2014: fixed most input, changed to multiple choice letters
			also fixed  ranking, rangeranking and wordranking deleted
			made redflags function
			also merry christmas #nolife
			
			
25/12/2014: Done: most rankings, main input system. 
			To do list:
			point lists
			match module
			firstread
			commitee
			general cleaning up
			
27/12/2014: To do:
			Begin testing.
			committee function
			'''
		



class User:
	def __init__(self, name, gpa, sat, sat2, rec
	, interview, awardlist,awardlevels, eclist, eclevels, #ec and awards re-added
	otherachlist, otherachlevels, otherachpositions, ecpositions, classrank, finaid, 			
	international, URM, legacy, ed, firstgen,#externalexams left out
	employment, commservice, otherach, ): 
		
		self.name = name
		self.gpa = gpa
		self.sat = sat
		self.sat2 = sat2
		self.rec = rec
		self.interview = interview
		self.award_list = awardlist
		self.award_levels = awardlevels
		self.ec_list = eclist
		self.ec_levels = eclevels
		self.ec_positions = ecpositions
		self.classrank = classrank
		self.finaid = finaid
		self.international = international
		self.URM = URM
		self.legacy = legacy
		self.ed = ed
		self.firstgen = firstgen
		self.employment = employment
		self.commservice = commservice
		self.otherac = otherach
		
	
def main():
	#copypasta this:   print "\n\ta) \n\tb) \n\tc) \n\td) \n\te)"
	print "Welcome to Chance Me Maybe"
	print "You will receive a troll calculation of your acceptance chances"
	print "What is your name?"
	name = raw_input("> ")
	
	print "Hello %s!" %name
	print "Please answer the questions as accurately as possible."
	print "Where the question is multiple choice,"
	print "Please type the letter corresponding to your choice."
	print "May the force be with you."
	
	print "\nWhat is your gpa?"
	print "\n\ta) 4.0\n\tb) 3.7 - 3.9\n\tc) 3.4 - 3.6\n\td) 3.0 - 3.3\n\te) < 3.0"
	gpa = raw_input("> ")
	
	print "\nWhat is your SAT1 score?"
	print "\n\ta) 2300 - 2400\n\tb) 2200 - 2300\n\tc) 2100 - 2200\n\t(d) 1800- 2000\n\t < 1800"
	sat = raw_input("> ")
	
	print "\nWhat is your SAT Subject Test score?"
	print "\n\ta) 780 - 800 \n\tb) 750 - 780 \n\tc) 720 - 760 \n\td) 700- 720 \n\te) <700 "
	sat2 = raw_input("> ")
	
	print "\nHow was your letter of recommendations?"
	print "Excellent, Very Good, Good or Average?"
	print "\n\ta) Excellent \n\tb) Very Good \n\tc) Good \n\td) Average \n\te) Below Average"
	rec = raw_input("> ")
	
	
	print "\n Time to input your top 5 Extra-Curriculars"
	print "You will be asked for the activity, then the level then your position."
	count = 0
	ec_list = []
	ec_levels = []
	ec_positions = []
	
	while count <= 4:
		print "What is your number %d extracurricular activity?" %(count + 1)
		ec_list[count] = raw_input("> ") #this has no purpose but why not
		
		print "\n At what level was this EC done?"
		print "\n\ta) International \n\tb) National \n\tc) Regional \n\td) State \n\te) City \n\tf) School"
		ec_levels[count] = raw_input("> ")
		
		print "\nWhat was your highest position throughout school?"
		print "\n\ta) Founder \n\tb) President \n\tc)Vice President \n\td)Officer \n\te) Member"
		ec_positions[count] = raw_input("> ")
		
		#need to add category for amount of years spent in EC 
		count += 1 #apparently ++ doesn't exist in python lol :(
		
		print "Do you have another extracurricular to report? Answer yes or no"
		answer = raw_input("> ")
		
		if answer == "no" or "No":
			break
		
		#loop takes up to 5 extra curriculars as most schools 
		#only care about the 5 most important
		#user may break early if they wish
	 
	
	print "How was your interview?"
	print "\n\ta) Excellent \n\tb) Very Good \n\tc) Good \n\td) Average \n\te) Below Average"
	interview = raw_input("> ")
	
	print "Have you won any awards?"
	answer = raw_input("> ")
	award_list = []
	award_levels = []
	count = 0
	while answer != ("no" or "No"):
		print "What is the name of your award?"
		award_list[count] = raw_input("> ")
		#award_list recorded without a real purpose
		
		print "What level was this award received at?"
		print "\n\ta) International \n\tb) National \n\tc) Regional \n\td) State \n\te) City \n\tf) School"
		award_levels[count] = raw_input("> ")
		#list of levels will be used for point calculation

		print "Nice, do you have any more awards to report?"
		
		answer = raw_input("> ")
		
		count += 1
		
	

	#print "What external exam have you done, if any?"
	#externalname = raw_input("> ")
	#print "What were your marks on %s" %external
	#externalmarks = input("> ") #needs multiple values ... zzzz
	
	print "\nWhat was your class rank?"
	print "Top 5%, Top 10%, Top 30%, Top 50% or Top 100% or School Does Not Rank"
	print "\n\ta) Top 5% \n\tb) Top 10%  \n\tc) Top 30% \n\td) Top 50% \n\te) School Does Not Rank" 
	#e is special case that needs to be dealt with
	classrank = raw_input("> ")
	if classrank == "e":
		classrank = None
	
	print "\nWill you be applying for financial aid?"
	print "Yes or No"
	aid = raw_input("> ")
	
	print "\nAre you considered an international student?"
	print "Yes or No"
	international = raw_input("> ")
	
	print "\nAre you considered an Underrepresented Minority?"
	URM = raw_input("> ")
	
	print "\nDo you have legacy status at the school you are applying to?"
	legacy = raw_input("> ")
	
	print "\nAre you applying early decision?"
	ed = raw_input("> ")
	
	print "\nAre you the first generation of your family to attend college?"
	firstgen = raw_input("> ")
	
	print "\nPlease list all your previous employment"
	print "Please state the type of employment"
	print "\n\ta) Full Time \n\tb) Part Time \n\tc) Summer \n\td) None \n\te)"
	#this actually needs to be a loop and needs to include work hours i.e doube list like EC
	employment = raw_input("> ")
	
	print "\nHow much community service hours do you have?"
	print "\n\ta) 1000 \n\tb) 100 \n\tc) 50 \n\td) 10 \n\te) 0" #dem numbers
	commservice = raw_input("> ")
	
	print "\nDo you have any other accomplishments?"
	print "Such as creating an international billion dollar corporation?"
	answer = raw_input("> ") #how much times does 'answer' get assigned to something? :) 
	otherach_list = []
	otherach_levels = []
	otherach_positions = []
	count = 0
	while answer != "no" or "No":
		print "Describe your accomplishment"
		otherach_list[count] = raw_input("> ")
		#otheracc_list recorded without a real purpose
		
		print "At what level was this accomplishment achieved?"
		print "\n\ta) International \n\tb) National \n\tc) Regional \n\td) State \n\te) City \n\tf) School"
		otherach_levels[count] = raw_input("> ")
		#list of levels will be used for point calculation
		print "What was your position in this group/competition/etc?"
		print "\n\ta) Founder \n\tb) Leader \n\tc) Vice President \n\td) Officer \n\te) Member"
		otherach_positions[count] = raw_input("> ")

		print "Nice, do you have any more awards to report?"
		
		answer = raw_input("> ")
		
		count += 1

	#match quiz somewhere
	
	user1 = User(name, gpa, sat, sat2, rec, interview, award, 
	classrank, aid , international, URM, legacy, ed, firstgen
	, employment, commservice, otheracc) #this needs to be adjusted for new vars + name changes
	

class School:
	def __init__(self,name, gpa_weight, sat_weight, sat2_weight, 
	rec_weight, interview_weight, eclevels_weight,
	ecpositions_weight,awardlevels_weight, classrank_weight,need_blind, 
	employment_weight,commservice_weight, otherach_levels_weight,
	otherach_positions_weight): #match_weight
	
	# weights are equal to the points allotted for the achieving the highest rank
	#in that category. i.e gpa_weight = the points for a 4.0 gpa.
	
		self.name = name
		self.gpa_weight = gpa_weight
		self.sat_weight = sat_weight
		self.sat2_weight = sat2_weight
		self.rec_weight = rec_weight 
		self.ec_levels_weight = eclevels_weight
		self.ec_positions_weight = ecpositions_weight 
		self.interview_weight = interview_weight
		self.awardlevels_weight = awardlevels_weight
		#self.match_weight = match_weight
	
		#self.externalexams_weight = externalexams_weight  'temporarily' 
		#omitted as external exams requires a shitload of work for different exams

		self.classrank_weight = classrank_weight
		self.need_blind = need_blind #boolean value. need blind or need aware
		self.employment_weight = employment_weight
		self.commservice_weight = commservice_weight 
		self.otherach_levels_weight = otherach_levels_weight #other achievements
		self.otherach_positions_weight = otherach_positions_weight

	

		
	#attack of the dictionaries incoming
	
		gpa_points = {'a':self.gpa_weight, 'b': self.gpa_weight/1.1, 'c': self.gpa_weight/1.3,
		'd':self.gpa_weight/1.5, 'e':self.gpa_weight/2.0} #reduction factor may need improvements later

		sat_points = {'a':self.sat_weight, 'b':self.sat_weight/1.1, 'c': self.gpa_weight/1.3,
		'd':self.sat_weight/1.5, 'e':self.sat_weight/2.0}
	
		sat2_points = {'a':self.sat2_weight, 'b':self.sat2_weight/1.1, 'c':self.sat2_weight/1.3, 
		'd':self.sat2_weight/1.5, 'e':self.sat2_weight/2.0}
	
		rec_points = {'a':self.rec_weight, 'b':self.rec_weight/1.1, 'c':self.rec_weight/1.3, 
		'd':self.rec_weight/1.5, 'e':self.rec_weight/2.0}
	
		ec_levels_points = {'a':self.ec_levels_weight, 'b':self.ec_levels_weight/1.1, 'c':self.ec_levels_weight/1.3, 
		'd':self.ec_levels_weight/1.5, 'e':self.ec_levels_weight/2.0,'f':self.ec_levels_weight/3.0}
	
		ec_positions_points = {'a':self.ec_positions_weight, 'b':self.ec_positions_weight/1.1, 'c':self.ec_positions_weight/1.3, 
		'd':self.ec_positions_weight/1.5, 'e':self.ec_positions_weight/2.0}
	
		awardlevels_points ={'a':self.awardlevels_weight, 'b':self.awardlevels_weight/1.1, 'c':self.awardlevels_weight/1.3, 
		'd':self.awardlevels_weight/1.5, 'e':self.awardlevels_weight/2.0}
	
		otherach_positions_points = {'a':self.otherach_positions_weight, 'b':self.otherach_positions_weight/1.1, 'c':self.otherach_positions_weight/1.3, 
		'd':self.otherach_positions_weight/1.5, 'e':self.otherach_positions_weight/2.0}
		
		otherach_levels_points = {'a':self.otherach_levels_weight, 'b':self.otherach_levels_weight/1.1, 'c':self.otherach_levels_weight/1.3, 
		'd':self.otherach_levels_weight/1.5, 'e':self.otherach_levels_weight/2.0,'f':self.otherach_levels_weight/3.0}
	
		interview_points = {'a':self.interview_weight, 'b':self.interview_weight/1.1, 'c':self.interview_weight/1.3, 
		'd':self.interview_weight/1.5, 'e':self.interview_weight/2.0}


		classrank_points = {'a':self.classrank_weight, 'b':self.classrank_weight/1.1, 'c':self.classrank_weight/1.3, 
		'd':self.classrank_weight/1.5, 'e':self.classrank_weight/2.0}

		employment_points = {'a':self.employment_weight, 'b':self.employment_weight/1.1, 'c':self.employment_weight/1.3, 
		'd':self.employment_weight/1.5, 'e':self.employment_weight/2.0}
	# employment needs hours added to it so incomplete and will require similar calcs as EC list

		commservice_points =  {'a':self.commservice_weight, 'b':self.commservice_weight/1.1, 'c':self.commservice_weight/1.3, 
		'd':self.commservice_weight/1.5, 'e':self.commservice_weight/2.0}
	

	

def caseagainst(user, school):
	redflags = 0
	if user.gpa < school.minimumgpa: #school.minimumgpa doesn't exist yet :O
		redflags += 1
	
	if user.sat < school.minimumsat:
		redflags += 1
		
	if user.sat2 < school.minimumsat2:
		redflags += 1
		
	if user.classrank < school.minimumclassrank:
		redflags += 1
		
	#etc
	#essentially, find out the amount of potential red flags the candidate has
	#red flags severely affect chances of the committee accepting you
	#in absolute the worst cases, too much redflags can give a chance of instant rejection before committee
	#i.e application sent to dean of admissions for him to decide whether to reject or let candidate go to committee
	
	
def firstread(user, school):
	
	user.gpa_points = school.gpa_points[user.gpa]
	user.sat_points = school.sat_points[user.sat]
	uer.sat2_points = school.sat2_points[user.sat2]
	
	user.rec_points = school.rec_points[user.rec]
	
	#each ec gets a different attribute, for the top 10 thing to make sense
	user.ec1_points = (school.ec_levels_points[user.ec_levels[0]] *
	school.ec_positions_points[user.ec_positions[0]])
	
	user.ec2_points = (school.ec_levels_points[user.ec_levels[1]] *
	school.ec_positions_points[user.ec_positions[1]])
	
	user.ec3_points = (school.ec_levels_points[user.ec_levels[2]] *
	school.ec_positions_points[user.ec_positions[2]])
	
	user.ec4_points = (school.ec_levels_points[user.ec_levels[3]] *
	school.ec_positions_points[user.ec_positions[3]])
	
	user.ec5_points = (school.ec_levels_points[user.ec_levels[4]] *
	school.ec_positions_points[user.ec_positions[4]])
	
	#user can now only submit 5 awards
	user.award1_points = school.awardlevels_points[user.awardlevels[0]]
	user.award2_points = school.awardlevels_points[user.awardlevels[1]]
	user.award3_points = school.awardlevels_points[user.awardlevels[2]]
	user.award4_points = school.awardlevels_points[user.awardlevels[3]]
	user.award5_points = school.awardlevels_points[user.awardlevels[4]]
		
	user.otherach1_points = (school.otherach_positions_points[user.otherach_positions[0]] *
	school.ec_positions_points[user.ec_positions[0]])
	
	user.otherach2_points = (school.otherach_positions_points[user.otherach_positions[1]] *
	school.otherach_levels_points[user.otherach_levels[1]])
	
	user.otherach3_points = (school.otherach_positions_points[user.otherach_positions[2]] *
	school.otherach_levels_points[user.otherach_levels[2]])
	
	user.otherach4_points = (school.otherach_positions_points[user.otherach_positions[3]] *
	school.otherach_levels_points[user.otherach_levels[3]])
	
	user.otherach5_points = (school.otherach_positions_points[user.otherach_positions[4]] *
	school.otherach_levels_points[user.otherach_levels[4]])
	
	
	user.interview_points =  school.interview_points[user.interview]

	user.classrank_points = school.classrank_points[user.classrank]

	user.employment_points = school.employment_points[user.employment]

	user.commservice_points =  school.commservice_points[user.commservice]
	
	user.pointlist = [user.gpa_points, user.sat_points, uer.sat2_points,
	user.rec_points, user.ec1_points, user.ec2_points,
	user.ec3_points, user.ec4_points,
	user.ec5_points, user.award1_points,
	user.award2_points, user.award3_points, 
	user.award4_points, user.award5_points, 
	user.otherach1_points, user.otherach2_points, 
	user.otherach3_points, user.otherach4_points, 
	user.otherach5_points, user.interview_points,  
	user.classrank_points, user.employment_points, 
	user.commservice_points 
	]
	
	
	user.descending_pointlist = sorted(pointlist, reverse=True)
	
	user.toptenlist = descending_pointlist[:10]
	
	
def committee(user, school):
	if school.name == 'Harvard':
		print "You are rejected"
	
	else:
		print "You are still rejected"