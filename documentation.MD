# Selenium Mini Documentation

Required Dependencies:  
>selenium==4.19.0  
>webdriver-manager==4.0.1


# Python
`import time` Importiert die Time library die für die sleep Methode gebraucht wird  
`time.sleep(float seconds)` Die Ausführung des Programms wird für die angegebene Zeit pausiert

# Selenium

## Imports:
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
```

`webdriver`  Selenium's WebDriver Tool  
`By` Selenium's Locator Klasse die genutzt wird um Elenement in der Webseite zu finden  
`Keys` Selenium's Klasse die genutzt wird um Tastenschläge zu senden

## Webdriver

`webdriver.Chrome()` `webdriver.Firefox()` `webdriver.Edge()` `webdriver.Safari()` Erstellen ein WebDriver Objekt mit dem ausgewähltem Browser und öffnen diesen  

```python
driver = webdriver.Chrome() #Creates and opens the Chrome WebDriver
```
`webdriver.get(string url)` Öffnet  im webdriver die gegebene URL  
```python
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
```
`webdriver.implicitly_wait(float seconds)` Lässt den Webdriver die angegebene Zeit warten (sinnvoll um die Webseite laden zu lassen)  
```python
driver.implicitly_wait(1) #Makes the WebDriver wait for 1s before continuing
```
`webdriver.find_element(By.Locator, string value)` Der WebDriver sucht in der aktuellen Seite nach einem Element dessen Daten mit dem Locator übereinstimmt. Wenn mehrere Elemente mit der Bedingung übereinstimmen, wird das erste ausgewählt
```python
text_box = webdriver.find_element(by=By.Name, value="my-text") #Select the element with the Name "my-text"
submit_button = webdriver.find_element(by=By.CSS_Selector, value="button") #Selects the first button element
```
`element.send_keys(string keys)` `element.send_keys(Keys Key)` Sendet die gegebenen Tastenschläge an das ausgewählte Element
```python
text_box.send_keys("Hello Seleniu")
text_box.send_keys(Keys.ARROW_LEFT)
```
`button.click()` Clickt auf das ausgewählten Element
```python
submit_button.click()
```