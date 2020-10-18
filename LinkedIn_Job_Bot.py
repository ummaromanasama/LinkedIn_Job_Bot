#Import modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Open LinkedIn in Chrome browser
browser = webdriver.Chrome('/Users/ummaromanasama/Desktop/chromedriver85')
browser.get('https://www.linkedin.com')

#Log into LinkedIn
browser.find_element_by_link_text('Sign in').click()
sleep(1.5)
browser.find_element_by_id('username').send_keys('Email')
sleep(1.5)
browser.find_element_by_id('password').send_keys('Password')
sleep(1.5)
browser.find_element_by_xpath("//button[@type = 'submit']").click()
sleep(1.5)

#Goes to LinkedIn jobs page
browser.get('https://www.linkedin.com/jobs/search/')

job = ['Customer Service']

jobID = browser.find_element_by_class_name('jobs-search-box__text-input')
#Send input
jobID.send_keys(job)

#Click Search
browser.find_element_by_class_name("jobs-search-box__submit-button").click()
sleep(1.5)

#Filter: Experience Level 
browser.find_element_by_xpath("//span[text()='Experience Level']").click()

#Checkbox: Experience Level 
browser.find_element_by_xpath("//span[text()='Internship']").click()
browser.find_element_by_xpath("//span[text()='Entry level']").click()
browser.find_element_by_xpath("//span[text()='Associate']").click()
sleep(1.5)

#Need help with clickong Apply, maybe I need a different approach?
# browser.find_element_by_xpath("//button[.//span='Apply']").click()
sleep(1.5)

#Filter: Experience Level 
browser.find_element_by_xpath("//span[text()='Job Type']").click()

#Checkbox: Experience Level 
browser.find_element_by_xpath("//span[text()='Part-time']").click()
browser.find_element_by_xpath("//span[text()='Internship']").click()
sleep(1.5)




