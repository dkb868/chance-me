from nose.tools import *
from chanceme.main import *

Harvard = School(name = 'Harvard University', gpa_weight=2000, sat_weight=1000, sat2_weight=1500, 
	rec_weight=900, interview_weight=500, ec_levels_weight=500,
	ec_positions_weight=900,awardlevels_weight=500, classrank_weight=200,need_blind=True, 
	employment_weight=100,commservice_weight=1000, otherach_levels_weight=5000,otherach_positions_weight = 100
	,minimumgpa=0,minimumsat=0,minimumsat2=0,minimumclassrank=0)
	
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
	
	
Jem = User(name = "Jem", gpa = -1, sat = 'a', sat2 = 'a', rec = 'a'
	, interview = 'a', award_list = [0],award_levels = [0], ec_list = [0],
	ec_levels = [0], otherachlist = [0], otherach_levels = [0],
	otherach_positions = [0], ec_positions = [0], 
	classrank = 'a', finaid = False, 			
	international = False , URM = False, 
	legacy = False , ed = False, 
	firstgen = False ,
	employment = 'a', commservice = 'a')

def test_user():
	
	assert_equal(Jem.name, "Jem")
	assert_equal(Jem.gpa, -1)
	assert_equal(Jem.sat, "a")
	assert_equal(Jem.sat2, "a")
	assert_equal(Jem.rec, "a")
	assert_equal(Jem.interview, "a")
	assert_equal(Jem.award_list, [0])
	assert_equal(Jem.award_levels, [0])
	assert_equal(Jem.ec_list, [0])
	assert_equal(Jem.ec_levels, [0])
	assert_equal(Jem.otherachlist, [0])
	assert_equal(Jem.otherach_levels, [0])
	assert_equal(Jem.otherach_positions, [0])
	assert_equal(Jem.ec_positions, [0])
	assert_equal(Jem.classrank, "a")
	assert_equal(Jem.finaid, False)
	assert_equal(Jem.international, False)
	assert_equal(Jem.URM, False)
	assert_equal(Jem.legacy, False)
	assert_equal(Jem.ed, False)
	assert_equal(Jem.firstgen, False)
	assert_equal(Jem.employment, "a")
	assert_equal(Jem.commservice, "a")
	
	
def test_case_against():
	caseagainst(Jem, Harvard)
	assert_equal(Jem.redflags, 1)