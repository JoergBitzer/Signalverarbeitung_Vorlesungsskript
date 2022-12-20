---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

(sec:exercises)=
# Übungen

Dieser Abschnitt enthält eine Sammlung an Wiederholungsfragen und Übungsaufgaben. Die Übungen sind nach den Buchkapiteln sortiert, zum Teil ergeben sich thematische Überschneidungen. Zu jedem Kapitel gibt es Übungen zur *Wiederholung des Stoffes und einfache Rechenaufgaben*, gefolgt von Aufgaben (auf Klausurniveau) und Programmieraufgaben. Einige Programmieraufgaben sind noch für Matlab formuliert, eine Anpassung für Python folgt in Zukunft.


## Signale

### Wiederholung des Stoffes und einfache Rechenaufgaben

1.  Klassifizieren Sie folgende Signale anhand der in {numref}`Kapitel %s  <sec:signale>` angegeben Merkmale:
    +   $si(t)$  
    +   Das digitale (SP-DIF) und analoge Signal eines CD-Players  
    +   Ein DVD-Film  
    +   Vielleicht ihr Beispiel  

2.  Was ist die Grundvoraussetzung für eine erfolgreiche Digitalisierung?  

3.  Warum verliert man Informationen bei der Digitalisierung?  

4.  Warum lassen sich Funktionen mit Knickstellen (Bsp: Dreieck) nicht wirklich digitalisieren?  

5.  Welches ist die höchste Harmonische einer aliasingfreien Dreieckschwingung mit der Grundfrequenz $f = 440$  
    Hz, bei einer Abtastrate von $f_s = 48000$ Hz?  

6.  Zeigen Sie, dass $si$(0) = 1 ist!  

7.  Zeichnen Sie $x(k) = 2\delta(k + 2) - 0.5\delta(k - 1) + 3\delta(k - 2)$ .

### Aufgaben (Auf Klausurniveau)
1.  Wie hoch ist die Leistung eines mittelwertfreien Dreieckssignals mit der Amplitude A?


### Programmieraufgaben
1.  Programmieren Sie eine Funktion, die einen Mid-Tread Quantisierer mit einer Auflösung von 4 Bit     
    realisiert. Versuchen Sie so allgemein zu programmieren, dass Sie jederzeit die Auflösung ändern können.

2.  Programmieren Sie einen Rechtecksignal-Generator mit und ohne Aliasing.

3.  Erzeugen Sie eine Funktion die eine Delta-Impulsfolge mit vordefinierter Länge (Angabe in Sekunden und $f_s$) 
    zurückgibt.



## Systeme

### Wiederholung des Stoffes und einfache Rechenaufgaben

1.  Ist ein Quantisierer ein lineares System, da ja von linearer
    Quantisierung gesprochen wird? Begründen Sie ihre Antwort.

2.  Sind die folgenden Systeme zeitinvariant, kausal und linear?
    Begründen Sie ihre Antwort.

    -   $y(k) = x(k) + 2d$ mit $d\neq 0$

    -   $y(k) = a_1 x(k-2) + a_2 x(k-3)$

    -   $y(k) = k x(k-1) + x(k-2)$

    -   $y(k) = log_{10}( x(k-2)) + 3 x(k-1)$

3.  Falten Sie die folgenden vier Signale jeweils grafisch mit sich
    selbst und mit allen anderen Signalen.

    ```{figure} ../images/psUeb/GraphikFaltung.png
    ---
    height: 150px
    name: fig:GraphikFaltung
    ---
    Testsignale zum Üben der grafischen Faltung
    ``` 

4.  Zeigen Sie, dass das Kommutativgesetz der Faltung allgemein gilt.

(sec:AufgabenSys)=
### Aufgaben (Einige auf Klausurniveau)

