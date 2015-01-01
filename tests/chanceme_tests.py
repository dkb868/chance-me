from nose.tools import *
from chanceme.main import *

Harvard = School(name = 'Harvard University', gpa_weight=2000, sat_weight=1000, sat2_weight=1500, 
	rec_weight=900, interview_weight=500, ec_levels_weight=500,
	ec_positions_weight=900,awardlevels_weight=500, classrank_weight=200,need_blind=True, 
	employment_weight=100,commservice_weight=1000, otherach_levels_weight=5000,otherach_positions_weight = 100
	,minimumgpa=0,minimumsat=0,minimumsat2=0,minimumclassrank=0,idealsum=5000000)
	
def test_school():
	
	assert_equal(Harvard.name, "Harvard University")
	assert_equal(Harvard.gpa_weight, 2000)
	assert_equal(Harvard.sat_weight, 1000)
	assert_equal(Harvard.sat2_weight, 1500)
	assert_equal(Harvard.rec_weight, 900)
	assert_equal(Harvard.interview_weight, 500)
	assert_equal(Harvard.ec_levels_weight, 500)
	assert_equal(Harvard.ec_positions_weight, 900)
	assert_equal(Harvard.awardlevels_weight, 500)
	assert_equal(Harvard.classrank_weight, 200)
	assert_equal(Harvard.need_blind, True)
	assert_equal(Harvard.employment_weight, 100)
	assert_equal(Harvard.commservice_weight, 1000)
	assert_equal(Harvard.otherach_levels_weight, 5000)
	assert_equal(Harvard.otherach_positions_weight, 100)
	assert_equal(Harvard.minimumgpa, 0)
	assert_equal(Harvard.minimumsat, 0)
	assert_equal(Harvard.minimumsat2, 0)
	assert_equal(Harvard.minimumclassrank, 0)
	assert_equal(Harvard.idealsum, 5000000.0)
	
	
Jem = User(name = "Jem", gpa = "a", sat = 'a', sat2 = 'a', rec = 'a'
	, interview = 'a', award_list = ['a','a','a','a','a'],award_levels = ['a','a','a','a','a'], 
	ec_list = ['a','a','a','a','a'],
	ec_levels = ['a','a','a','a','a'], otherachlist = ['a','a','a','a','a'],
	otherach_levels = ['a','a','a','a','a'],
	otherach_positions = ['a','a','a','a','a'], ec_positions = ['a','a','a','a','a'], 
	classrank = 'a', finaid = False, 			
	international = False , URM = False, 
	legacy = False , ed = False, 
	firstgen = False ,
	employment = 'a', commservice = 'a')

def test_user():
	
	assert_equal(Jem.name, "Jem")
	assert_equal(Jem.gpa, "a")
	assert_equal(Jem.sat, "a")
	assert_equal(Jem.sat2, "a")
	assert_equal(Jem.rec, "a")
	assert_equal(Jem.interview, "a")
	assert_equal(Jem.award_list, ['a','a','a','a','a'])
	assert_equal(Jem.award_levels, ['a','a','a','a','a'])
	assert_equal(Jem.ec_list, ['a','a','a','a','a'])
	assert_equal(Jem.ec_levels, ['a','a','a','a','a'])
	assert_equal(Jem.otherachlist, ['a','a','a','a','a'])
	assert_equal(Jem.otherach_levels, ['a','a','a','a','a'])
	assert_equal(Jem.otherach_positions, ['a','a','a','a','a'])
	assert_equal(Jem.ec_positions, ['a','a','a','a','a'])
	assert_equal(Jem.classrank, "a")
	assert_equal(Jem.finaid, False)
	assert_equal(Jem.international, False)
	assert_equal(Jem.URM, False)
	assert_equal(Jem.legacy, False)
	assert_equal(Jem.ed, False)
	assert_equal(Jem.firstgen, False)
	assert_equal(Jem.employment, "a")
	assert_equal(Jem.commservice, "a")
	
	
def test_caseagainst():
	caseagainst(Jem, Harvard)
	assert_equal(Jem.redflags, 0)
	
def test_firstread():
	firstread(Jem, Harvard)
	
	assert_equal(Jem.gpa_points, 2000)
	assert_equal(Jem.sat_points, 1000)
	assert_equal(Jem.sat2_points, 1500)
	assert_equal(Jem.rec_points, 900)
	assert_equal(Jem.ec1_points, 450000)
	assert_equal(Jem.ec2_points, 450000)
	assert_equal(Jem.ec3_points, 450000)
	assert_equal(Jem.ec4_points, 450000)
	assert_equal(Jem.ec5_points, 450000)
	assert_equal(Jem.award1_points, 500)
	assert_equal(Jem.award2_points, 500)
	assert_equal(Jem.award3_points, 500)
	assert_equal(Jem.award4_points, 500)
	assert_equal(Jem.award5_points, 500)
	assert_equal(Jem.otherach1_points, 500000)
	assert_equal(Jem.otherach2_points, 500000)
	assert_equal(Jem.otherach3_points, 500000)
	assert_equal(Jem.otherach4_points, 500000)
	assert_equal(Jem.otherach5_points, 500000)
	assert_equal(Jem.interview_points, 500)
	assert_equal(Jem.classrank_points, 200)
	assert_equal(Jem.employment_points, 100)
	assert_equal(Jem.commservice_points, 1000)
	
	assert_equal(Jem.pointlist, [Jem.gpa_points, Jem.sat_points, Jem.sat2_points,
	Jem.rec_points, Jem.ec1_points, Jem.ec2_points,
	Jem.ec3_points,Jem.ec4_points,
	Jem.ec5_points, Jem.award1_points,
	Jem.award2_points, Jem.award3_points, 
	Jem.award4_points, Jem.award5_points, 
	Jem.otherach1_points, Jem.otherach2_points, 
	Jem.otherach3_points, Jem.otherach4_points, 
	Jem.otherach5_points, Jem.interview_points,  
	Jem.classrank_points, Jem.employment_points, 
	Jem.commservice_points 
	])
	
	assert_equal(Jem.toptenlist, [Jem.otherach1_points, Jem.otherach2_points, 
	Jem.otherach3_points, Jem.otherach4_points, 
	Jem.otherach5_points,Jem.ec1_points, Jem.ec2_points,
	Jem.ec3_points,Jem.ec4_points,
	Jem.ec5_points])
	
	assert_equal(Jem.toptensum, 4750000)
	
def test_committee():
	firstread(Jem, Harvard)
	committee(Jem, Harvard)
	assert_equal(Jem.chancedecimal, 0.95)