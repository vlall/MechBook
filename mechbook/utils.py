#!/usr/bin/python

import mechanize
import re
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import time
import json
import mechanize
from utils import Load_FB
 
class Identity:

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

	def open_File(self,browser, number):
		self.number = number
		sitetest = browser.open('https://www.facebook.com/search/str/%%20%s/keywords_top' % str(number))
		site = sitetest.read()
		return site

	def site_Test(self,browser, number = 8102934256):
		username = self.open_File(browser,number)
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

	def get_phoneBook(self):
		print "Phone numbers found: %s" % (len(self.phoneBook))
		return self.phoneBook

if __name__ == '__main__':
	#Site Test
	search = Load_FB()
	findUsers = Identity('../' + search._data)
	print findUsers.site_Test(search.get_Browser(),8102934256)

	'''
	identityList = []
	for i in findUsers.phoneBook:
		name = findUsers.get_Name(i)
		url = findUsers.get_URL(i)
		if name != 'None':
			if [name,url] not in identityList:
				identityList.append([name,url])
				print '%s, %s' % (name,url)
		else:
			print 'Searching...'
		time.sleep(1)
	
	print identityList
	print '%d unique identities found.\n %d numbers unidentitified.' % (len(identityList),findUsers.failedCounter)
	text_file = open("data_Out.csv", "w")
	text_file.write(str(identityList))
	text_file.close()
	'''