1.  Geben sie die Impulsantwort für die
    folgenden Differenzengleichungen an. Brechen Sie bei unendlichen
    Folgen nach $k=10$ ab. Nehmen sie an, dass sich das System zum
    Zeitpunkt $k=0$ in Ruhe befand.

    -  $y(k) = 0.5x(k-1)+ 0.3x(k-2)+ 0.4x(k-3) - 0.4 x(k-4)$

    -  $y(k) = y(k-1)+0.5x(k)$

    -  $y(k) = 0.25 x(k-1)+0.75 y(k-1) - 0.75y(k-3)$

2.  Gegeben ist das System $0 = \frac{1}{k} x(k) + 2x(k-2) - 0.5y(k-1)$.
    Begründen Sie Linearität und Zeit-Invarianz bitte mathematisch
    formal!


### Programmieraufgaben

1.  Testen Sie folgende Systeme auf Zeitinvarianz und Linearität durch
    Rauschfolgen als Eingangssignale. Haben Sie im Hinterkopf, dass Sie
    mit Zahlentests nichts beweisen können. Eine Aussage ist nur für
    Nicht-Linearität und Zeitvarianz möglich. Dies ergibt sich, wenn der
    Test fehl schlägt, da *ein* Gegenbeispiel ausreicht um Linearität
    oder Zeitinvarianz auszuschließen.

    -   $y(k) = x(k) + y(k-1)$

    -   $y(k) = 3 y(k-1) + 2 x(k-1) + x(k)$

    -   $y(k) = k x(k-1) + x(k-2)$

    -   $y(k) = log_{10} x(k-2) + 3 y(k-1)$

2.  Erzeugen Sie eine Funktion die eine Delta-Impulsfolge mit
    vordefinierter Länge zurück gibt.

3.  Nutzen Sie diese Funktion, um ihre Ergebnisse aus {numref}`Abschnitt %s <sec:AufgabenSys>` Aufgabe 1 zu überprüfen.

4.  Erzeugen Sie kurze Sequenzen mit $T = 12$ Werten um die oben
    gezeigten Signale zu approximieren. Überprüfen Sie Ihre Ergebnisse
    mit dem `conv`-Befehl.



## z-Transformation

### Wiederholung des Stoffes und einfache Rechenaufgaben
1.  Welche Bedingungen müssen gelten, damit ein LTI-System stabil ist?

2.  Welche Beschreibungen eines LTI-Systems kennen Sie?

3.  Warum ist die Angabe der z-Transformationsfunktion nicht ausreichend?

4.  Testen Sie die folgenden LTI-Systeme auf Stabilität:
    -   $y(k) = -2y(k - 1) + 1.5x(k) - 2x(k - 1)$
    -   $y(k) = 2.5x(k - 1) + 1.83y(k - 1) - 0.99y(k - 2)$
    -   $y(k) = 0.3x(k) + 0.7x(k - 1) + 1.9812y(k - 1) - 1.0201y(k - 2)$

5. Zeigen Sie, dass die Ungleichung {eq}`eq:SOS:Ungleichung2` gilt.


(sec:AufgabenZTrafo)=
### Aufgaben (Auf Klausurniveau)

1.  Zeigen Sie, dass die z-Transformation eine lineare Transformation
    ist, indem Sie den Linearitätstest durchführen.

2.  Welchen Wert hat das folgende System nach 50 Schritten. Geben Sie die direkte Berechnungsmethode an. 
    Ist das System BIBO-stabil?\
    $y(k) = \sqrt(2) y(k-1) -  y(k-2) + 0.5 \delta(k)$

3.  Sind die folgenden Systeme kausal, stabil, linear und zeitinvariant?
    Begründen Sie ihre Antwort (auch wenn Sie keine Aussage machen
    können) mathematisch oder textuell (16)!

    -  $y(k) = 0.5 y(k-1) - 0.3 y(k-2) k + 0.4 x(k) - 0.5x(k-1)x(k-2)$

    -  $y(k+1) = 1.1 y(k-1) - 0.5 x(k+1) + 0.3 x(k) - 0.5x(k-1)$

    -  $y(k+1) = 2x(2k-k) - y(k+1) + 4 x(k-2) + 1.8 y(k-1)$

    -  $y(k) = 0.3 x(k) + 0.6x(k-1) - 0.7 x(k-2)y(k-2) + x(2k-2)$

