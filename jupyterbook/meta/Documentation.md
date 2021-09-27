# Allgemeine Code Struktur
Der Zweck aller Skripte ist es eine anschaulich und teilweise interakitve Grafik zu erzeugen. 
Dadurch wird sehr oft ein ähnlicher Aufruf des Plottings und Interaktion folgen. 

## Plotting
Plottingaufrufe für eine Grafink mit Unterplots in M Zeilen und N Spalten folgen nach dem folgenden Muster:
fig, ( (ax_zeile1_spalte1, ax_zeile1_spalte2, ..., ax_zeile1_spalteN), 
	   (ax_zeile2_spalte1, ax_zeile2_spalte2, ..., ax_zeile2_spalteN),
	   (ax_zeileM_spalte1, ax_zeileM_spalte2, ..., ax_zeileM_spalteN) ) = pyplot.subplots( M, N )
Der Plotname wird der Übersichtlichkeit halbe aber einen Hinweis darauf enthalten was geplottet werden wird.
Darauf folgend werden verscheidene Parametereinstellungen, wie xlim, ylim für den Grenzbereich, xlabel, ylabel für die Achsenbeschriftung eingestellt.
Die Änderung von Datenwerten durch interaktive parameteränderung kann durch 2 Mechanismen geschehen:
1. Setzen eines neuen Datenvektors "daten_vec" im plot über das graph objekt das über eine "plot" Funktion zurückgegeben wird. Dafür wird der Aufruf "graph.set_ydata( daten_vec )" verwendet.
2. In Diagrammtypen wie Histogramm muss erst die der gesamte plot auf dem Unterplot "ax" über "ax.cla()" gelöscht werden. Um dann mit den neuen Daten normal neu geplottet zu werden
In beiden Fällen muss am Ende der plot dir fig.canvas.draw_idle() aktualisiert werden

## Interaktion
Geschieht üblicherweise über Slider und Knöpfe.
Diese werden über die on_changed Funktion mit einem definierten Funktionsaufruf verknüpft. Das sieht dann so aus: 
slider1.on_changed(aufzurufende_funktion)
In 4_5+6, 4_8 und 4_9 wird ein Mausklick ähnlich verknüft. Das geschieht auf der Abbildung "fig" über fig.canvas.mpl_connect(event_art , aufzurufende_funktion)
Hier ist die event_art = 'button_press_event'

## Fourier Zero-Padding

## Zeitvektoren
