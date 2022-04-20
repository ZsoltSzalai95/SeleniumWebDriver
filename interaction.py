from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/.../chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

fname = driver.find_element_by_name("fName")
fname.send_keys("FirstName")
lname = driver.find_element_by_name("lName")
lname.send_keys("LastName")
email = driver.find_element_by_name("email")
email.send_keys("asd123@321dsa.asd")
#OR
# email.send_keys(Keys.ENTER)

signbutton = driver.find_element_by_css_selector(".btn")
signbutton.click()