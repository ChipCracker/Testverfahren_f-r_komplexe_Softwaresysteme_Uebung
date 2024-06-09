from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchDriverException

def checkBrowser(driver: webdriver, browser: str):
    try:
        driver.get('http://localhost:8000/web/uebung/5.html') #Get the website
        driver.implicitly_wait(1)
        browserData = driver.find_element(By.ID, 'data-browser').text #Get text element
        assert browserData == browser #Compare Browser Strings
        driver.quit() #Stop the driver
        print(f"{browser} detected correctly")
    except AssertionError: #Browser not detected correctly
        print(f"Warning: Website did not detect {browser} correctly")
        driver.quit()

def checkChrome():
    # Create WebDriver
    driver = webdriver.Chrome()
    checkBrowser(driver, 'Chrome')
       

def checkFirefox():
    driver = webdriver.Firefox()
    checkBrowser(driver, 'Firefox')

def checkEdge():
    try:
        driver = webdriver.Edge()
        checkBrowser(driver, 'Edge')
    except OSError: #Browser not detected
        print(f"Error: Unable to test Edge. Probably not a Windows Machine")
    
def checkSafari():
    try:
        driver = webdriver.Safari()
        checkBrowser(driver, 'Safari')
    except NoSuchDriverException: #Browser not detected
        print(f"Error: Unable to test Safari. Probably not a Mac")
    

checkChrome()
checkFirefox()
checkEdge()
checkSafari()
