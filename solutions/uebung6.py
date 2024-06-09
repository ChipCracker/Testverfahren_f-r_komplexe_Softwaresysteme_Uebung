from selenium import webdriver
from selenium.webdriver.common.by import By

#Start the Webdriver and get the Webpage
driver = webdriver.Chrome()
driver.get('http://localhost:8000/web/uebung/6.html')
driver.implicitly_wait(1)

try:
    driver.set_window_size(500, 1000) #Set the window size to 500px width
    box_element = driver.find_element(By.ID, 'center-box') #Get the box element
    box_width = box_element.size['width'] #Get the width of the box
    window_width = driver.execute_script("return window.innerWidth") #Get the width of the window
    print(f"Box width at 500px window width: {box_width}px, Window width: {window_width}px")
    if box_width == window_width: #Check if the box width is equal to the window width
        print("Test erfolgreich: Box nimmt bei kleiner Fenstergröße 100% der Breite ein.")
    else:
        print("Test fehlgeschlagen: Box nimmt nicht die erwartete Breite ein.")

    # Repeat for a window width of 800px, this time the box should only take up 75% of the width
    driver.set_window_size(800, 1000)
    box_width = box_element.size['width']
    window_width = driver.execute_script("return window.innerWidth")
    expected_width = 0.75 * window_width
    print(f"Box width at 800px window width: {box_width}px, Expected width: {expected_width}px")
    if abs(box_width - expected_width) <= 1:  # a minimal difference is allowed
        print("Test erfolgreich: Box nimmt bei größerer Fenstergröße 75% der Breite ein.")
    else:
        print("Test fehlgeschlagen: Box nimmt nicht die erwartete Breite ein.")

finally:
    driver.quit()
