# a rather rough draft
#highest points = weighted value

#import match  <- somebody's job

class User:
	def __init__(self, name, gpa, sat, sat2, rec
	, interview,awards, classrank, finaid,
	international, URM, legacy, ed, firstgen,#externalexams left out
	employment, commservice, otherach): #user_ec temp removed
		pass
	
		#pls
	
def main():
	print "Welcome to Chance Me Maybe"
	print "You will receive a troll calculation of your acceptance chances"
	print "What is your name?"
	name = raw_input("> ")
	print "\nWhat is your gpa?"
	gpa = int(float(raw_input("> ")) * 10)
	print "\nWhat is your SAT1 score?"
	sat = input("> ")
	print "\nWhat is your SAT Subject Test score?"
	sat2 = input("> ")
	print "\nHow was your letter of recommendations?"
	print "Excellent, Very Good, Good or Average?"
	rec = raw_input("> ")
	print "\nWhat are your ECs"
	#2 hard 4 me
	# double list required. 
	#Region  e.g international
	#position e.g president
	#clearly some thing needs to change with regards all the EC variables
	
	print "How was your interview?"
	print "Excellent, Very Good, Good or Average?"
	interview = raw_input("> ")
	print "\nWhat kind of awards have you won and at what level?"
	print "International, National, Regional, State, City, School"
	award = raw_input("> ")
	#wait that needs to take more than one things.
	#also need a sentence parser or something to search for the keywords.
	#rest of their sentence is irrelevant
	
	#print "What external exam have you done, if any?"
	#externalname = raw_input("> ")
	#print "What were your marks on %s" %external
	#externalmarks = input("> ") #needs multiple values ... zzzz
	
	print "\nWhat was your class rank?"
	print "Top 5%, Top 10%, Top 30%, Top 50% or Top 100% or School Does Not Rank"
	classrank = raw_input("> ")
	
	print "\nWill you be applying for financial aid?"
	print "Yes or no"
	aid = raw_input("> ")
	
	print "\nAre you considered an international student?"
	print "Yes or no"
	international = raw_input("> ")
	
	print "\nAre you considered an Underrepresented Minority?"
	URM = raw_input("> ")
	
	print "\nDo you have legacy status at the school you are applying to?"
	legacy = raw_input("> ")
	
	print "\nAre you applying early decision?"
	ed = raw_input("> ")
	
	print "\nAre you the first generation of your family to attend college?"
	firstgen = raw_input("> ")
	
	print "\nAre you or have you been employed?"
	print "Full time, part time, summer or no"
	employment = raw_input("> ")
	
	print "\nHow much community service hours do you have?"
	commservice = input("> ")
	
	print "\nDo you have any other accomplishments?"
	print "Such as creating an international billion dollar corporation?"
	print "At what level was this accomplishment?"
	print "And what is your position in the group if applicable?"
	otheracc = raw_input("> ") #also double list problem , see above.
	
	#match quiz somewhere
	
	user1 = User(name, gpa, sat, sat2, rec, interview, award, 
	classrank, aid , international, URM, legacy, ed, firstgen
	, employment, commservice, otheracc)
	

class School:
	def __init__(self, gpa_weight, sat_weight, sat2_weight, 
	rec_weight, interview_weight, awards_weight,  #ec_weight temp removed
	classrank_weight,need_blind, employment_weight, 
	commservice_weight, otherach_weight): #match_weight
	
	#listed all attributes of school.
	# weights are equal to the points allotted for the achieving the highest rank
	#in that category. i.e gpa_weight = the points for a 4.0 gpa.
	
		self.gpa_weight = gpa_weight
		self.sat_weight = sat_weight
		self.sat2_weight = sat2_weight
		self.rec_weight = rec_weight #recommendations
	#	self.ec_weight = ec_weight #extracurriculars
		self.interview_weight = interview_weight
		self.awards_weight = awards_weight
		#self.match_weight = match_weight
	
		#self.externalexams_weight = externalexams_weight  'temporarily' 
		#omitted as external exams requires a shitload of work for different exams
		
		self.classrank_weight = classrank_weight
		self.need_blind = need_blind #boolean value. need blind or need aware
		self.employment_weight = employment_weight
		self.commservice_weight = commservice_weight 
		self.otherach_weight = otherach_weight #other achievements

	
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
		
			'''rangelist = [self.highest, self.range1, self.range2, self.range3,
			self.range4, self.range5, self.range6, self.range7]'''

			ranking = [self.highest, [range(self.range1, self.highest)],
			[range(self.range2,self.range1)], [range(self.range3, self.range2)],
			[range(self.range4, self.range3)], [range(self.range5, self.range4)],
			[range(self.range6, self.range5)], [range(self.range7, self.range6)]]
		
			#ranking.index(self.highest) etc. to be used later
			'''
		
			n = 1
			while n < 8:
				for x in range(rangelist[n], rangelist[n-1]): #can maybe multiply gpa by 10 to solve this problem
					ranking[x] = n
				n += 1'''
		
		
	#making ranking list objects
	
	gpa_ranking = rangeranking(40, 39, 37, 35, 30) #everything multiplied by 10 cuz no floaty points
	sat_ranking = rangeranking(2400, 2300, 2200,2100, 2000)
	sat2_ranking = rangeranking(800, 780, 760, 720, 700)
	rec_ranking = wordranking('Excellent', 'Very Good', 'Good', 'Average')
	#ec_ranking = wordranking #ec_ranking contains 2 lists and different calculations
#1 list to get the level of activity eg international and another to get the persons
#position e.g vice president.	too lazy to do atm
	
	interview_ranking = wordranking('Excellent', 'Very Good', 'Good', 'Average')
	award_ranking = wordranking('International', 'National', 'Regional', 'State',
	'City', 'School')
	#external_ranking  10+ exams = 10+ grading scales lolno
	
	classrank_ranking = wordranking('Top 5%', 'Top 10%', 'Top 30%', 'Top 50%', 'Top 100%')
	
	employment_ranking = wordranking('Full Time', 'Part Time', 'Summer') # can add 2nd list for no. hours, length of time
	
	commservice_ranking = rangeranking(100, 50, 10, 0)
	
	otheracc_ranking = wordranking #another doube list ranking, not sure how to deal with atm.
	
	gpa_reduction_factor = self.gpa_weight/10
	gpa_points = [self.gpa_weight, self.gpa_weight - gpa_reduction_factor, 
	self.gpa_weight - 2 * gpa_reduction_factor, #etc]
	
	#maybe finda  better way to generate the point lists for everything
	#using dem loops
	
def points_calculator(user, school):
	user.gpa_points = school.gpa_points[school.gpa_ranking.index(user.gpa)] #somehow need to account 
	#for the fact that  school.gpa_ranking is a list of lists ...
	#find the index i.e ranking of the user gpa.
	#use that rank as the index in gpa_points 
	#i.e 4.0 = rank 0 = index 0 = full gpa weight.
	
	#etc 
	
	#add upp all points and bazinga, moar calculations required to find chances.
	#actually still need to create the actual chance % calculator algorithm.
	
def chances_calculator():
	pass
	