4.  Ist das folgende Systeme kausal, stabil, linear und zeitinvariant?
    Begründen Sie ihre Antwort mathematisch oder textuell! Falls Sie
    keine Aussage treffen können, begründen Sie auch dies!\
    $y(k+1) - 2y(k+2) + \alpha x(k+2) + x(k+1) =  1.99 y(k)$\
    Nehmen Sie an $\alpha = 2$ (8 Punkte). Für welche Bereiche von
    $\alpha$ (rein reell) ist das System stabil (Begründung)? (2 Punkte)

5.  Sind die beiden folgenden Systeme kausal, stabil, linear und
    zeitinvariant? Begründen Sie ihre Antwort mathematisch oder
    textuell! Falls Sie keine Aussage treffen können, begründen Sie auch
    dies!

    -  $y(k) + \beta^2 y(k-2) + x(k-2) = 2 x(k) - 2x(k-2) - 1.9y(k-1)$.\
        Zur Beantwortung der Frage nehmen Sie an $\beta = \sqrt{0.5}$ (8
        Punkte).\
        Für welche Bereiche von $\beta$ ist das System stabil bzw.
        instabil (4 Punkte).

    -  $2y(k) - 3.7x(-k-2)k -0.3y(k-3) = 10x(k-10)$. (8 Punkte)


### Programmieraufgaben

1.  Lösen Sie die Aufgabe 2 aus {numref}`Abschnitt %s <sec:AufgabenZTrafo>` durch den Aufbau des Systems und
    Iteration.

2.  Programmieren Sie eine Funktion, die einen Pol-Nullstellenplan
    zeichnet und zusätzlich im Titel den $b_0$-Koeffizienten ausgibt.
    Nutzen Sie als Anhaltspunkt die `zplane` Funktion von Matlab.
    Hinweis: Sie benötigen den `axis` Befehl um eine quadratische Grafik
    aufzubauen (siehe help). Sie sollten die `mpoles` Funktion nutzen,
    um Mehrfach Null- bzw. Polstellen herauszufinden.

3.  Schreiben Sie eine Funktion, die es ermöglicht Systeme durch eine
    grafische Eingabe mit der Maus zu definieren. Zeichnen Sie dazu den
    Einheitskreis in eine figure. Hinweis: Sie benötigen den `ginput`
    Befehl für die Maus-Eingabe und `axis`, um eine quadratische Grafik
    zu erzeugen.




## Spektren

### Wiederholung des Stoffes und einfache Rechenaufgaben

1.  Bei einer Abtastrate von 44100 Hz und einer DFT Auflösung von $1024$
    soll ein Sinus erzeugt werden, der keinerlei Leakage-Effekt zur Folge
    hat. Welche Frequenzen sind mögliche Kandidaten.

2.  Wozu werden Fensterfunktionen benötigt?

3.  Nach welchem Prinzip kann die Rechenleistung der DFT reduziert werden?

4.  Welchen Einfluss haben Pole auf das Übertragungsverhalten und welchen Einfluss Nullstellen?

5.  Wodurch entsteht ein Allpass-System?

6.  Erklären Sie, die Folgen des Übergangs von der DTFT zur DFT!

7.  Um zu zeigen, dass nicht-lineare Systeme neue Frequenzen erzeugen,
    sollten Sie das System $y(k) = x^2(k)$ mit der Exponentialschwingung
    anregen und sich das Ergebnis anschauen

8.  Ein mit 200Hz abgetastetes reelles Signal wird mit einer 8 Punkte
    DFT spektral analysiert. Welche Frequenzbereiche sind in den 8
    Spektralwerten enthalten? Welche dieser Werte (Indize) haben den
    gleichen Betrag?

