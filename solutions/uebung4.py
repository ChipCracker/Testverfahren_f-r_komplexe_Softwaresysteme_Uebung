from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_scroll_to_10000_and_click():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:8000/web/uebung/4.html')
    driver.maximize_window()

    def scroll_to_element_with_text(target_text):
        scroll_attempt = 0
        while True:
            driver.execute_script("window.scrollBy(0, 800);")
            time.sleep(0.01)
            scroll_attempt += 1

            try:
                
                element = driver.find_element(By.XPATH, f"//*[contains(text(), 'Element {target_text}')]")
                if element:
                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    print(f"Element with text 'Element {target_text}' found and scrolled into view.")
                    
                    element.click()
                    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
                    alert_text = alert.text
                    print(f"Alert text: '{alert_text}'")
                    alert.accept()
                    break
                    
            except Exception as e:
                reached_bottom = driver.execute_script("return window.innerHeight + window.scrollY >= document.body.offsetHeight;")
                if reached_bottom:
                    print("Reached the bottom or no more content to load.")
                    break

            if scroll_attempt > 5000: 
                print("Reached scroll attempt limit.")
                break

    scroll_to_element_with_text(10000)
    driver.quit()

if __name__ == "__main__":
    test_scroll_to_10000_and_click()
