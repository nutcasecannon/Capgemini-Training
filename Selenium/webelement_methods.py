from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option(name="detach",value=True)
driver=Chrome(options=o)
driver.maximize_window()

''' submit() : Google Search'''
# driver.get("https://www.google.com")
# a=driver.find_element("class name","gLFyf")
# a.send_keys("Python Selenium")
# a.submit()

''' clear() : Fill username and password '''
# driver.get("https://demo.vtiger.com/vtigercrm/index.php")
# a=driver.find_element("id","username")
# b=driver.find_element("id","password")
# a.clear()
# b.clear()
# a.send_keys("ankita")   # without clear : these keys would've been appended to default values
# b.send_keys("bhunia")

''' is_displayed() : Check if 'Click the button' is visible or not. '''
# driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
# a=driver.find_element("id","myDIV")
# print(a.is_displayed())

''' is_enabled() : Check if text box is enabled or not. '''
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# sleep(5)
# a=driver.find_element("xpath","//input[@type='text']")
# print(a.is_enabled())
# won't work in instagram since it checks for 'disabled' but it is not there in instagram

''' is_selected() : Check if checkbox is selected or not. '''
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# sleep(5)
# a=driver.find_element("xpath","//input[@type='checkbox']")
# print(a.is_selected())

''' size,location,rect : Print details of username element '''
# driver.get("https://www.facebook.com")
# sleep(5)
# a=driver.find_element("name","email")
# print(a.size)
# print(a.location)
# print(a.rect)

''' get_attribute() : Check if checkbox is selected or not. '''
# driver.get("https://www.instagram.com")
# sleep(3)
# a=driver.find_element("name","email")
# print(a.get_attribute("type"))