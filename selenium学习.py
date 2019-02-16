from selenium import webdriver
from selenium.webdriver.common.keys import Keys
brower=webdriver.Firefox()
brower.get('http://www.python.org')
assert "Python" in brower.title
elem=brower.find_element_by_name("q")
elem.send_keys("pycodan")
elem.send_keys(Keys.RETURN)
print(brower.page_source)
print("success")