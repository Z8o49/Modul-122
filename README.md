# Modul-122
Für ein kompaktes Demonstrationsprojekt wurde ein Python-Programm entwickelt, das beispielhafte Google-Suchergebnisse in einer SQLite-Datenbank speichert. Beim Start der Anwendung wird automatisch eine Datenbankdatei mit dem Namen search_results.db erstellt. Innerhalb dieser Datei wird eine Tabelle namens results angelegt, in der die simulierten Suchergebnisse abgelegt werden.

Zum Auslesen der gespeicherten Daten steht ein separates Skript zur Verfügung, das die Einträge aus der Datenbank abruft und übersichtlich im Terminal darstellt. Ziel des Projekts ist es, den grundlegenden Umgang mit Datenbankoperationen in Python zu demonstrieren – insbesondere das Einfügen und spätere Abfragen strukturierter Daten.

Anstelle echter Suchmaschinendaten – deren Nutzung aus technischen und rechtlichen Gründen komplex ist – kommen fiktive Suchergebnisse zum Einsatz, um die Funktionsweise möglichst nachvollziehbar darzustellen.

Die Anwendung setzt lediglich eine funktionierende Python-Umgebung mit SQLite-Unterstützung voraus. Nach dem Ausführen des Hauptskripts (google_scraper.py) wird die Datenbank automatisch angelegt und mit Beispielinhalten befüllt. Das zweite Skript (read_db.py) ermöglicht anschließend die Darstellung der gespeicherten Einträge.
