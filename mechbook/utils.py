import json
import mechanize
from reverse import Identity

class Load_FB:

	def __init__(self):
		with open('../config.json', 'r') as file:
			config = json.load(file)
		_email = config['email']
		_pass = config['pass']
		_data = config['datafile']
		self._email = _email
		self._pass = _pass
		self._data = _data
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		cookies = mechanize.CookieJar()
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.open("https://www.facebook.com/login.php")
		browser.select_form(nr=0)
		# Enter Facebook information of user that's performing the search
		browser.form['email'] = _email
		browser.form['pass'] = _pass
		response = browser.submit()
		#print response.read()

	def data_up(self):
		findUsers = Identity('../' + self._data)
		return findUsers

if __name__ == '__main__': 
	testingUtils = Load_FB()
	run = testingUtils.data_up()
	print run.site_Test(8102934256)
