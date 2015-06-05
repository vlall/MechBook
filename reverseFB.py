#!/usr/bin/python

import mechanize
import re
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import time

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

	def open_File(self, number):
		self.number = number
		sitetest = browser.open('https://www.facebook.com/search/str/%%20%s/keywords_top' % str(number))
		site = sitetest.read()
		return site

	def site_Test(self, number = 8102934256):
		username = self.open_File(number)
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return 'SUCCESS'
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
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	cookies = mechanize.CookieJar()
	browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
	browser.open("https://www.facebook.com/login.php")
	browser.select_form(nr=0)
	# Enter Facebook information of user that's performing the search
	browser.form['email'] = 'YOUR_EMAIL'
	browser.form['pass'] = 'YOUR_PASS'
	response = browser.submit()
	findUsers = Identity('hadoop-small.csv')
	#print response.read()

	#print findUsers.get_phoneBook()
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





