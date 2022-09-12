
<!-- #region -->
---
# Signalverarbeitung 1


Vorlesungsskript WS 2022 / 2023

Autor: Prof. Dr. Jörg Bitzer  
01.10.2022  
für SV I Version 0.9553  

Jade Hochschule  
Fachbereich Bauwesen Geoinformation Gesundheitstechnologien  
Abteilung Technik und Gesundheit für Menschen   

---


## Zu diesem Dokument 

Dieses Dokument ist ein [Jupyter-Book](https://jupyterbook.org). Viele der Grafiken werden direkt durch den enthaltenen Python Queltext erzeugt. In einigen Fällen wird darauf hingewiesen, dass es sich um interaktive Grafiken handelt. Hier lohnt es sich den Code in ein eigenständiges Skript (`GrafikName.py`) zu kopieren und direkt auszuführen (`python3 GrafikName.py`), um die interaktiven Elemente nutzen zu können. ALternativ können die interaktiven Python-Skripte im Ordner `jupyterbook/code/interactive_programs/` des Repositories (s.u.) direkt verwendet werden.

Um das Buch selbst zu kompilieren, müssen neben den Modulen für das Juyper Book selbst, auch verschiedene Abhängigkeiten des darin enthaltenen Codes selbst vorhanden sein. Diese finden sich in der Datei `meta/requirements.txt` und können mit `pip3 install -r meta/requirements.txt` installiert werden. 

Das Buch selbst lässt sich durch `jupyter-book build jupyterbook` kompilieren. Die erzeugten HTML-Dokumente befinden sich dann im Unterordner `jupyterbook/_build/html`. 

Dieses Buch ist Work-in-progress. Langfristig soll es auch die Inhalte aus den Vorlesungen SV II, Audiotechnik und DAFx beinhalten. In der Zwischenzeit kann jede_r Leser_in mithelfen den Text und die Source-Codes zu verbessern. Es gibt die Möglichkeit oben in der Titelzeile ein *Issue* zu öffnen und die Verbesserung zu beschreiben. Bei manchen Änderungen oder selbst behebbaren Fehlern in Text oder Source Code kann es sinnvoll sein, direkt das Repository zu clonen und ein merge-request zu initiieren.

Das Repository finden Sie hier:

https://github.com/JoergBitzer/Signalverarbeitung_Vorlesungsskript


---

## Nützliche Literatur für die Module SV I und SV II und kurze Beschreibung:
- Girod, B., Rabenstein, R., Stenger, A., *Einführung in die Systemtheorie*,  
  Dieses Buch gibt es in mehreren Ausgaben in der Bibliothek und ist eine anschauliche Einführung in die Systemtheorie. Das Buch geht über den Stoff der Vorlesung hinaus, ist aber sehr anschaulich.
- Kammeyer, K.-D., Kroschel, K., *Digitale Signalverarbeitung*,  
  Eines der Standardwerke in der deutschen SV Literatur. Gut geschrieben, Matlab Beispiele, beinhaltet theoretische Hintergründe zu einigen wichtigen Punkten der Vorlesung
- Proakis, J. G., Manolakis, D., *Digital Signal Processing*,  
  Meine Empfehlung, ein hervorragendes Buch, Sie lernen außerdem gleich die englischen Fachbegriffe
- Orfanidis, S., *Introduction to digital signal processing*, 
  Schönes Einsteigerbuch mit Beispielen aus dem Audiobereich
- Martin Meyer, *Grundlagen der Informationstechnik - Signale, Systeme und Filter*, 1. Auflage, Vieweg-Verlag.
- Vary, P., Heute, U., Hess,W., *Digitale Sprachsignalverarbeitung*,  
  Geht inhaltlich deutlich über die Vorlesung hinaus. Ist für alle interessant, die in diesem Bereich einmal arbeiten wollen.
- Zölzer, U., *Digitale Audiosignalverarbeitung*,  
  Spezialbuch für alle Interessierten.
<!-- #endregion -->
