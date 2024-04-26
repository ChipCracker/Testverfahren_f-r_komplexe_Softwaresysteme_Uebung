# Selenium Mini Documentation

Required Dependencies:  
>selenium==4.19.0  
>webdriver-manager==4.0.1


# Python
`import time` Importiert die Time library, die für die sleep Methode gebraucht wird  
`time.sleep(float seconds)` Die Ausführung des Programms wird für die angegebene Zeit pausiert

# Selenium

## Imports:
``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
```

`webdriver`  Selenium WebDriver.\  
`By` Selenium Locator Klasse, die genutzt wird um Elemente auf der Webseite zu finden.\  
`Keys` Selenium Klasse, die genutzt wird um Tastenanschläge zu senden\
`Service` Klasse zur Steuerung des Browser-Dienstes. \
`WebDriverWait` Zum Warten auf das Vorhandensein bestimmter Bedingungen. \
`expected_conditions` Vordefinierte Bedingungen zur Nutzung mit WebDriverWait.\
`ChromeDriverManager` Automatische Verwaltung von Chromedriver.\


## WebDriver Service Management

`Service(ChromeDriverManager().install())` Installiert und initiiert den Chromedriver-Dienst, der für die Ausführung von Chrome Browser erforderlich ist.

```python
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

## WebDriver

### WebDriver starten
`webdriver.Chrome()` `webdriver.Firefox()` `webdriver.Edge()` `webdriver.Safari()` Erstellen ein WebDriver Objekt mit dem ausgewähltem Browser und öffnet diesen.

```python
driver = webdriver.Chrome()
webdriver.Firefox()
webdriver.Edge()
webdriver.Safari()
```

### WebDriver schließen
`driver.quit()` Schließt den Browser und beendet den Webdriver-Dienst.
```python
driver.quit()
```

### Website/URL ansteuern
`webdriver.get(string url)` Öffnet im Browser die gegebene URL.
```python
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
```

### Warten
`webdriver.implicitly_wait(float seconds)` Lässt den Webdriver die angegebene Zeit warten (sinnvoll um die Webseite laden zu lassen).
```python
driver.implicitly_wait(1) #Makes the WebDriver wait for 1s before continuing
```

### Element suchen
`webdriver.find_element(By.Locator, string value)` Der WebDriver sucht auf der aktuellen Seite nach einem Element, dessen Daten mit dem Locator übereinstimmt. Wenn mehrere Elemente mit der Bedingung übereinstimmen, wird das erste ausgewählt.
```python
text_box = webdriver.find_element(by=By.Name, value="my-text") #Select the element with the Name "my-text"
submit_button = webdriver.find_element(by=By.CSS_Selector, value="button") #Selects the first button element
```

### Atribute auslesen

`element.get_attribute('style')` Der Webdriver liest den Wert des spezfizierten Elements aus.

```python
links = self.driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.get_attribute('href'))
```

### Eingabe von Text
`element.send_keys(string keys)` `element.send_keys(Keys Key)` Sendet die gegebenen Tastenschläge an das ausgewählte Element.
```python
text_box.send_keys("Hello Selenium!")
text_box.send_keys(Keys.ARROW_LEFT)
```

### Maus Klicken
`button.click()` Klickt das ausgewählte Element.
```python
submit_button.click()
```

### JavaScript ausführen
`driver.execute_script(script, *args)` Führt JavaScript im Kontext der derzeit geladenen Seite aus.
``` python
driver.execute_script("console.log("Hello Selenium!");")
```

### Bedingtes warten
`WebDriverWait(driver, timeout).until(condition)` Wartet bis eine bestimmte Bedingung erfüllt ist.

``` python
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
``` 


## Arbeit mit Browser-Tabs

### Tab öffnen
Um einen neuen Tab in einem Browser mit Selenium zu öffnen, kann man JavaScript verwenden, das über die `execute_script()` Methode des WebDriver ausgeführt wird.

``` python
driver.execute_script("window.open('');")
```

Nach dem Öffnen eines neuen Tabs können man nun zwischen den Tabs wechseln. Folgender Code öffnet den neuesten:
``` python
driver.switch_to.window(driver.window_handles[-1])
```

### Tab schließen
`driver.close()` Schließt den aktuellen Tab.
``` python
driver.close()
```