
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
	'''
	print "\nWhat are your top 5 ECs"
	print "State the Activity followed by your Position followed by the Level"
	print "For example: chess club,founder,national"
	count = 0
	ec_list = []
	while count <= 4:
		ec_list[count] = raw_input("What is activity number %d?  >  " %count)
		count ++'''
	
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
	while answer != "no" or "No":
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
	# employmentname = raw_input("> ") useless for point calculations
	print "Full time, part time, summer or no"
	print "Please state the type of employment"
	print "\n\ta) Full Time \n\tb) Part Time \n\tc) Summer \n\td) None \n\te)"
	#this actually needs to be a loop
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
	def __init__(self, gpa_weight, sat_weight, sat2_weight, 
	rec_weight, interview_weight, awards_weight, eclevel_weight,
	ecposition_weight,awardlevel_weight, classrank_weight,need_blind, 
	employment_weight,commservice_weight, otherachlevels_weight): #match_weight
	
	#listed all attributes of school.
	# weights are equal to the points allotted for the achieving the highest rank
	#in that category. i.e gpa_weight = the points for a 4.0 gpa.
	
		self.gpa_weight = gpa_weight
		self.sat_weight = sat_weight
		self.sat2_weight = sat2_weight
		self.rec_weight = rec_weight #recommendations
		self.eclevel_weight = eclevel_weight
		self.ecposition_weight = ecposition_weight #points system needs to multiply eclevel by ecpositoonj
		self.interview_weight = interview_weight
		self.awards_weight = awards_weight
		#self.match_weight = match_weight
	
		#self.externalexams_weight = externalexams_weight  'temporarily' 
		#omitted as external exams requires a shitload of work for different exams
		self.awardlevel_weight = awardlevel_weight
		self.classrank_weight = classrank_weight
		self.need_blind = need_blind #boolean value. need blind or need aware
		self.employment_weight = employment_weight
		self.commservice_weight = commservice_weight 
		self.otherachlevels_weight = otherach_weight #other achievements

	
	''' This was serious laziness i realized:
		also more efficient code was made
		
		class wordranking:
		def __init__(self, wordrank1, wordrank2 ,wordrank3 = 0 ,wordrank4 = 0, wordrank5 = 0,
		wordrank 6 = 0, wordrank 7 = 0):
		
			self.wordrank1 = wordrank1 
			self.wordrank2 = wordrank2
			self.wordrank3 = wordrank3
			self.wordrank4 = wordrank4
			self.wordrank5 = wordrank5
			self.wordrank6 = wordrank6
			self.wordrank7 = wordrank7
		
			ranking = [self.wordrank1, self.wordrank2, self.wordrank3, self.wordrank4,
			self.wordrank5, self.wordrank6, self.wordrank7]
	
		
		
	
	class rangeranking:
		def __init__(self, highest, range1, range2, range3 = 0,
		range4 = 0, range5 = 0, range6 = 0, range7 = 0):
		
			self.highest = highest 
			self.range1 = range1
			self.range2 = range2
			self.range3 = range3
			self.range4 = range4
			self.range5 = range5
			self.range6 = range6
			self.range7 = range7
		
			rangelist = [self.highest, self.range1, self.range2, self.range3,
			self.range4, self.range5, self.range6, self.range7]

			ranking = [self.highest, [range(self.range1, self.highest)],
			[range(self.range2,self.range1)], [range(self.range3, self.range2)],
			[range(self.range4, self.range3)], [range(self.range5, self.range4)],
			[range(self.range6, self.range5)], [range(self.range7, self.range6)]]
		
			#ranking.index(self.highest) etc. to be used later
			
		
			n = 1
			while n < 8:
				for x in range(rangelist[n], rangelist[n-1]): #can maybe multiply gpa by 10 to solve this problem
					ranking[x] = n
				n += 1 '''
		
		
	#making ranking list objects
	
	# copypasta this  [a, b, c, d, e]
	gpa_ranking = [a, b, c, d, e] #using letters for everything now, user well enter a letter corresponding to choice
	#using the dictionary method, most of these no longer required.
	sat_ranking = [a, b, c, d, e]
	sat2_ranking = [a, b, c, d, e]
	rec_ranking = [a, b, c, d, e]
	ec_levels_ranking = [a, b, c, d, e, f]
	ec_positions_ranking = [a, b, c, d, e]
	awardlevels_ranking =[a, b, c, d, e]
	otherach_positions_ranking = [a, b, c, d, e]
	otherach_levels_ranking = [a, b, c, d, e, f]
	#ec_ranking =  ec_ranking contains 2 lists and different calculations
#1 list to get the level of activity eg international and another to get the persons
#position e.g vice president.	too lazy to do atm
	
	interview_ranking = [a, b, c, d, e]
	award_ranking = [a, b, c, d, e]
	#external_ranking  10+ exams = 10+ grading scales lolno
	
	classrank_ranking = [a, b, c, d, e]
	
	employment_ranking = [a, b, c, d, e] # employment needs hours added to it so incomplete and will require similar calcs as EC list
	
	commservice_ranking =  [a, b, c, d, e]
	#all of these can mayve be made into dictionaries 'a': self.gpa_weight
	#or make dictionaries like that and just take user input
	
	gpa_points = {'a':self.gpa_weight, 'b': self.gpa_weight/1.1, 'c': self.gpa_weight/1.3,
	'd':self.gpa_weight/1.5, 'e':self.gpa_weight/2.0} #how the fk to get a good reduction factor
	#unless each individual school gets its own gpa points list after object is created.
	#the difference between first two categories should usually be low
	#bigger difference as we go lower in the categories
	#now the point calculator can use a simple school.gpa_points[user.gpa]
	#ec and other double list will require a loop in pointcalculator
def chances_calculator():
	pass
	

def caseagainst(user, school):
	redflags = 0
	if user.gpa < school.minimumgpa:
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
	
	
def firstread(user, school): '''this is the point calculator
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
	pass
	
		
	
	