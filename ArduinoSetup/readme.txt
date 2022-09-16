### Hardwareanschluss, Pinbelegung.

- Die Pinbelegung ist im Arduino-Sketch aus den Zeilen 13 - 30 zu entnehmen.


### Notwendige Bibliotheken für das Arduino-Sketch installieren:

Es müssen die folgende Bibliotheken installiert werden:

AccelMotor beta 0.0
GyverMotor 2.1

Diese Bibliotheken sind im Ordner Libraries zu finden und müssen einfach nach den Bibliothekenverzeichnis von Arduino IDE kopiert werden. 
Um den Bibliothekenverzeichnis zu ermitteln: 
	1. Arduino IDE öffnen
	2. Reiter "Datei" anklicken
	3. "Voreinstellungen"
	4. Ganz oben wird ein Sketchbook-Speicherort angezeigt. In diesem Ordner soll sich ein weiterer Ordner befinden ("libraries") und da sollen die beiden Bibliotheken eingefügt werden.
		Wenn der Ordner "libraries" nicht existiert, dann soll er neuerstellt werden (mittels Windows Explorer)
	5. Arduino IDE neustarten.


###  Arduino IDE Einstellungen.

1. Zielboard auswählen:
	- Reiter Werkzeuge anklicken
	- Board
	- Arduino AVR Boards
	- "Arduino Duemilanove or Diecimila" auswählen
2. Prozessor auswählen:
	- Reiter Werkzeuge anklicken
	- Prozessor: "ATMega 328P"
3. COM Port auswählen:
	- Arduino Board muss zu diesem Zeitpunkt zum PC angeschlossen werden und Arduino Treiber installiert werden.
	- Reiter Werkzeuge anklicken
	- Port
	- Den richtigen COM Port auswählen, der dem Board vom PC zugewiesen wurde.
Um den richtigen COM Port zu finden (falls es mehrere angeschlossene Geräte gibt):
	- Reiter Werkzeuge -> Port
	- Merken, welche Ports angezeigt werden
	- Arduino Board vom PC trennen
	- Reiter Werkzeuge -> Port
	- Der fehlende Port in der Liste ist der richtige. Arduino Board nochmalls zum PC verbinden und diesen Port auswählen
