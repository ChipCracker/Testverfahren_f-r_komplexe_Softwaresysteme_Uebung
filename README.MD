### Test 1: Webseite der Technischen Hochschule Nürnberg

#### Beschreibung
Der erste Test soll die Funktionalität des Zugriffs auf die Webseite der Technischen Hochschule Nürnberg überprüfen. Das Ziel dieses Tests ist es, sicherzustellen, dass die Webseite erreichbar ist und der Seitentitel korrekt geladen wird.

#### Testaufgabe
__URL__: https://www.th-nuernberg.de \
__Ziel__: Automatisieren Sie den Prozess, um die Webseite in einem Browser zu öffnen und den Seitentitel auszugeben. \
__Erwartetes Ergebnis__: Der Test soll den Titel der Webseite in der Konsole ausgeben, um zu bestätigen, dass die richtige Seite geladen wurde. 
#### Schritte
1. Initialisieren Sie den WebDriver.
2. Öffnen Sie die URL der TH Nürnberg.
3. Extrahieren Sie den Titel der geladenen Webseite.
4. Geben Sie den Titel in der Konsole aus.
5. Schließen Sie den Browser.

<hr>

### Test 2: Navigation zur offiziellen Selenium-Webseite
#### Beschreibung

Der zweite Test zielt darauf ab, die offizielle Webseite von Selenium WebDriver durch eine Google-Suche zu finden und darauf zuzugreifen. Dieser Test überprüft die Funktionalität der Suchfunktion und die korrekte Weiterleitung auf externe Seiten über Suchergebnisse.

#### Testaufgabe

__URL__: https://www.google.de \
__Ziel__: Automatisieren Sie den Prozess, um "google.de" zu öffnen, nach "Selenium WebDriver" zu suchen, auf den Link zur offiziellen Dokumentationsseite zu klicken und den Titel der Seite sowie die URL zu überprüfen. \ 
__Erwartetes Ergebnis__: Der Test soll den Titel und die URL der Selenium-Dokumentationsseite ausgeben, um zu bestätigen, dass die korrekte Seite geladen wurde.

#### Schritte

1. Initialisieren Sie den WebDriver.
2. Öffnen Sie die URL von Google.
3. Geben Sie "Selenium WebDriver" in das Suchfeld ein und senden Sie die Suchanfrage.
4. Klicken Sie auf den Link, der zur offiziellen Selenium-Webseite führt.
5. Überprüfen Sie den Titel der Seite und die URL, um sicherzustellen, dass Sie auf die 6.6. 6. korrekte Seite weitergeleitet wurden.
7. Geben Sie den Titel und die URL in der Konsole aus.
8. Schließen Sie den Browser.

<hr>

### Test 3: Taschenrechner-Funktionalität

#### Beschreibung
Der dritte Test, test3, konzentriert sich auf die Überprüfung der Funktionalität eines Web-basierten Taschenrechners. Der Test soll automatisch eine Serie von Berechnungen durchführen und prüfen, ob die Ergebnisse wie erwartet zurückgegeben werden.

#### Testaufgabe
__URL__: http://localhost:8000/web/uebung/3.html \
__Ziel__: Automatisieren Sie den Prozess, verschiedene arithmetische Operationen durch den Taschenrechner ausführen zu lassen, und überprüfen Sie, ob die angezeigten Ergebnisse korrekt sind.
__Erwartetes Ergebnis__: Alle Testfälle sollten bestätigen, dass der Taschenrechner die erwarteten Ergebnisse liefert.
#### Schritte
1. Initialisieren Sie den WebDriver.
2. Öffnen Sie die URL des Taschenrechners.
3. Führen Sie eine Liste vordefinierter Berechnungen durch (z.B. Addition, Subtraktion, Multiplikation, Division).
4. Überprüfen Sie für jede Berechnung, ob das Ergebnis im Webinterface des Taschenrechners 5. mit dem erwarteten Ergebnis übereinstimmt.
6. Geben Sie das Ergebnis jeder Überprüfung in der Konsole aus.
7. Schließen Sie den Browser.