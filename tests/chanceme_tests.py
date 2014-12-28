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
	
	


