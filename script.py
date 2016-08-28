##################################################################
#
#	Robobrowser or url3/request approach abandoned due to issues with SSL certification. 
#	PITA, I tell you...
#
##################################################################

# import re
# from robobrowser import RoboBrowser

# browser = RoboBrowser(history=True)
# # browser.open('https://courses.iitm.ac.in/login/index.php')
# browser.open('http://playgo.to/iwtg/en/')

# import requests
# url = "https://courses.iitm.ac.in/login/index.php"
# returnResponse = requests.get(url, verify=False)

import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://courses.iitm.ac.in/login/index.php")

# ToDo : Add the encryption later.
f = open('../key.txt', 'r')
lines = f.readlines()
f.close()
username = lines[0][:-1]
password = lines[1][:-1]

print username, password

inputElement = driver.find_element_by_id("username")
inputElement.send_keys(username)
inputElement = driver.find_element_by_id("password")
inputElement.send_keys(password)

inputElement = driver.find_element_by_id("loginbtn")
inputElement.submit()

link = driver.find_element_by_link_text('My courses')
link.click()


####### Now choose all the courses one-by-one ####### 

# Add your own courses here
courses = ['CS6040', 'EE5176', 'CS6370', 'CS4100', 'CS4110', 'MS3910', 'HS4370']
courseIDs = [i + ':JUL-NOV 2016' for i in courses]

# courseIDs = ['CS4110:JUL-NOV 2016']
# material_counters = [0 for i in range(len(courseIDs))]
# forum_counters = [0 for i in range(len(courseIDs))]

notifications = []

i=0
for course in courseIDs:
	link = driver.find_element_by_link_text(course)
	link.click()
	# ids = driver.find_elements_by_xpath('//*[@id]')
	# for ID in ids:
	# 	print ID.get_attribute('id') 
	# material_counters[i] = len(ids)
	
	# print course + ' : ' + str(len(ids)) + ' : '
	
	links = driver.find_elements_by_partial_link_text('unread post')
	if len(links)==0:
		os.system('notify-send " '+ course + '" "Nothing new since last login."')
	else:
		for link in links:
			os.system('notify-send " '+ course + '" "' + link.get_attribute('text') + '"')
			notifications.append(course + ':' + link.get_attribute('text'))
 
	time.sleep(2)

 	##### For opening the posts then and there. #####
	# for link in links:
	# 	link.click()
	# 	posts = driver.find_element_by_class_name('unread')
	# 	all_children = post.find_elements_by_xpath(".//*")
	# 	l = all_children[0]
	# 	l.click()
	#	time.sleep(10)

	link = driver.find_element_by_link_text('My courses')
	link.click()
	# time.sleep(5)

print '\n'.join(notif for notif in notifications)


##### For testing purposes #####

# course = 'CS6040:JUL-NOV 2016'
# link = driver.find_element_by_link_text(course)
# link.click()
# ids = driver.find_elements_by_xpath('//*[@id]')
# for ID in ids:
# 	print ID.get_attribute('id') + ' : ' + ID.value
