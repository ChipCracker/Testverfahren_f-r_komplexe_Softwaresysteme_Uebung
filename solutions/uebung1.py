from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get('https://www.th-nuernberg.de')
    
    page_title = driver.title
    print(f"The title of the page is: '{page_title}'")

finally:
    driver.quit()
