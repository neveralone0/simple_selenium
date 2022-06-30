from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('https://www.google.com/')
browser.find_element(By.CLASS_NAME,'gLFyf').send_keys('python'+ Keys.RETURN)
browser.find_element(By.PARTIAL_LINK_TEXT, "Videos").click()

time.sleep(60)