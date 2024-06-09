from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#Start the WebDriver and open the website
driver = webdriver.Chrome()
driver.get('http://localhost:8000/web/uebung/7.html')
driver.implicitly_wait(1)

action = ActionChains(driver) #Create the ActionChain
action.move_to_element(driver.find_element(by=By.ID, value="menu1")) #Move mouse to dropdown menu
action.pause(1)
action.move_to_element(driver.find_element(by=By.XPATH, value="//a")) # Move mouse to dropdown menu item
action.pause(1)
action.click() #Click on dropdown menu item
action.perform() #Perform the actions

#Check if the URL has changed to include the # at the end
if (driver.current_url == "http://localhost:8000/web/uebung/7.html#"):
    print("Dropwdown Menu works as expected")
else: print("Dropwdown Menu does not work as expected")