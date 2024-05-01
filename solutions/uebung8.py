from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8000/web/uebung/8.html')

driver.implicitly_wait(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(by=By.ID, value="menu1"))
action.pause(1)
action.move_to_element(driver.find_element(by=By.XPATH, value="//a"))
action.pause(1)
action.click()
action.perform()

time.sleep(2)