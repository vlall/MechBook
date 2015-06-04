#!/usr/bin/python

import mechanize
import re
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup
import time

class Identity:

	def __init__(self, filename):
		dataIn = open(filename, 'rU')
		phoneBook = []
		self.filename = filename
		self.phoneBook = phoneBook
		for row in dataIn:
			cells = row.split(',')
			if 'phone' in row:
				phoneBook.append(cells[2].rstrip())		

	def get_Name(self, number):
		self.number = number
		sitetest = browser.open('https://www.facebook.com/search/str/%%20%s/keywords_top' % str(number))
		site = sitetest.read()
		username = site
		# Scrape between '<div class="_5d-5">' and '<div class="_glm">' for facebook profile name
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_5d-5">')[1]
			nameSplit2 = nameSplit1.split('<div class="_glm">')[0]
			fullName = nameSplit2.split('</div>')[0]
			return fullName
		else:
			return 'None'


	def get_URL(self, number):
		self.number = number
		sitetest = browser.open('https://www.facebook.com/search/str/%%20%s/keywords_top' % str(number))
		site = sitetest.read()
		username = site
		# Scrape between '<div class="_5d-5">' and '<div class="_glm">' for facebook profile name
		if '<div class="_5d-5">' in username:
			nameSplit1 = username.split('<div class="_gll"><a href="')[1]
			nameSplit2 = nameSplit1.split('<div class="_6a _6b _5d-4">')[0]
			fullURL = nameSplit2.split('?ref=br_rs">')[0]
			return fullURL
		else:
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
	browser.form['email'] = 'User_Email'
	browser.form['pass'] = 'User_Password'
	response = browser.submit()
	findUsers = Identity('hadoop-small.csv')
	#print response.read()

	#print findUsers.get_phoneBook()
	identityList = []
	for i in findUsers.phoneBook:
		if findUsers.get_Name(i) != 'None':
			if findUsers.get_Name(i) not in identityList:
				identityList.append([findUsers.get_Name(i),findUsers.get_URL(i)])
			print '%s, %s' % (findUsers.get_Name(i),findUsers.get_URL(i))
		time.sleep(1)

	print identityList
	text_file = open("data_Out.csv", "w")
	text_file.write(identityList)
	text_file.close()
