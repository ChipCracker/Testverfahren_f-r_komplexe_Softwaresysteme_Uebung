from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_page_title():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        driver.get('https://www.th-nuernberg.de')
        
        page_title = driver.title
        print(f"The title of the page is: '{page_title}'")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    get_page_title()
