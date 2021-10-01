---
# Signalverarbeitung 1


Vorlesungsskript WS 2021 / 2022


©Autor: Prof. Dr. Jörg Bitzer  
01.01.2021  
für SV I Version 0.9552  

Jade Hochschule  
Fachbereich Bauwesen und Geoinformation  
Abteilung Technik und Gesundheit für Menschen 

---

<!-- #region -->
## Zu diesem Jupyter-Buch

Dieses Jupyter-Book enthält für viele Grafiken auch den Python Source-Code. In einigen Fällen wird darauf hingewiesen, dass es sich um interaktive Grafiken handelt. Hier lohnt es sich den Code in ein eigenständiges Skript (GrafikName.py) zu kopieren und direkt auszuführen (python3 GrafikName.py), um die interaktiven Elemente nutzen zu können.


## Fehler bzw. Änderungs-Log:
- Version 0.9542 vom 29.10.2017: Fehler berichtigt Abschnitt Rekursion N ersetzt durch M und N-1 in Formel durch M
- Version 0.9543 vom 12.11.2017: zTrafo: nicht-kausale Folge richtig definiert: ACHTUNG: In der Bildüberschrift noch nicht geändert
- Version 0.9544 vom 20.11.2017: Beim Stabilitätsdreieck die Bedingung auf $a_2^2 <1$ geändert (Quadrat ergänzt).
- Version 0.9545 vom 26.11.2017: Begin Spektren (5.1-5.3) $\Omega$ durch $\Omega_0$ ersetzt, da eine spezifische Frequenz gemeint ist .
- Version 0.9546 vom 14.12.2017: Fensterfunktionen mit $4\pi$ statt $2\pi$.
- Version 0.9547 vom 13.11.2018: Erzeugung Dreieck cos auf sin geändert. Lösung war fehlerhaft.
- Version 0.9548 vom 13.11.2018: Abb 2.22 Werte zu Definitionsbereich geändert und Bsp Linearität klarer dargestellt. Es fehlt noch im oberen Teil des Bildes das xmix.
- Version 0.955 vom 07.12.2018: Phasenberechnung aus PN geändert.
- Version 0.9551 vom 05.09.2019: Girod, Rabenstein als Ideengeber bei Pol-Nullstellendarstellung 
- Version 0.9551 vom 05.09.2019: Fibonacci Beispiel entfernt und Stil geändert in zTrafo Anfang

---

## Nützliche Literatur für die Module SV I und SV II und kurze Beschreibung:
- Girod, Rabenstein, Stenger, *Einführung in die Systemtheorie*,  
  Dieses Buch gibt es in mehreren Ausgaben in der Bibliothek und ist eine anschauliche Einführung in die Systemtheorie. Das Buch geht über den Stoff der Vorlesung hinaus, ist aber sehr anschaulich.
- Kammeyer, Kroschel, *Digitale Signalverarbeitung*,  
  Eines der Standardwerke in der deutschen SV Literatur. Gut geschrieben, Matlab Beispiele, beinhaltet theoretische Hintergründe zu einigen wichtigen Punkten der Vorlesung
- Proakis, Manolakis, *Digital Signal Processing*,  
  Meine Empfehlung, ein hervorragendes Buch, Sie lernen außerdem gleich die englischen Fachbegriffe
- Orfanidis, *Introduction to digital signal processing*, 
  Schönes Einsteigerbuch mit Beispielen aus dem Audiobereich
- Martin Meyer, *Grundlagen der Informationstechnik - Signale, Systeme und Filter*, 1. Auflage, Vieweg-Verlag.
- Vary, Heute, Hess, *Digitale Sprachsignalverarbeitung*,  
  Geht inhaltlich deutlich über die Vorlesung hinaus. Ist für alle interessant, die in diesem Bereich einmal Arbeiten wollen.
- Zölzer, *Digitale Audiosignalverarbeitung*,  
  Spezialbuch für alle Interessierten.
<!-- #endregion -->
