import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://account.ikonpass.com/en/login"
driver = webdriver.Chrome()
driver.get(url)

u = driver.find_element_by_name('email')
u.send_keys('jjohnson11096@gmail.com')
p = driver.find_element_by_name('password')
p.send_keys(sys.argv[1])
p.send_keys(Keys.RETURN)



