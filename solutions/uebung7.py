# Windows Size
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8000/web/uebung/7.html')
driver.implicitly_wait(1)
time.sleep(1)

box_element = driver.find_element(By.ID, 'center-box')

driver.set_window_size(600, 800)
# Check Centerbox
box_width = box_element.value_of_css_property('width')
box_padding = box_element.value_of_css_property('padding')
box_width = box_width.replace('px', '')
box_padding = box_padding.replace('px', '')
box_width = float(box_width)
box_padding = float(box_padding)
assert box_width == 600 - box_padding - 1, f"Width is {box_width}, expected {600 - box_padding - 1}"
border_radius = box_element.value_of_css_property('border-radius')
assert border_radius == '0px', f"Border radius is {border_radius}, expected 0px"
print ("Style sheet is correct for 600p")

driver.set_window_size(1920, 1080)
driver.implicitly_wait(1)
#time.sleep(100)
box_width = box_element.value_of_css_property('width')
box_padding = box_element.value_of_css_property('padding')
print (box_width)
print (box_padding)
box_width = box_width.replace('px', '')
box_padding = box_padding.replace('px', '')
box_width = float(box_width)
box_padding = float(box_padding)
assert box_width == 1920 * 0.75 - box_padding - 1, f"Width is {box_width}, expected {1920 * 0.75 - box_padding - 1}"
border_radius = box_element.value_of_css_property('border-radius')
assert border_radius == '8px', f"Border radius is {border_radius}, expected 0px"
print ("Stylesheet is correct for 1920p")