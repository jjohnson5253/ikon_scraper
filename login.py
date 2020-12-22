import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
from bs4 import BeautifulSoup

url = "https://account.ikonpass.com/en/login"
driver = webdriver.Chrome()
driver.get(url)

u = driver.find_element_by_name('email')
u.send_keys('jjohnson11096@gmail.com')
p = driver.find_element_by_name('password')
p.send_keys(sys.argv[1])
p.send_keys(Keys.RETURN)

# wait for login to load (in seconds)
# TODO: see if there is a better way to wait for this. Like wait for a redirect?
# or see the minimum time needed (could be different for different people's computers)
time.sleep(3)

url = "https://account.ikonpass.com/en/myaccount/add-reservations/"
driver.get(url)

time.sleep(2)

#mountains = driver.find_element_by_class_name('sc-qQwsb kORfUh').get_attribute("innerHTML")
#mountain = driver.find_element_by_link_text('Arapahoe Basin')
#mountain = driver.find_element_by_id('react-autowhatever-resort-picker-section-0-item-1')
mountain = driver.find_element(By.XPATH, '//span[text()="Arapahoe Basin"]')
mountain.click();

cont = driver.find_element(By.XPATH, '//span[text()="Continue"]')
cont.click();

#day = driver.find_element_by_xpath("//div[@aria-label='Wed Dec 23 2020' and @class='DayPicker-Day']");
time.sleep(2)
day = driver.find_element(By.XPATH, '//div[@aria-label="Wed Dec 23 2020"]')
print(day.get_attribute('class'))



