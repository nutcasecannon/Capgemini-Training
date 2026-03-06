from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option(name="detach",value=True)
driver=Chrome(options=o)
driver.maximize_window()

''' Single Select Dropdown '''
# driver.get("https://demoqa.com/select-menu")
# sleep(10)
# a=driver.find_element("id","oldSelectMenu")
# o=Select(a)
# o.select_by_index(5)                # select_by_index
# o.select_by_value("10")             # select_by_value
# o.select_by_visible_text("Blue")    # select_by_visible_text

''' Multi Select Dropdown '''
# driver.get("https://demoqa.com/select-menu")
# sleep(10)
# a=driver.find_element("id","cars")
# o=Select(a)
# o.select_by_index(0)                    # select_by_index
# o.select_by_value("opel")               # select_by_value
# o.select_by_visible_text("Audi")        # select_by_visible_text
# o.deselect_by_index(0)                    # deselect_by_index
# o.deselect_by_value("opel")               # deselect_by_value
# o.deselect_by_visible_text("Audi")        # deselect_by_visible_text
# o.deselect_all()                          # deselect_all