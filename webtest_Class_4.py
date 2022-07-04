from selenium import webdriver
import time

# Mac and linux:
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/afik.navaro/Downloads/chromedriver")  # will open Chrome browser using the driver
driver.implicitly_wait(10)
driver.get("https://translate.google.com")   # the driver will get the url after the get
# print(driver.current_url) # Will print the current URL we are working on
# print(driver.title) # Will print the driver title
# print(driver.page_source) # Will print the HTML of the page we are working on
# driver.close() # Will close the current tab
# driver.quit() # Will close the browser with all tabs
# driver.find_element_by_class_name("VfPpkd-Jh9lGc") # Locator to find element by a locator + locator value, which in this case is class
# driver.find_element(by=By.CLASS_NAME, value="er8xn") # finding elements by the class name
# driver.find_element_by_class_name("er8xn") # Old way to do so
# driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div")
# print(driver.find_element(by=By.XPATH, value="//div"))
# driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div") # Full Xpath

my_list = driver.find_elements(by=By.TAG_NAME, value="div") #Finding all elements "div" and list them in my_list (tag name is the first word after <)
print(len(my_list)) # printing the amount of values in the list (how many "div"s)

driver.find_element(by=By.CLASS_NAME, value="er8xn").send_keys("Hello") # sending Hello to text area, we can also use .clear() to clear it

# time.sleep(5) # sets a delay for running the commands ( to avoid no synchronization, for exmaple if the page takes time to load, probably more than the code )
# this is mostly used for practice and testing

# driver.implicitly_wait(10) # Will wait up to 10 seconds on each find_element or find_elements to avoid no sync and avoids waiting, will apply to all below and can be override

# driver.find_element(by=By.CLASS_NAME, value='VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-INsAgc.VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc.Rj2Mlf.OLiIxf.PDpWxe.qfvgSe.aiUxpf').click() # Clicking on Websites

driver.find_element(by=By.XPATH, value="//button[@jscontroller='soHxf']").click()
