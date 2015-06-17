#!/usr/bin/python

import json
import mechanize
from fb_utils import Load_FB
import time
from bs4 import BeautifulSoup

class Identity:

	def __init__(self, browser, filename):
		dataIn = open(filename, 'rU')
		self.browser = browser
		self.filename = filename
		phoneBook = []
		self.phoneBook = phoneBook
		self.failedCounter = 0
		for row in dataIn:
			cells = row.split(',')
			if 'phone' in row:
				self.phoneBook.append(cells[2].rstrip())		
		print '*** Reading CSV ****'

	def mechRead(self,url):
		browser = self.browser
		sitetest = browser.open(url)
		site = sitetest.read()
		return site

	def open_File(self, number):
		self.number = number
		url = 'https://www.facebook.com/search/str/%%20%s/keywords_top' % str(number)
		site = self.mechRead(url)
		return site

	def site_Test(self, number = 8102934256):
		username = self.open_File(number)
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return 'Successfully connected, reverse search works'
		else:
			return 'FAILED'

	def get_Name(self, number):
		username = self.open_File(number)
		# Scrape between '<div class="_5d-5">' and '<div class="_glm">' for facebook profile name
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return fullName
		else:
			return 'None'

	def get_URL(self, number):
		username = self.open_File(number)
		# Scrape between '<div class="_5d-5">' and '<div class="_glm">' for facebook profile name
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_gll"><a href="')[1]
			nameSplit2 = nameSplit1.split('<div class="_6a _6b _5d-4">')[0]
			fullURL = nameSplit2.split('?ref=br_rs">')[0]
			return fullURL
		else:
			self.failedCounter +=1
			return 'None'

	def get_City(self, url):
		city = 'None'
		site = self.mechRead(url)
		if 'hovercard="/ajax/hovercard/page.php?id=112222822122196">' in site:
			nameSplit1 = site.split('hovercard="/ajax/hovercard/page.php?id=112222822122196">')[2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
			nameSplit2 = nameSplit1.split('</a></div>')[0]
			soup = BeautifulSoup(nameSplit2)
			city = soup.getText()
		return city

	def get_Job(self, url):
		site = self.mechRead(url)
		nameSplit1 = site.split('<div class="_42ef"><div><div class="_50f3">')[1]
		nameSplit2 = nameSplit1.split('<span class="_50f8">')[0]
		soup = BeautifulSoup(nameSplit2)
		job = soup.getText()
		return job.encode("utf-8")

	def get_intel(self, areaName):
		firstName = name[0]
		lastName = name[-1]
		# if there's a middle name, these are usually made up by facebook users
		if len(name) == 3:
			middleName = name[1]
		url = 'http://www.intelius.com/results.php?ReportType=1&formname=name&qf=%s&qmi=&qn=%s&qcs=%s&focusfirst=1' % (firstName, lastName, areaName)
		#TO DO: Parse the intelius link. For now this is not neccessary. 
		browser = self.browser
		sitetest = browser.open(url)
		site = sitetest.read()
		#nameSplit1 = site.split('We found')[1]
		#nameSplit2 = nameSplit1.split('</p>')[0]
		#soup = BeautifulSoup(nameSplit2)
		#intel = soup.getText()
		return url.encode("utf-8")

	def get_areaCode(self, number):
		url = 'http://www.allareacodes.com/' + str(number)
		site = self.mechRead(url)
		nameSplit1 = site.split('<td>Major City:</td>')[1]
		nameSplit2 = nameSplit1.split('</td>')[0]
		soup = BeautifulSoup(nameSplit2)
		area = soup.getText()
		return area.encode("utf-8")

	def get_phoneBook(self):
		print "Phone numbers found: %s" % (len(self.phoneBook))
		return self.phoneBook

	def write_data(self, data, name):
		text_file = open(name, "w")
		text_file.write(str(data))
		text_file.close()

if __name__ == '__main__':
	#Site Test
	search = Load_FB()
	# Set delay in seconds between requests so Facebook doesnt get overloaded
	delay = 1
	findUsers = Identity(search.browser,search._data)
	print findUsers.site_Test()
	identityList = []

	for i in findUsers.phoneBook:
		name = findUsers.get_Name(i)
		if name != 'None':
			phone = i
			url = findUsers.get_URL(i)
			city = findUsers.get_City(url)
			job = findUsers.get_Job(url)
			areaName = findUsers.get_areaCode(phone)
			intel = findUsers.get_intel(areaName)
			if [name,url] not in identityList:
				identityList.append([name,url,city,job,areaName,intel])
				print '%s, %s, %s, %s, %s, %s, %s' % (phone,name,url,city,job,areaName,intel)
		else:
			print 'Searching...'
		time.sleep(delay)
	
	print str(identityList)
	print '%d unique identities found.\n%d numbers unidentitified.' % (len(identityList),findUsers.failedCounter)
	findUsers.write_data(str(identityList), 'output.csv')
	