9.  Zeichnen Sie qualitativ die Betragsübertragungsfunktion für die
    folgenden durch einen Pol-Nullstellenplan gegebenen Systeme:
    
    ```{figure} ../images/psUeb/PolNullstellenUebung.png
    ---
    height: 500px
    name: fig:PolNullstellenUebung
    ---
    Verschiedene Systeme und ihre Pol-/ Nullstellenverteilung
    ``` 

10. Berechnen Sie das Spektrum einer Cosinus-Schwingung der Frequenz
    2000 Hz bei einer Abtastrate von 6000 Hz, wenn Sie eine 6 Punkte DFT
    verwenden.


### Aufgaben (Auf Klausurniveau)

1.  Welche Pol-Nullstellenlage würde die folgende
    Betragsübertragungsfunktion mit dazugehöriger Phase bei einem
    reellwertigen, stabilen System zur Folge haben ($f_s = 8000$ Hz)?
    (Genauere qualitative Skizze (Grosser Kreis bitte!) und kurze
    stichpunktartige Begründung für die relevanten Punkte)(8)
    
    ```{figure} ../images/psUeb/Betrag_14_20_18.png
    ---
    height: 300px
    ---
    ``` 
    
    ```{figure} ../images/psUeb/Phase_14_20_18.png
    ---
    height: 300px
    ---
    ``` 

2.  Berechnen Sie die Übertragungsfunktion zur Impulsantwort
    $h(k) = [1\;\; 0\;\; 1]$

3.  Berechnen Sie die Übertragungsfunktion zu dem folgenden Filter:
    $y(k) = x(k) - \alpha y(k-1)$.\
    Skizzieren Sie die Funktion für $\alpha = 0.9$ und $\alpha = -0.9$

4.  Ordnen Sie die folgenden Pol-Nullstellenpläne (a-d) den
    verschiedenen Übertragungsfunktionen (1-8) zu (2 Punkte für jede
    richtige Zuordnung, -1 Punkt für jede falsche).

    ```{figure} ../images/psUeb/PolNullstellenKlausur2.png
    ---
    height: 200px
    ---
    ``` 
    
    ```{figure} ../images/psUeb/UebertragungKlausur2.png
    ---
    height: 500px
    ---
    ``` 

### Programmieraufgaben

1.  Bestimmen Sie die Übertragungsfunktion der folgenden Systeme.

    -  $y(k) = x(k) - \alpha y(k-1)$

    -  $y(k) =  0.3 x(k) + 07 x(k-1) + 1.9812 y(k-1)   - 1.0201 y(k-2)$


### Transferleistung

1.  Bei der Berechnung des Faltungsprodukts muss bei der DFT/FFT auf die
    Zirkularität geachtet werden. Welche Probleme können auftreten, wenn
    das Ausgansspektrum nicht durch Multiplikation $Y(n) = X(n)H(n)$,
    sondern durch eine Division $Y(n) = X(n)/H(n)$ entsteht (sog.
    Deconvolutionproblem)

2.  Welche Folge hat das Decimation in Time Prinzip der FFT für den
    Zusammenhang der Eingangsfolge zum berechneten Spektrum. Anders
    ausgedrückt, was ist notwendig, damit das Prinzip funktioniert.




## Filter

### Wiederholung des Stoffes und einfache Rechenaufgaben

1.  Nennen Sie jeweils eine mögliche Anwendung (am besten aus dem
    Bereich der Audiotechnik, Hörtechnik, Audiologie) für die
    verschiedenen Grundcharakteristika der Filter und überlegen sich, wie die
    Entwurfsparamter aussehen könnten (Grenzfrequenz, Ordnung)

2.  Geben Sie zu folgendem Blockschaltbild die Differenzengleichung an.

    ```{figure} ../images/psUeb/IIr_2terOrdnung.png
    ---
    width: 30%
    name: fig:IIr_2terOrdnung
    ---
    Blockschaltbild eines Systems
    ```

