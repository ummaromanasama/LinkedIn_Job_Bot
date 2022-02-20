from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import re
    
job_title = input("Enter job title:")

#Open LinkedIn in Chrome browser
browser = webdriver.Chrome('/Users/ummaromanasama/Desktop/chromedriver')
browser.get('https://www.linkedin.com')

def login_linkedin():
    #Log into LinkedIn
    browser.find_element_by_link_text('Sign in').click()
    sleep(1.5)
    browser.find_element_by_id('username').send_keys('email')
    sleep(1.5)
    browser.find_element_by_id('password').send_keys('password!')
    sleep(1.5)
    browser.find_element_by_xpath("//button[@type = 'submit']").click()
    sleep(1.5)

def job_search():
    #Go to jobs section
    browser.find_element_by_link_text('Jobs').click()
    sleep(1.5)

    browser.find_element_by_class_name('jobs-search-box__text-input').send_keys(job_title)
    sleep(1.5)

    search_location = browser.find_element_by_css_selector(".jobs-search-box__text-input[aria-label='City, state, or zip code']")
    search_location.clear()
    search_location.send_keys('New York, United States')
    sleep(1.5)

    browser.find_element_by_class_name("jobs-search-box__submit-button").click()
    sleep(1.5)
    
    #Easy Apply
    browser.find_element_by_xpath("//button[text()='Easy Apply']").click()

def find_offers():
    #Find total results
    total_results = browser.find_element_by_class_name("display-flex.t-12.t-black--light.t-normal")     
    total_results_int = int(total_results.text.split(' ',1)[0].replace(",",""))
    print(total_results_int)
        
    sleep(1.5)

    #Get results
    # current_page = browser.current_url
    results = browser.find_elements_by_class_name("jobs-search-results__list-item.occludable-update.p0.relative.ember-view")
    
    #For each job sumbit application if no questions asked
    for result in results:
        hover = ActionChains(browser).move_to_element(result)
        hover.perform()
        titles = result.find_elements_by_class_name("full-width.artdeco-entity-lockup__title.ember-view")
        for title in titles:
            submit_apply(title)
            
    # #  if there is more than one page, find the pages and apply to the results of each page
    #     if total_results_int > 24:
    #         sleep(2)

    #         # find the last page and construct url of each page based on the total amount of pages
    #         find_pages = browser.find_elements_by_class_name("artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view")
    #         total_pages = find_pages[len(find_pages)-1].text
    #         total_pages_int = int(re.sub(r"[^\d.]", "", total_pages))
    #         get_last_page = browser.find_element_by_xpath("//button[@aria-label='Page "+str(total_pages_int)+"']")
    #         get_last_page.send_keys(Keys.RETURN)
    #         sleep(2)
    #         last_page = browser.current_url
    #         total_jobs = int(last_page.split('start=',1)[1])
    #         print(total_pages_int)

    #         # go through all available pages and job offers and apply
    #         for page_number in range(25,total_jobs+25,25):
    #             browser.get(current_page+'&start='+str(page_number))
    #             sleep(2)
    #             results_ext = browser.find_elements_by_class_name("occludable-update.artdeco-list__item--offset-4.artdeco-list__item.p0.ember-view")
    #             for result_ext in results_ext:
    #                 hover_ext = ActionChains(browser).move_to_element(result_ext)
    #                 hover_ext.perform()
    #                 titles_ext = result_ext.find_elements_by_class_name('job-card-search__title.artdeco-entity-lockup__title.ember-view')
    #                 for title_ext in titles_ext:
    #                     submit_apply(title_ext)

    #     else:
    #         browser.close_session()
  
def submit_apply(job_add):
    """This function submits the application for the job add found"""
    
    print('You are applying to the position of: ', job_add.text)
    job_add.click()
    sleep(2)

    # click on the easy apply button, skip if already applied to the position
    try:
        in_apply = browser.find_element_by_xpath("//button[@data-control-name='jobdetails_topcard_inapply']")
        in_apply.click()
    except NoSuchElementException:
        print('You already applied to this job, go to next...')
        pass
    sleep(1)

    # try to submit if submit application is available...
    try:
        submit = browser.find_element_by_xpath("//button[@data-control-name='submit_unify']")
        submit.send_keys(Keys.RETURN)
        # browser.find_element_by_xpath("//button[@type = 'Submit application']").click()
        print('Hooray!')
        sleep(2)
        close_job = browser.find_element_by_xpath("//button[@data-test-modal-close-btn']")
        close_job.send_keys(Keys.RETURN)

    # ... if not available, discard application and go to next
    except NoSuchElementException:
        print('Not direct application, going to next...')
        try:
            discard = browser.find_element_by_xpath("//button[@data-test-modal-close-btn]")
            discard.send_keys(Keys.RETURN)
            sleep(1)
            discard_confirm = browser.find_element_by_xpath("//button[@data-test-dialog-secondary-btn]")
            discard_confirm.send_keys(Keys.RETURN)
            sleep(1)
        except NoSuchElementException:
            pass

    sleep(1)

def close_session():
    """This function closes the actual session"""
    
    print('End of the session, see you later!')
    browser.close()
    
def apply():
        """Apply to job offers"""

        browser.maximize_window()
        login_linkedin()
        sleep(5)
        job_search()
        sleep(2)
        find_offers()
        sleep(2)
        # close_session()
        
apply()
