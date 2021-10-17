from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


#Open LinkedIn in Chrome browser
browser = webdriver.Chrome('/Users/ummaromanasama/Desktop/chromedriver')
browser.get('https://www.linkedin.com')

#Log into LinkedIn
browser.find_element_by_link_text('Sign in').click()
sleep(1.5)
browser.find_element_by_id('username').send_keys('email')
sleep(1.5)
browser.find_element_by_id('password').send_keys('password')
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

#New code

#Find total results
total_results = browser.find_element_by_class_name("display-flex.t-12.t-black--light.t-normal")     
total_results_int = int(total_results.text.split(' ',1)[0].replace(",",""))
print(total_results_int)
sleep(1.5)

#Get results
current_page = browser.current_url
results = browser.find_elements_by_class_name("occludable-update.artdeco-list__item--offset-4.artdeco-list__item.p0.ember-view")

#For each job sumbit application if no questions asked
for result in results:
    hover = ActionChains(browser).move_to_element(result)
    hover.perform()
  
def submit_apply(self,job_add):
    """This function submits the application for the job add found"""

    print('You are applying to the position of: ', job_add.text)
    job_add.click()
    sleep(2)
    
    # click on the easy apply button, skip if already applied to the position
    try:
        in_apply = self.driver.find_element_by_xpath("//button[@data-control-name='jobdetails_topcard_inapply']")
        in_apply.click()
    except NoSuchElementException:
        print('You already applied to this job, go to next...')
        pass
    time.sleep(1)

    # try to submit if submit application is available...
    try:
        submit = self.driver.find_element_by_xpath("//button[@data-control-name='submit_unify']")
        submit.send_keys(Keys.RETURN)
    
    # ... if not available, discard application and go to next
    except NoSuchElementException:
        print('Not direct application, going to next...')
        try:
            discard = self.driver.find_element_by_xpath("//button[@data-test-modal-close-btn]")
            discard.send_keys(Keys.RETURN)
            time.sleep(1)
            discard_confirm = self.driver.find_element_by_xpath("//button[@data-test-dialog-primary-btn]")
            discard_confirm.send_keys(Keys.RETURN)
            time.sleep(1)
        except NoSuchElementException:
            pass

    sleep(1)
