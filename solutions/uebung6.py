from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8000/web/uebung/6.html')
driver.implicitly_wait(1)

try:
    driver.set_window_size(500, 1000)
    time.sleep(1)
    box_element = driver.find_element(By.ID, 'center-box')
    box_width = box_element.size['width']
    window_width = driver.execute_script("return window.innerWidth")
    print(f"Box width at 500px window width: {box_width}px, Window width: {window_width}px")
    if box_width == window_width:
        print("Test erfolgreich: Box nimmt bei kleiner Fenstergröße 100% der Breite ein.")
    else:
        print("Test fehlgeschlagen: Box nimmt nicht die erwartete Breite ein.")

    driver.set_window_size(800, 1000)
    time.sleep(1)
    box_width = box_element.size['width']
    window_width = driver.execute_script("return window.innerWidth")
    expected_width = 0.75 * window_width
    print(f"Box width at 800px window width: {box_width}px, Expected width: {expected_width}px")
    if abs(box_width - expected_width) <= 1:  # eine minimale Abweichung ist erlaubt
        print("Test erfolgreich: Box nimmt bei größerer Fenstergröße 75% der Breite ein.")
    else:
        print("Test fehlgeschlagen: Box nimmt nicht die erwartete Breite ein.")

finally:
    driver.quit()
