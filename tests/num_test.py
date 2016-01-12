import mechanize
import re
import time

# BROKEN
class Run_Tests:

	def __init__(self, filename):
		dataIn = open(filename, 'rU')
		self.filename = filename
		phoneBook = []
		self.phoneBook = phoneBook
		self.failedCounter = 0
		for row in dataIn:
			cells = row.split(',')
			if 'phone' in row:
				self.phoneBook.append(cells[2].rstrip())		
		print '*** Reading CSV ****'

	def site_Test(self, number = 8102934256):
		username = self.open_File(number)
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return 'Successfully connected, reverse search works'
		else:
			return 'FAILED'

if __name__ == '__main__': 
	#Debugging
	print Load_FB('input.csv').site_Test()

