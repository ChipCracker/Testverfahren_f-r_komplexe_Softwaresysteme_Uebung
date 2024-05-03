from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def search_selenium_official_website():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        driver.get('https://www.google.de')

        driver.implicitly_wait(10) 
        try:
            # Cookies ablehnen
            accept_button = driver.find_element(By.XPATH, '//*[@id="W0wltc"]')
            accept_button.click()
        except Exception as e:
            print("No privacy button found, continuing...")

        # Google Suchfeld ansteuern und Suchbegriff eingeben
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)

        # auf die Ergebnisseite warten
        driver.implicitly_wait(10)  

        # Klicke auf den Link zur offiziellen Selenium Webseite
        link = driver.find_element(By.XPATH,  "//a[h3[contains(text(),'WebDriver')]]")
        link.click()

        print(f"The title of the page is: '{driver.title}'")

         # Überprüfe, ob die URL korrekt ist
        expected_url = "https://www.selenium.dev/documentation/webdriver/"
        current_url = driver.current_url
        assert current_url == expected_url, f"URL mismatch: expected {expected_url}, got {current_url}"
        print(f"URL is correct: {current_url}")

    finally:
        driver.quit()

if __name__ == "__main__":
    search_selenium_official_website()
