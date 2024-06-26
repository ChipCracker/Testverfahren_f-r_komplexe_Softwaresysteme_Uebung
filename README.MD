## Prerequisites
## Install dependencies
1. `python3 -m venv .venv`
2. activate the virtual environment\
macOS: `source ./.venv/bin/activate`\
Windows: `.venv/bin/activate` 
3. `pip install -r requirements.txt`

### Http-Server
For starting the python http server, execute the `serve.bat`file or the `serve.sh`file.


### Test 1: Webseite der Technischen Hochschule Nürnberg

#### Beschreibung
Der erste Test soll die Funktionalität des Zugriffs auf die Webseite der Technischen Hochschule Nürnberg überprüfen. Das Ziel dieses Tests ist es, sicherzustellen, dass die Webseite erreichbar ist und der Seitentitel korrekt geladen wird.

#### Testaufgabe
__URL__: https://www.th-nuernberg.de \
__Ziel__: Automatisieren Sie den Prozess, um die Webseite in einem Browser zu öffnen und den Seitentitel auszugeben. \
__Erwartetes Ergebnis__: Der Test soll den Titel der Webseite in der Konsole ausgeben, um zu bestätigen, dass die richtige Seite geladen wurde. 


<hr>

### Test 2: Navigation zur offiziellen Selenium-Webseite
#### Beschreibung

Der zweite Test zielt darauf ab, die offizielle Webseite von Selenium WebDriver durch eine Google-Suche zu finden und darauf zuzugreifen. Dieser Test überprüft die Funktionalität der Suchfunktion und die korrekte Weiterleitung auf externe Seiten über Suchergebnisse.

#### Testaufgabe

__URL__: https://www.google.de \
__Ziel__: Automatisieren Sie den Prozess, um "google.de" zu öffnen, nach "Selenium WebDriver" zu suchen, auf den Link zur offiziellen Dokumentationsseite zu klicken und den Titel der Seite sowie die URL zu überprüfen. \ 
__Erwartetes Ergebnis__: Der Test soll den Titel und die URL der Selenium-Dokumentationsseite ausgeben, um zu bestätigen, dass die korrekte Seite geladen wurde.

#### Bemerkung
Cookie-Banner sind manchmal nervig xD

<hr>

### Test 3: Taschenrechner-Funktionalität

#### Beschreibung
Der dritte Test, test3, konzentriert sich auf die Überprüfung der Funktionalität eines Web-basierten Taschenrechners. Der Test soll automatisch eine Serie von Berechnungen durchführen und prüfen, ob die Ergebnisse wie erwartet zurückgegeben werden.

#### Testaufgabe
__URL__: http://localhost:8000/web/uebung/3.html \
__Ziel__: Automatisieren Sie den Prozess, verschiedene arithmetische Operationen durch den Taschenrechner ausführen zu lassen, und überprüfen Sie, ob die angezeigten Ergebnisse korrekt sind. Eventuell hat sich ein Fehler eingeschlichen, bei dem eine bestimmte Zahl als Eingabe als Fehler gewertet wird. \
__Erwartetes Ergebnis__: Alle Testfälle sollten bestätigen, dass der Taschenrechner die erwarteten Ergebnisse liefert.

<hr>

### Test 4: Endlose Scroll-Demo

#### Beschreibung
Der vierte Test zielt darauf ab, die Funktionalität des unendlichen Scrollens auf einer Webseite zu überprüfen. Es wird getestet, ob die Webseite dynamisch weitere Inhalte lädt, wenn der Benutzer nach unten scrollt. Zusätzlich enthält das 10.000. Element ein verstecktes Alert, das beim Klicken eine geheime Nachricht ("Flag") enthüllt.

#### Testaufgabe
__URL__: http://localhost:8000/web/uebung/4.html \
__Ziel__: Automatisieren Sie den Prozess, um die Webseite zu öffnen, nach unten zu scrollen und das 10.000. Element zu klicken, um den Alert zu aktivieren und die darin enthaltene Nachricht anzuzeigen. \
__Erwartetes Ergebnis__: Der Test soll die Nachricht innerhalb des Alerts verifizieren, um zu bestätigen, dass die richtige Nachricht angezeigt wird.

#### Schritte
1. Initialisieren Sie den WebDriver.
2. Öffnen Sie die URL der Demo-Seite.
3. Scrollen Sie automatisch bis das 10.000. Element erscheint.
4. Klicken Sie auf das 10.000. Element, um das Alert zu öffnen.
5. Überprüfen Sie die Nachricht im Alert.
6. Geben Sie die Nachricht des Alerts in der Konsole aus.
7. Schließen Sie den Browser.

<hr>

### Test 5: Browser Erkennung

#### Beschreibung
Dieser Test demonstriert die Fähigkeit von Seleniums verschiedene Browser testen zu können.

#### Testaufgabe
__URL__: http://localhost:8000/web/uebung/5.html  
__Ziel__: Automatisieren Sie den Prozess die Webseite mit verschiedenen Browser zu testen.  
__Erwartetes Ergebnis__: Die Webseite sollte immer den Namen des verwendeten Browsers angeben.

#### Schritte
Pro Browser der getestet werden soll:
1. Initialisieren Sie den WebDriver.
2. Öffnen Sie die angegebene URL.
3. Überprüfen Sie ob die Webseite den aktuellen Browser richtig erkannt hat.
4. Geben Sie in der Konsole aus, ob die Webseite funktioniert oder ob es ein Problem gibt. 

### Test 6: CSS Überprüfung

#### Beschreibung
Dieser Test dient der Überprüfung, ob die verknüpfte Stylesheet auf dieser Webseite korrekt funktioniert und ob das Layout bei verschiedenen Fenstergrößen richtig angepasst wird. 

#### Testaufgabe
__URL__: http://localhost:8000/web/uebung/6.html  
__Ziel__: Lassen Sie Selenium automatisch die Fenstergröße des Browsers anpassen und überprüfen Sie, ob das Styling korrekt ist. \
__Erwartetes Ergebnis__: Die Div auf der Webseite sollte automatisch bei einer kleinen Windowgröße anfangen die gesamte Breite des Fensters einzunehmen.

#### Schritte
1. Initialisieren Sie den WebDriver und öffnen Sie die URL.
2. Setzen Sie die Fenstergröße unter 700p.
3. Überprüfen Sie ob das Div "border-box" 100% der Fensterbreite einnimmt und das css property "border-radius" auf 0 gesetzt wird. 
4. Setzen Sie die Fenstergröße über 700p und überprüfen Sie ob die Breite 75% der Fensterbreite einnimmt.

### Test 7: Selenium Action Chain Demo

#### Beschreibung
Dieser Test überprüft, ob die Dropdown Menüs richtig beim Maus Hovern angezeigt werden und ob die damit verbundenen Knöpfe funktionieren.

#### Testaufgabe

__URL__: http://localhost:8000/web/uebung/7.html  
__Ziel__: Lassen Sie Selenium automatisch das Dropdown Menü und dessen Elemente testen.
__Erwartetes Ergebnis__: Der Browser sollte zurück auf die /web/home Seite navigieren.

### Bonusaufgabe: Implementierung eines Webcrawlers mit Selenium
#### Beschreibung
In dieser Aufgabe soll ein einfacher Webcrawler implementiert werden, welcher eine Start-URL besucht und rekursiv alle Links auf dieser Webseite sammelt und aufruft und die URLs nach beenden des Crawls hierarchisch in der Konsole ausgiebt. Dies testet nicht nur die Funktionalität von Link-Erkennungen, sondern auch die Handhabung von dynamisch geladenen Webseiten.

#### Testaufgabe
__Start-URL__: (bitte eigene wählen) \
__Ziel__: Automatisieren Sie den Prozess, um mit Selenium Webseiten zu durchsuchen, alle gefundenen Links zu erfassen und diese anschließend zu besuchen.\
__Erwartetes Ergebnis__: Der Crawler sollte alle auf der Basis-URL verfügbaren Links erfassen und besuchen, wobei er auch Seitenverweise und eingebettete Links erfassen sollte.

#### Schritte
1. Initialisieren Sie den WebDriver.
2. Öffnen Sie die Start-URL.
3. Sammeln Sie alle Links auf der aktuellen Seite.
4. Besuchen Sie jeden Link und wiederholen Sie Schritt 3 und 4 für neue Seiten, bis ein Abbruchkriterium erreicht ist (z.B. maximale Tiefe oder Anzahl der besuchten Seiten).
5. Überprüfen Sie, ob die gesammelten Links erreichbar sind und loggen Sie etwaige Fehler oder Probleme.
6. Geben Sie Informationen über die Anzahl der gesammelten und besuchten Links sowie eventuelle Fehler in der Konsole aus.
7. Schließen Sie den Browser.