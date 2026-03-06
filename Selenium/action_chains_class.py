from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains

o=ChromeOptions()
o.add_experimental_option(name="detach",value=True)
driver=Chrome(options=o)
driver.maximize_window()

o=ActionChains(driver)      # Creates ActionChains object to perform user interactions

''' Clicks/Hover using ActionChains '''

# driver.get("https://www.google.com/")
# a=driver.find_element("xpath","//a[.='Gmail']")
# o.click(a).perform()                            # click

# driver.get("https://demoqa.com/buttons")
# sleep(2)
# a=driver.find_element("id","doubleClickBtn")
# o.double_click(a).perform()                     # double_click
# b=driver.find_element("id","rightClickBtn")
# o.context_click(b).perform()                    # right_click

# driver.get("https://amazon.in/")
# sleep(4)
# a=driver.find_element("id","nav-link-accountList")
# o.move_to_element(a).perform()                  # hover
