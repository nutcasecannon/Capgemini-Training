'''
Questions
1. Navigate to amazon and print all category names.
2. Print top 10 movie names from IMDB Top 250
3. Count all images on amazon
4. Open https://demoqa.com/select-menu
Target first dropdown in that page and select first option
5.	Print All Links in amazon Page
6.	Print Auto Suggestions of any site
7.	From the “Accounts & Lists” section on the Amazon homepage, select the “Your Wish List” option.
8.	Access the content displayed inside the embedded page and print the heading text visible inside it.
https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe
9.	Search Laptop and print all product titles.
'''
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

'''1st Question'''
# driver.get("https://www.amazon.in")
# sleep(4)
# a=driver.find_elements("xpath","//div[@class='nav-div']")
# for i in a :
#     print(i.text)

'''2nd Question'''
# driver.get("https://imdb.com/chart/top/")
# a=driver.find_elements("xpath","//h3[@class='ipc-title__text']")
# for i in range(0,10) :
#     print(f'{i+1}. {a[i].text}')

'''3rd Question'''
# driver.get("https://www.amazon.in")
# sleep(4)
# a=driver.find_elements("xpath","//img")
# print(len(a))

'''4th Question'''
# driver.get("https://demoqa.com/select-menu")
# sleep(3)
# driver.find_element(By.ID, "withOptGroup").click()
# sleep(2)
# driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()
# sleep(2)

'''5th Question'''
# driver.get("https://www.amazon.in/")
# sleep(3)
# links = driver.find_elements(By.TAG_NAME,"a")
# for link in links:
#     print(link.text)

''' Question 6 '''
# driver.get("https://www.google.com")
# search = driver.find_element(By.NAME,"q")
# search.send_keys("football")
# sleep(3)
# suggestions = driver.find_elements(By.XPATH,"//li[@role='presentation']")
# for s in suggestions:
#     print(s.text)

''' Question 7 '''
# driver.get("https://www.amazon.in/")
# sleep(4)
# a = driver.find_element("id", "nav-link-accountList")
# o = ActionChains(driver)
# o.move_to_element(a).perform()
# sleep(2)
# driver.find_element(By.LINK_TEXT, "Your Wish List").click()

''' Question 8 '''
# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
# driver.switch_to.frame("iframeResult")
# driver.switch_to.frame(0)
# a = driver.find_element(By.TAG_NAME, "h1").text
# print(a)

''' Question 9 '''
# driver.get("https://www.amazon.in/")
# sleep(5)
# a = driver.find_element("id", "twotabsearchtextbox")
# a.send_keys("Laptop")
# a.send_keys(Keys.ENTER)
# sleep(3)
# a = driver.find_elements("xpath", "//h2//span")
# for i in a:
#     print(i.text)
