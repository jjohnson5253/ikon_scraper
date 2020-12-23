import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
from bs4 import BeautifulSoup

monthInput = 'March'
yearInput = '2021'

# class name if the day is available
AVAILABLE = 'DayPicker-Day'

# open login page
url = "https://account.ikonpass.com/en/login"
driver = webdriver.Chrome()
driver.get(url)

# send login parameters
username = driver.find_element_by_name('email')
username.send_keys('jjohnson11096@gmail.com')
password = driver.find_element_by_name('password')
password.send_keys(sys.argv[1])
password.send_keys(Keys.RETURN)

# Click 'Make a Reservation' button
try:
	# wait for page to load
	resButton = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//span[text()="Make a Reservation"]')))
except:
	print("Error: Timed out")
# use a javascript click, the selenium click not working
driver.execute_script("arguments[0].click();", resButton) 

# Select mountain
try:
	# wait for page to load
	mountain = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//span[text()="Arapahoe Basin"]')))
except:
	print("Error: Timed out")
mountain.click();

# Click 'Continue' button
try:
	# wait for page to load
	contButton = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//span[text()="Continue"]')))
except:
	print("Error: Timed out")
contButton.click()

# check if correct month is being checked
try:
	# wait for page to load
	monthBeingChecked = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
except:
	print("Error: Timed out")
if (monthBeingChecked.get_attribute('innerHTML') != (monthInput + ' ' + yearInput)):
	print('WRONG MONTH')

# loop through months until correct month is being checked

while (monthBeingChecked.get_attribute('innerHTML') != (monthInput + ' ' + yearInput)):
	# go to next month
	nextMonthButton = driver.find_element(By.XPATH, '//i[@class="amp-icon icon-chevron-right"]')
	nextMonthButton.click()
	try:
		monthBeingChecked = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//span[@class="sc-pckkE goPjwB"]')))
	except:
		print("Error: Timed out")
	time.sleep(1)
	print(monthBeingChecked.get_attribute('innerHTML'))



# Check if day is available by reading class
try:
	# wait for page to load
	day = WebDriverWait(driver, 20).until(
	EC.presence_of_element_located((By.XPATH, '//div[contains(@aria-label,"Mar 23")]')))
except:
	print("Error: Timed out")

if (day.get_attribute('class') == AVAILABLE):
	print("This day is available")



