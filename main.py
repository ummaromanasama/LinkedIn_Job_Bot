from selenium import webdriver
from time import sleep


#Open LinkedIn in Chrome browser
browser = webdriver.Chrome('/Users/ummaromanasama/Desktop/chromedriver')
browser.get('https://www.linkedin.com')

#Log into LinkedIn
browser.find_element_by_link_text('Sign in').click()
sleep(1.5)
browser.find_element_by_id('username').send_keys('insert_email')
sleep(1.5)
browser.find_element_by_id('password').send_keys('insert_password!')
sleep(1.5)
browser.find_element_by_xpath("//button[@type = 'submit']").click()
sleep(1.5)

#Go to jobs section
browser.find_element_by_link_text('Jobs').click()
sleep(1.5)

browser.find_element_by_class_name('jobs-search-box__text-input').send_keys('Engineer')
sleep(1.5)

browser.find_element_by_class_name("jobs-search-box__submit-button").click()
sleep(1.5)

#Easy Apply
browser.find_element_by_xpath("//button[text()='Easy Apply']").click()

