import json
import mechanize

class Load_FB:


	#Facebook Mechanize session
	def __init__(self):
		with open('../config.json', 'r') as file:
			config = json.load(file)
		_email = config['email']
		_pass = config['pass']

		# Set Location of data file
		_input = '../' + config['input_file']
		_output = config['output_file']
		_api = config['gmaps-api-key']
		self._email = _email
		self._pass = _pass
		self._input = _input
		self._output = _output
		self._api = _api 
 		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		cookies = mechanize.CookieJar()
		browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US)     AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
		browser.open("https://m.facebook.com/")
		browser.select_form(nr=0)

		# Enter Facebook information of user that's performing the search
		browser.form['email'] = _email
		browser.form['pass'] = _pass
		response = browser.submit()
		self.browser = browser
		self.response = response

	def read_Response(self):
		 return self.response.read()
		
if __name__ == '__main__': 
	test = Load_FB()
	url ='https://m.facebook.com/search/top/?q=%s' % 8102934256
	print test.browser.open(url).read()
