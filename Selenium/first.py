''' On Execution of below lines, Chrome and Edge open and close immediately.
However, in case of Firefox, the browser stays open. '''

# from selenium.webdriver import Chrome, Edge, Firefox
# chrome_driver = Chrome()
# edge_driver = Edge()
# firefox_driver = Firefox()

''' To keep Chrome/Edge browser open. '''
from selenium.webdriver import Chrome, ChromeOptions
o=ChromeOptions()
o.add_experimental_option(name="detach",value=True)
driver=Chrome(options=o)

# The above syntax works for Chrome and Edge. It gives an error for Firefox.