from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
driver.get("http://my.bupt.edu.cn/index.portal")
user=driver.find_element_by_id("user_name")
user.send_keys("2014212999")
passwd=driver.find_element_by_name("password")
passwd.send_keys("11")
login=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div[2]/form/button")
login.click()
