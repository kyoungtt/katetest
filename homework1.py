# -*- coding: utf-8 -*-
from __future__ import division
#Declarations
#The dictionary of parameters
#name,bname,type,family,unit,value,mode,description,group,min,max,list,enable,iscombocheckbox,isused
parameterDict = {}
try:
	if Parameter:
		pass
except NameError:
	class Parameter:
		def __init__(self, **d):
			pass
#DeclarationsEnd
### for every variable in every dataset in every well, 
###print the variables that are missing units and families
import TechlogDatabase as db

for w in db.wellList():
	for d in db.datasetList(w):
		vnulist,vnfamlist = [], []
		countvar=countvarfam =0
		for v in db.variableList(w,d):
			#check for missing values
			unit=db.variableUnit(w,d,v)
			if (not unit) or (unit == '-'):
				countvar = countvar + 1
				vnulist.append(v)
			family = db.variableFamily(w,d,v)	
			if (family == ''):
				countvarfam = countvarfam +1
				vnfamlist.append(v)
		if countvar>0:
				print 'in', w, 'in dataset', d, countvar, 'variable(s) do not have units:', vnulist
		if countvarfam>0:
				print 'in', w, 'in dataset', d, countvar, 'variable(s) do not have family:', vnfamlist	
	print '---------------------------------------------------------------------------------------------------------------------------------------'				

__author__ = """Kathryn YOUNG (younkt)"""
__date__ = """2015-09-24"""
__version__ = """1.0"""
__group__ = """"""
__suffix__ = """"""
__prefix__ = """"""