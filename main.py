from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

chrome_driver_path = "/media/user/SSD/web/AngelaYu/Python/ChromeDriver/chromedriver"
linkedin_url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# Setting up Selenium Driver:
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url=linkedin_url)

# Auto-click on Sign in button in LinkedIn main webpage:
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()
sleep(2)

# Auto-fill username field:
username = driver.find_element_by_id(id_="username")
username.send_keys(os.environ.get("USERNAME"))
sleep(0.5)

# Auto-fill password field:
password = driver.find_element_by_id(id_="password")
password.send_keys(os.environ.get("PASSWORD"))
sleep(1)

# Auto-submit:
submit = driver.find_element_by_tag_name(name="button")
submit.click()
sleep(2)

# Auto-apply for jobs :

# 1. Job title link click:
job = driver.find_element_by_link_text("Python Developer")
job.click()
sleep(2)
try:
    # Auto-save job;
    save = driver.find_element_by_class_name("jobs-save-button")
    save.click()
    sleep(2)

    # Auto-apply for a job:
    apply = driver.find_element_by_class_name(name="jobs-apply-button")
    apply.click()
    sleep(1)

    # Auto-fill phone number:
except NoSuchElementException:
    print("1 Job was not found")

else:
    phone = driver.find_element_by_id(
        id_="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2328433260,15578714,phoneNumber~nationalNumber)")
    phone.send_keys("123456789")
    sleep(1)

    # Auto-click Next button
    next_button = driver.find_element_by_tag_name(name="button")
    next_button.click()

    # Apply to all jobs in a page: