from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchDriverException

#Chrome
def checkChrome():
    try:
        print("Testing Chrome...")
        driver = webdriver.Chrome()
        driver.get('http://localhost:8000/web/uebung/5.html')
        browser = driver.find_element(By.ID, 'data-browser').text
        assert browser == 'Chrome'
        driver.quit()
        print("Chrome detected correctly")
    except AssertionError:
        print("Warning: Website did not detect Chrome correctly")

#Firefox
def checkFirefox():
    try:
        print("Testing Firefox...")
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/web/uebung/5.html')
        driver.implicitly_wait(1)
        browser = driver.find_element(By.ID, 'data-browser').text
        assert browser == 'Firefox'
        driver.quit()
        print("Firefox detected correctly")
    except:
        print("Warning: Website did not detect Firefox correctly")

#Edge
def checkEdge():
    try:
        print("Testing Edge...")
        driver = webdriver.Edge()
        driver.get('http://localhost:8000/web/uebung/5.html')
        driver.implicitly_wait(1)
        browser = driver.find_element(By.ID, 'data-browser').text
        assert browser == 'Edge'
        driver.quit()
        print("Edge detected correctly")
    except AssertionError:
        print("Warning: Website did not detect Edge correctly")
    except NoSuchDriverException:
        print("Error: Edge not detected. Probably not a Windows Install")

#IE
def checkIE():
    try:
        print("Testing Internet Explorer...")
        driver = webdriver.Ie()
        driver.get('http://localhost:8000/web/uebung/5.html')
        driver.implicitly_wait(1)
        browser = driver.find_element(By.ID, 'data-browser').text
        assert browser == 'IE'
        driver.quit()
        print("IE detected correctly")
    except AssertionError:
        print("Warning: Website did not detect Internet Explorer correctly")
    except (NoSuchDriverException, OSError):
        print("Error: Internet Explorer not detected. Probably not a Windows Install")
    
def checkSafari():
    try:
        print("Testing Safari...")
        driver = webdriver.Safari()
        driver.get('http://localhost:8000/web/uebung/5.html')
        driver.implicitly_wait(1)
        browser = driver.find_element(By.ID, 'data-browser').text
        assert browser == 'Safari'
        driver.quit()
        print("Safari detected correctly")
    except AssertionError:
        print("Warning: Website did not detect Safari correctly")
    except NoSuchDriverException:
        print("Error: Safari not detected. Probably not a MacOS Install")

checkChrome()
checkFirefox()
checkEdge()
checkIE()
checkSafari()