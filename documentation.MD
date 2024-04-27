# Selenium Mini Documentation

Required Dependencies:

> selenium==4.19.0  
> webdriver-manager==4.0.1

# Python

`import time` Importiert die Time library, die für die sleep Methode gebraucht wird  
`time.sleep(float seconds)` Die Ausführung des Programms wird für die angegebene Zeit pausiert  
`assert Condition` Kann genutzt werden um zu überprüfen ob Daten der Webseite ihren Soll Werten entsprechen

# Selenium

## Imports:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
```

`webdriver` Selenium WebDriver  
`By` Selenium Locator Klasse, die genutzt, wird um Elemente auf der Webseite zu finden  
`Keys` Selenium Klasse, die genutzt wird um Tastenanschläge zu senden\
`ActionChains` Selenium Klasse die zur Durchführung komplexerer Aktionen genutzt wird\
`Service` Klasse zur Steuerung des Browser-Dienstes  
`WebDriverWait` Zum Warten auf das Vorhandensein bestimmter Bedingungen  
`expected_conditions` Vordefinierte Bedingungen zur Nutzung mit WebDriverWait  
`ChromeDriverManager` Automatische Verwaltung von Chromedriver

## WebDriver Service Management

`Service(ChromeDriverManager().install())` Installiert und initiiert den Chromedriver-Dienst, der für die Ausführung von Chrome Browser erforderlich ist.

```
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

## WebDriver

### WebDriver starten

`webdriver.Chrome()` `webdriver.Firefox()` `webdriver.Edge()` `webdriver.Safari()` Erstellen ein WebDriver-Objekt mit dem ausgewählten Browser und öffnen diesen.

```python
driver = webdriver.Chrome()
webdriver.Firefox()
webdriver.Edge()
webdriver.Safari()
```

### WebDriver schließen

`driver.quit()` Schließt den Browser und beendet den WebDriver-Dienst.

```python
driver.quit()
```

### Website/URL ansteuern

`webdriver.get(string url)` Diese Methode öffnet im Browser die gegebene URL.

```python
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
```

### Warten

`webdriver.implicitly_wait(float seconds)` Lässt den WebDriver die angegebene Zeit warten (sinnvoll um die Webseite laden zu lassen).

```python
driver.implicitly_wait(1) #Makes the WebDriver wait for 1s before continuing
```

### Element suchen

`webdriver.find_element(By.Locator, string value)` Der WebDriver sucht auf der aktuellen Seite nach einem Element, dessen Daten mit dem Locator übereinstimmen. Wenn mehrere Elemente mit der Bedingung übereinstimmen, wird das erste ausgewählt.

```python
text_box = webdriver.find_element(by=By.Name, value="my-text") #Select the element with the Name "my-text"
submit_button = webdriver.find_element(by=By.CSS_Selector, value="button") #Selects the first button element
```

### Attribute auslesen

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

### Überprüfen von CSS Eigenschaften

`WebElement.value_of_css_property(string property)` Holt das gewünschte CSS Property des ausgewählten Elements

```python
button_color = submit_button.value_of_css_property('background-color')
```

### Maus Klicken

`button.click()` Klickt das ausgewählte Element.

```python
submit_button.click()
```

### JavaScript ausführen

`driver.execute_script(script, *args)` Führt JavaScript im Kontext der derzeit geladenen Seite aus.

```python
driver.execute_script("console.log("Hello Selenium!");")
```

### Bedingtes warten

`WebDriverWait(driver, timeout).until(condition)` Wartet bis eine bestimmte Bedingung erfüllt ist.

```python
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
```

## Arbeiten mit Actions

Manchmal müssen komplizierte Aktionen auf Webseiten ausgeführt werden. Hierzu gibt es die ActionChains Klasse welche komplexere, low-level Benutzereingaben durchführen kann.

### ActionChain erstellen

`ActionChains(WebDriver driver)` Erstellt eine Action Chains Klasse zu der eine Reihe Aktionen hinzugefügt werden kann

```python
action = ActionChains(driver)
```

### Maus zu Element bewegen

`ActionChains.move_to_element(WebElement element)` Bewegt einen emulierten Mauszeiger zu dem gegebenen Punkt. Der Mauszeiger bleibt nach der Bewegung an dieser Stelle, ideal um Mouse Over Skripte zu testen. (Wird erst bei action.perform() durchgeführt)

```python
action.move_to_element(submit_button)
```

### Durchführung Aktionen pausieren

`ActionChains.pause(int seconds)` Pausiert wartet bis zur Durchführung der nächsten Aktion die angegebene Zeit (Wird erst bei action.perform() durchgeführt)

```python
action.pause(1)
```

### Aktionen durchführen

`ActionChains.perform()` Führt alle Aktionen durch in der Reihenfolge die sie der ActionChains Klasse hinzugefügt wurden. Alle oben angebene Befehle können auch zu einer Methodenzeile zusammengefasst werden.

```python
action.perform() # Mit den oben angebenen Befehlen würde der WebDriver den virtuellen Mauszeiger zum submit_button bewegen und dann eine Sekunde warten
action = ActionChains(driver).move_to_element(submit_button).pause(1).perform() #Das geht auch in einer Zeile
```

## Arbeit mit Browser-Tabs

### Tab öffnen

Um einen neuen Tab in einem Browser mit Selenium zu öffnen, kann man JavaScript verwenden, das über die `execute_script()` Methode des WebDriver ausgeführt wird.

```python
driver.execute_script("window.open('');")
```

Nach dem Öffnen eines neuen Tabs können man nun zwischen den Tabs wechseln. Folgender Code öffnet den neuesten:

```python
driver.switch_to.window(driver.window_handles[-1])
```

### Tab schließen

`driver.close()` Schließt den aktuellen Tab.

```python
driver.close()
```

## Arbeit mit Browser-Fenster

### Window Größe holen

`driver.get_window_size()` Holt die aktuelle Browser Fenster Größe im Format `{'width': xGröße, 'height': yGröße}`

```python
driver.get_window_size()
```

### Window Größe setzen

`driver.set_window_size(int x, int y)` Setzt aktuele Browser Fenster Größe auf x\*y Pixel

```python
driver.set_window_size(800, 600)
```
