# MechBook
Mechbook allows you to Mechanize Facebook reverse searches- given a csv list containing phone numbers, reverse search facebook profile names and links of posters.
#####TO DO
- Make Testing Folder
- Fix Dependencies

##Dependencies
- Mechanize
- Apache Tika

##Running MechBook
1. Once you have Mechanize installed, you need to put your Facebook credentials inside the config.json file (Make sure you do not accidentally commit this file...) 

  ```
  "email" : "facebook_EMAIL",
  "pass" : "facebook_PASS",
  ```
2. Next, you can leave the default input.csv for testing, or put in your own phone numbers.  
  ```
  "input_file" : "input.csv",
  ```

3. You can run the testing file to see if you can connect. Scrape and understand your data with Apache Tika.
  ```
  $ python fb_utils.py > out.txt
  $ python tika_read.py
  ```
  
4. At this point, scraping should be easy! Here's an example.  
  ```
import tika
from tika import parser
from fb_utils import Load_FB

# Mechanize into Your Facebook Profile
test = Load_FB()
url ='https://m.facebook.com/search/top/?q=%s' % TESTING_NUMBER
myPage = test.browser.open(url).read()
print myPage

# Save to out.txt
fileOut = open("out.txt", "w")
fileOut.write(myPage)	
fileOut.close

# Use Apache Tika to analyze out.txt
parsed = parser.from_file('out.txt')
print parsed["content"]
print parsed["metadata"]
	```
