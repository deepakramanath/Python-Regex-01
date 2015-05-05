#!/usr/bin/python
# Deepak Ramanath

# Python Program to extract the temperature values from the data file using regex

import sys
import re
import os
import matplotlib.pyplot as plt

# Pattern compiling
headerPattern = re.compile(r'(?P<pCode>[A-Za-z]+[ ]?[a-z]+),(?P<sNumber>(\w+[ ]?)+),(?P<ymd>(\w+,?){,3}),(?P<maxT>(\w+[ ]?\w+)),')
productCode = re.compile(r'(?P<pC>\w+)')
stationNumber = re.compile(r'\w+,(?P<sN>\d+)')
ymd = re.compile(r'\w+,\d+,(?P<year>\d+),(?P<month>\d+),(?P<day>\d+)')
maxTemp = re.compile(r'\w+,(\d+,){,4}(?P<mT>\d+.\d+)')

# Lists
monthValue = []
dayValue = []
maxTempValue = []

# Opening the data file
with open('data.txt', 'r') as data:
	for line in data:

		if not 'IDCJAC0010' in line:
			headerSearch = headerPattern.search(line.strip())
			print headerSearch.group('pCode')
			print headerSearch.group('sNumber')
			print headerSearch.group('ymd')
			print headerSearch.group('maxT')

		if not 'Product' in line:
			pCSearch = productCode.search(line.strip())
			sNSearch = stationNumber.search(line.strip())
			ymdSearch = ymd.search(line.strip())
			maxTempSearch = maxTemp.search(line.strip())
			
			month = ymdSearch.group('month')
			day = ymdSearch.group('day')
			mTemp = maxTempSearch.group('mT')
			
			monthValue.append(month)
			dayValue.append(day)
			maxTempValue.append(mTemp)

# All values as Tuples 
dataValues = zip(monthValue, dayValue, maxTempValue)

# Example for January's maximum day temperature
janValues = dataValues[0:31]
janDay = [x[1] for x in janValues]
janTemp = [x[2] for x in janValues]

# Example for February's maximum day temperature
febValues = dataValues[len(janValues)+1:len(janValues)+28]
febDay = [x[1] for x in febValues]
febTemp = [x[2] for x in febValues]

#Plots for each month
if janValues:
	plt.plot(janDay, janTemp)
	plt.xlabel('Days')
	plt.ylabel('Temperature [C]')
	plt.xlim(1,len(janValues))
	plt.title('Maximum temperature for the month of January, Station ID: IDCJAC0010')
	plt.show()
else:
	print "Evaluate January values"

if febValues:
	plt.plot(febDay,febTemp)
	plt.xlabel('Days')
	plt.ylabel('Temperature [C]')
	plt.xlim(1, len(febValues))
	plt.title('Maximum temperature for the month of Februrary, Station ID: IDCJAC0010')
	plt.show()
else:
	print "Evaluate Februrary values"