3.  Welche Vor- und Nachteile ergeben sich durch das Overlap-Add
    Verfahren zur schnellen Faltung?

4.  Zeichnen Sie zu den folgenden Systemen eine Realisierung als
    Blockschaltbild

    -  $y(k) = x(k) - \alpha y(k-1)$

    -  $y(k) =  0.3 x(k) + 0.7 x(k-1) + 1.9812 y(k-1)   - 1.0201 y(k-2)$

### Aufgaben (Auf Klausurniveau)

1.  Berechnen Sie die Übertragungsfunktion der Impulsantwort
    $h(k) = [-1 \;\; 1]$! Skizzieren Sie den Betrags- und Phasengang! Um
    was für einen Filtertyp handelt es sich (Realisierungsform und
    Filtercharakteristik)?

2.  Sie sehen die folgende Impulsantwort. Um was für ein Filter handelt
    es sich (Realisierung und Filtercharakteristik)? Berechnen Sie die
    Übertragungsfunktion und skizzieren Sie den Betrags- und
    Phasenverlauf! Was ist besonders an diesem Filter und könnte es
    realisiert werden?

    ```{figure} ../images/psUeb/KlausurWS2003_2IR.png
    ---
    width: 20%
    name: fig:KlausurWS2003_2IR
    ```

3.  Gegeben ist das folgende System
    
    $$
    y(k) = 2x(k) + 2x(k-1) - 2x(k-3) - 2x(k-4)
    $$ 
    
    Berechnen Sie die
    Übertragungsfunktion nach Betrag und Phase! Skizzieren Sie den
    Betrags- und Phasenverlauf zwischen 0 und $\pi$! Um was für einen
    Typ Filter handelt es sich? Zeichnen Sie eine möglichst effiziente
    Realisierung als Blockschaltbild!

4.  Skizzieren Sie den Betragsverlauf zu dem hier vorliegenden
    Pol-Nullstellenplan! Welche besonderen Eigenschaften hat dieses
    System? Geben Sie die Übertragungsfunktion $H(z)$ als Funktion von
    Biquads an. Nehmen Sie an, die Radien für die Pole und Nullstellen
    betragen $0.9$ bzw $1.1$ und $b_0 = 1$.


    ```{figure} ../images/psUeb/PZ_18_25_28.png
    ---
    width: 50%
    name: fig:PZ_18_25_28
    ---
    ```

5.  Wie lautet die Differenzengleichung und die Übertragungsfunktion des
    folgenden Systems nach Betrag und Phase? Zeichnen Sie den Betrags-
    und Phasenverlauf! Um was für eine Art Filter handelt es sich? (Typ
    und Realisierungsform)


    ```{figure} ../images/psUeb/FIR_zweiterOrdnung.png
    ---
    width: 50%
    name: fig:FIR_zweiterOrdnung
    ```


### Programmieraufgaben

1.  Realisieren Sie eine Funktion, die die Koeffizienten eines mit der
    Fenstermethode entworfenen Tiefpasses zurückgibt. Als
    Übergabeparameter sollten die Grenzfrequenz, die Ordnung und das zu
    verwendende Fenster zur Verfügung stehen. Als Standard-Fenster soll
    das Rechteck-Fenster verwendet werden.

2.  Schreiben Sie eine Funktion, die aus einem beliebigen FIR-Filter
    eine minimalphasige Realisierung macht, wobei die
    Betragsübertragungsfunktion exakt erhalten bleiben soll. Die
    Übergabeparameter sind nur die bisher verwendeten FIR-Koeffizienten.


### Transferleistung

1.  Überlegen Sie eine weitere kanonische Struktur für SOS-Filter.

2.  Nehmen wir an beim OLA-Verfahren wechselt die Übertragungsfunktion
    während der Datenvektor noch nicht vollständig bearbeitet wurde
    (Zeitvariantes Verhalten). Was glauben Sie ist die Folge? Können Sie
    sich vorstellen, wie man die auftretenden Probleme lösen kann?

 
