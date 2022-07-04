from selenium import webdriver
import time

# Mac and linux:
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




#1 a+b
driverC = webdriver.Chrome(executable_path="/Users/afik.navaro/Documents/chromedriver")
# driverFF = webdriver.Firefox(executable_path="/Users/afik.navaro/Downloads/geckodriver")
# driverFF.implicitly_wait(10)
driverC.implicitly_wait(10)
# driverC.get("https://www.walla.co.il")
# driverFF.get("http://www.ynet.co.il")

#2
# driverC.get("https://www.google.co.il")
# title = driverC.title
# driverC.refresh()
# title2 = driverC.title
# if title == title2:
#     print(True)
# else:
#     print(False)

## Changed site to google, walla never stopps loading due to advertisment

#3 Checked on FF and Chrome, same locators

#4
# driverC.get("https://translate.google.com/")
# driverC.find_element(by=By.XPATH, value="//textarea[@role='combobox']").send_keys("בדיקת תרגום אוטומטית")

#5
# driverC.get("https://www.youtube.com")
# driverC.find_element(by=By.XPATH, value="//input[@class='ytd-searchbox']").send_keys("RickRolled")
# driverC.find_element(by=By.XPATH, value="//button[@id='search-icon-legacy']").click()

#6
# driverC.get("https://translate.google.com/")
# el1 = driverC.find_element(by=By.XPATH, value="//textarea[@role='combobox']")
# el2 = driverC.find_element(by=By.CLASS_NAME, value="er8xn")
# el3 = driverC.find_element(by=By.XPATH, value="//textarea[@jsname='BJE2fc']")
# print(el1)
# print(el2)
# print(el3)

#7
# driverC.get("https://facebook.com")
# driverC.find_element(by=By.CLASS_NAME, value="inputtext._55r1._6luy").send_keys("***")
# driverC.find_element(by=By.CLASS_NAME, value="inputtext._55r1._6luy._9npi").send_keys("***")
# driverC.find_element(by=By.CLASS_NAME, value="_42ft._4jy0._6lth._4jy6._4jy1.selected._51sy").click()

#8
driver_c2 = webdriver.Chrome(executable_path="/Users/afik.navaro/Documents/chromedriver")
driver_c2.get("chrome://settings/clearBrowserData")
driver_c2.find_element(by=By.XPATH, value="/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[1]/settings-section[5]/settings-privacy-page//settings-clear-browsing-data-dialog//cr-dialog[1]/div[4]/cr-button[2]").click()