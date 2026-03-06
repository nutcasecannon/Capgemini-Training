from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

''' Launching the browser '''
o=ChromeOptions()
o.add_experimental_option(name="detach",value=True)
driver = Chrome(options=o)

''' Webdriver methods '''
# driver.get("https://www.instagram.com/")
# driver.get("https://www.facebook.com/")
# driver.back()
# sleep(4)  # to delay next execution since selenium script is faster than the browser
# driver.forward()
# driver.refresh()
# driver.minimize_window()
# driver.maximize_window()
# driver.quit()

''' Webdriver properties '''
# --------------------------------------Note------------------------------------------------
# If used directly after launching the Chrome window, the 3 properties return the following :
# current_url -> data:,
# title -> <blank line>
# page_source -> <html><head></head><body></body></html>
# ------------------------------------------------------------------------------------------
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)

''' Window / Current window handles '''
# driver.get("https://www.facebook.com/")
# sleep(6) # meanwhile manually open 2-4 tabs
# print(driver.window_handles)          # this will print ids of all tabs
# print(driver.current_window_handle)   # this will print id of first/current tab (the one with control)
# driver.quit()

''' To open instagram in another tab '''
# driver.get("https://www.facebook.com/")
# sleep(5) # manually open 1 tab
# a=driver.window_handles # stores id of second tab
# driver.switch_to.window(a[1]) # to switch control to second tab
# driver.get("https://www.instagram.com/")
# driver.quit()

''' To open instagram in another tab without manually opening a new tab '''
# driver.get("https://www.facebook.com/")
# sleep(3) # manually open 1 tab
# driver.switch_to.new_window('tab')
# driver.get("https://www.instagram.com/")
# driver.quit()

''' Close and Quit '''
# driver.get('https://www.instagram.com')
# sleep(3) # manually open 2 tab
# driver.close() # closes instagram tab
# sleep(3)
# driver.quit() # closes entire window

''' Window size '''
# driver.set_window_size(500,500)
# print(driver.get_window_size)