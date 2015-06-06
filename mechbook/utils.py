import json
import mechanize

class Load_FB:

	def __init__(self):
		with open('../config.json', 'r') as file:
	    config = json.load(file)
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		cookies = mechanize.CookieJar()
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.open("https://www.facebook.com/login.php")
		browser.select_form(nr=0)
		# Enter Facebook information of user that's performing the search
		browser.form['email'] = config['email']
		browser.form['pass'] = config['pass']
		response = browser.submit()
		#print response.read()

	def data_up(self,datafile):
		findUsers = Identity(config['datafile'])
		return findUsers
