---
status:
  - closed
Participants:
  - Ilya Burlakin
  - Georg Kordowich
Date: 2024-09-23
---
### Open points:
- [x] Timeline / Kick-off presentation?
- [ ] TeX template?
### Results:
- Integration of transformer incl. phase rotation
- step/discrete voltage control
- ...
<br>
- Einarbeitung -> Präsentation und Excel Zeitschiene -> Anmeldung (plus-minus 2 Wochen)
- 15. Oktober ca. Kick-off -> +- 2 Wochen Anmeldung
- -> Kick-off presentation and timeline necessary
### Questions:
- How does transformer regulation / voltage control normally work? Which is the governing value (OS, US part of the transformer?, grid voltage, load side of the transformer?, secondary side?)
	- Depends on the interested value and control strategy; sometimes it seems useful controlling the voltage of a high voltage line, sometimes it is not relevant and the more load-orientated low- (or medium-) voltage grids and nodes are mandatory
- Is the FSM capable of varying the power angle? -> not only control of the voltage by different transformer ratio, but as well through "compensation" of needed reactive power possible (more complex control)?
	- No, it is a thyristor based circuit with different current states, allowing a step rage of $\in[-4;4]$ . Phase rotation is part of another EES project, but another circuit/module/part 

## Further Tags
#orga #fsm

Follow-up defined for [[2024-10-07 Bi-Weekly 1]].