from nose.tools import *
from chanceme.main import School

def test_school():
	Harvard = School(name = 'Harvard University', gpa_weight=2000, sat_weight=1000, sat2_weight=1500, 
	rec_weight=900, interview_weight=500, eclevels_weight=500,
	ecpositions_weight=900,awardlevels_weight=500, classrank_weight=200,need_blind=True, 
	employment_weight=100,commservice_weight=1000, otherach_levels_weight=5000,otherach_positions_weight = 100)
	
	assert_equal(Harvard.name, "Harvard University")
	assert_equal(Harvard.gpa_weight, 2000)