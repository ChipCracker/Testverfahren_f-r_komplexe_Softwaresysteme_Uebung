from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_all_numbers():
    # Start the WebDriver and open the webpage
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://localhost:8000/web/uebung/3.html')

    try:
        for i in range(100):  # Test numbers from 0 to 99
            # Locate the input field, clear it, input the calculation, and submit
            input_field = driver.find_element(By.ID, "inputString")
            input_field.clear()
            input_field.send_keys(f"{i}+{i}")
            input_field.send_keys(Keys.RETURN)

            # Click the calculate button
            calculate_button = driver.find_element(By.XPATH, "//button[contains(text(),'Berechne')]")
            calculate_button.click()

            # Wait for the response
            driver.implicitly_wait(2)

            # Check the result
            result = driver.find_element(By.ID, "result")
            expected_result = 2 * i
            actual_result = result.text.replace('Das Ergebnis ist: ', '')

            # Assert the expected result matches the actual result
            assert str(expected_result) in actual_result, f"Expected {expected_result}, got {actual_result}"

            print(f"Test successful for: {i} + {i} = {expected_result}")
    finally:
        # Close the browser after testing
        driver.quit()

if __name__ == "__main__":
    test_all_numbers()
