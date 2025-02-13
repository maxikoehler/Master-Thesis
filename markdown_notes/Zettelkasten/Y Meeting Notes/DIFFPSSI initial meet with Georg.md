**Notes:**
- Admittanz Matrix für Transformator interessant
- Achtung bei Drehung Koordinatensystemen: Global vs. lokal
- Per unit System aufpassen: Manche Maschinen beziehen auf andere Größen: Machowski im Anhang gleich am Anfang
- Per unit system auch bei Trafos: Stern-Dreieck System evtl. ein Unterschied mit ggf. $\sqrt{3}$ ?
- Per unit System: Manche Variablen nicht ein-eindeutig; Manchmal auch gekürzte Größen weggelassen -> manchmal nicht gut dokumentiert; eigentlich für "verständnisvollen" Code hinderlich...
- Regelung Ilya: Fragen wegen wo Simulation laufen lassen -> CIP Pool Rechner

Nice to have / potentially / nice to know:
- Evtl. nice: Als Matrizen lösen möglich statt iterative Integration?
- PyTorch: Bei komplexen Ableitungen sinnvoll für Optimierungen -> Simulation schneller mit numpy


**Offene Fragen:**
- [x] In welchen Größen wird simuliert? **RMS**, EMT, d-q-Koordinaten, ...? Evtl. sinnvoll ein anderes zu nehmen?
      - Auffälligkeit: Simulationsergebnisse quick and dirty schauen anders aus als in PF... (Werte des Modells zwar nicht gecheckt; Fehler sieht aber auch konvex statt konkav gekrümmt aus, ...)
      - Ist das aktuell mit den Current Injections überhaupt interessant, oder passen die Absolutwerte eh überein, weil nichts außer der SG als Differential modelliert ist? -> Wenn ich Trafos, Lasten, und Lines auch als Differentiale rechnen möchte, dann brauch ich doch auf jeden Fall Werte in einem Bezugssystem (symmetrische Komponenten am besten für alles?), um einen Absolut Punkt zu haben. Sonst ist es ja nur relativ und ich kann es nicht rechnen...
- [x] Line Modell auch "nur" statisch... Macht es Sinn, da einfach auch noch ein Differential Modell zu hinterlegen? Oder Gedanke "Co-Simulation", oder zu komplex, oder ...
- [x] Was ist eigentlich mit den statischen Models ```Load``` und ```Shunt```, oder sollen die einfach so bleiben?
- [x] Handling von ```ScEvents``` und ```ParamEvents```? Soll das einfach noch so "dirty" bleiben, oder auch verbessert werden?
      - Aktuell nur 3-phasiger KS auf einem Bus möglich. Was ist mit 1-phasig und/oder auch auf Lines?
- [x] Abbildungen der Netze zu den Examples / Private Examples in ```diffpssi```
- [x] _Relative Pfadimporte? How the Fuck? Vllt ein Unterschied zu "normalen" PCs statt M1 basierter Chip?_

-> sinnvoll kein anderes System
-> Unterschied PF 9-bus und Georg Modell: Keine Transformatorschaltungen drin und Sättigungen bein SG
-> Referenzsysteme können auch zu anderen Ergebnissen führen...
-> Lines sind in RMS nicht dynamisch -> nicht machen
-> Loads wäre zu überlegen; aber aktuell kein Bedarf da
-> 1-phasig logischerweise in RMS nicht möglich
-> Fehler auf lines werden normal durch einen Zusatzbus geregelt; der Einfachheit halber weg gelassen
-> 10e6 Admittanz Maniupulation könnte aber schöner sein
