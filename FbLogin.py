from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome(executable_path="./chromedriver.exe")

browser.get("https://www.facebook.com")

user_name = browser.find_element_by_id("email")
user_name.send_keys("adsvsv")
 
user_name = browser.find_element_by_id("pass")
user_name.send_keys("01762266")
user_name.send_keys(Keys.ENTER)




sleep(5)

browser.close()