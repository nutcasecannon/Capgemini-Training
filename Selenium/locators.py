from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option(name="detach",value=True)
driver=Chrome(options=o)
from time import sleep
driver.maximize_window()

'''Without importing'''
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element("id","username").send_keys("nutcasecannon")
# driver.find_element("id","password").send_keys("123456")

# driver.get("https://instagram.com")
# driver.find_element(by="id",value="_R_32d9lplcldcpbn6b5ipamH1_").send_keys("nutcasecannon")
# driver.find_element(by="id",value="_R_33d9lplcldcpbn6b5ipamH1_").send_keys("123456")

'''With importing'''
# from selenium.webdriver.common.by import By
# driver.find_element(By.ID,"username").send_keys("nutcasecannon")

'''ID Attribute (Fill registration form)'''
# driver.get("https://demowebshop.tricentis.com/register")
# driver.find_element(By.ID,"gender-female").click()
# driver.find_element(By.ID,"FirstName").send_keys("Ankita")
# driver.find_element(By.ID,"LastName").send_keys("Bhunia")
# driver.find_element(By.ID,"Email").send_keys("ankitabhunia24@gmail.com")

'''find_element vs find_elements'''
# a=driver.find_element("class name","text-box.single-line")
# b=driver.find_elements("class name","text-box.single-line")
# print(a)
# print(b)

'''Class Locator (Login)'''
# driver.get("https://www.saucedemo.com/")
# driver.find_elements("class name","input_error.form_input")[0].send_keys("standard_user")
# driver.find_elements("class name","input_error.form_input")[1].send_keys("secret_sauce")
# driver.find_element("class name", "submit-button.btn_action").click()

'''Google Search'''
# driver.get("https://www.google.com")
# driver.find_element("class name","gLFyf").send_keys("Cat pictures")   # give sleep(2) after this
# driver.find_element("class name","gNO89b").click()                    # works with sleep

'''Name Locator (Login)'''
# driver.get("https://www.saucedemo.com/")
# driver.find_element("name","user-name").send_keys("standard_user")
# driver.find_element("name","password").send_keys("secret_sauce")
# driver.find_element("name", "login-button").click()

'''Tag Locator'''
# driver.get("https://example.com/")
# driver.find_element("tag name", "a").click()            # Click on "Learn more" link
# print(driver.find_element("tag name", "h1").text)       # Read and print "Example Domain" text

'''Print h1 text using Tag Locator'''
# driver.get("https://www.w3schools.com/")
# a1=driver.find_element("tag name", "h1")
# print(a1.text)
# a2=driver.find_elements("tag name", "h1")
# for i in range(0, len(a2)):
#     print(a2[i].text)

'''Print all li tags in python.org'''
# driver.get("https://www.python.org/")
# a=driver.find_elements("tag name","li")
# for i in range(0, len(a)):
#     print(a[i].text)

# Class name and Tag name are least recommended.
# Visible text locators : line text and partial link text
# driver.get("https://www.orangehrm.com/en/book-a-free-demo")

'''Link and Partial Text Locator (Click on 'Privacy Policy' in Facebook)'''
# driver.get("https://www.facebook.com")
# driver.find_element("link text","Privacy Policy").click()       # works on anchor tag elements
# driver.find_element("partial link text","Privacy").click()
# driver.find_element("link text","Forgotten password?").click()  # works on non anchor tag element
# driver.get("https://www.w3schools.com/")
# print(driver.find_element("link text", "Learn to Code").text)     # doesn't work as it is not a link text

''' Search 'samsung' in amazon.in and click on 'Galaxy S26 5G' phone '''
# driver.get("https://www.amazon.in/")
# driver.find_element("id","twotabsearchtextbox").send_keys("samsung")
# driver.find_element("id","nav-search-submit-button").click()
# driver.find_element("partial link text","Galaxy S26 5G").click()

''' CSS Selector (Universal Selector *) '''
# driver.get("https://www.flipkart.com/")
# sleep(3)
# a=driver.find_elements("css selector","*")
# print(len(a))
# for i in a:
#     print(i.text)

''' Try entering username using link text '''
# driver.get("https://www.facebook.com")
# driver.find_element("link text","Email address or mobile number").send_keys("9642673556")
# Note : Unable to enter data in username because there isn't any visible text. Hence,we need CSS Selector.

''' CSS Selector (ID) '''
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element("css selector","#username").send_keys("arbin")
# driver.find_element("css selector","#password").send_keys("taj")

''' CSS Selector (Class) '''
# driver.get("https://www.saucedemo.com/")
# driver.find_elements("css selector",".input_error.form_input")[0].send_keys("standard_user")
# driver.find_elements("css selector",".input_error.form_input")[1].send_keys("secret_sauce")

''' CSS Selector (Tag) '''
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_elements("css selector","input")[0].send_keys("arbin")
# driver.find_elements("css selector","input")[1].send_keys("taj")

''' CSS Selector (Tag Name + Attribute(s) Name) '''
# driver.get("https://facebook.com/")
# sleep(3)
# driver.find_element("css selector","input[name='email']").send_keys("arbin")
# driver.find_element("css selector","input[type='password'][name='pass']").send_keys("taj")      # can add multiple attributes
# driver.find_element("css selector","span[class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft']").click()

''' XPath Locator ''' '''
SYNTAX
XPath (Text) - //tag_name[text()='text']
XPath (Attribute) - //tag_name[@attribute_name='attribute_value']
XPath (contains text) - //tag_name[contains(text(),'partial text')]
XPath (contains attribute) - //tag_name[contains(@attribute_name,'partial attribute_value')] '''

# driver.get("https://www.zomato.com/bangalore/restaurants")
# driver.find_element("xpath","//*[text()='Delivery']").click()

# driver.get("https://demoqa.com/automation-practice-form/")
# driver.find_element("xpath","//button[text()='Submit']").click()                    # text() - Click Submit Button
# driver.find_element("xpath","//input[@maxlength='10']").send_keys("9642673556")     # @attribute - Fill Phone Number

# driver.get("https://www.facebook.com/")
# driver.find_element("xpath","//a[contains(text(),'Coo')]").click()                  # contains text - Click on 'Cookies'
# driver.find_element("xpath","(//a[contains(@role,'li')])[31]").click()              # contains attribute - Click on 'AdChoices'

# sleep(4)
# driver.quit()