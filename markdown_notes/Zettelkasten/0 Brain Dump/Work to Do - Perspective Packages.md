---
stage:
  - second stage
date: 2025-02-18
---
### Programming
- [ ] Voltage Stability Illustration / Rating Tool
	- [x] Nose Curves mit OLTC Stufen
	- [x] Nose Curves mit Time Domain Verlauf
	- [x] Theoretische Lastschnittpunkte mit Nose Curves
	- [x] Diffpssi TDS: Last in Abhängigkeit von Zeit setzen 
	- [ ] Kritische Zeiten:
		- [ ] Prüfen / Rechnen der Zeit, bis kritischer Lastpunkt am Knoten Überschritten
			- Interpolation über der Verlauf der kritischen Punkte
			- 3D Visualisierung wie in Van Cutsem?
			- Je nach $\tan \phi$ max. Lastpunkt bekommen -> Schauen wann das Überschritten wird
		- [x] Schneiden von Envelopes
	- [x] FRT Kurven in TDS plotten
- [ ] General diffpssi
	- [x] Zeitabhängige Lasten
	- [x] Verhalten Synchronmaschine: konst. PV liefern auf konst. PQ (?)
	- [ ] Second / Third FSM Control: 
	      - FSM preferred, 
	      - FSM dependent on tap skips, 
	      - FSM / OLTC dependent on dynamics
	- [ ] _(Plotting Lib)_ 
	     - Basic TDS Plots von Spannungen an Bussen
	     - FRT Kurven adden, 
	     - Leistungen / Ströme an Bussen?
	- [ ] _(Networks Lib)_
	      Sammlung von Basic (parametrierbaren) Networks: SMIB, IEEE 9-bus, Simple Gen -Load mit auswahl line oder Trafo
	- [ ] Doku?
	- [ ] Test Cases?
### Validation
1. Pi Model Notebook
2. Control Schemes Notebook
	 - Bus Voltage behavior
	 - Inner Constants and Switching signals
3. Voltage Stability RATING tool: Plausibilities
	- [ ] Validation of Nose Curve Calculation in PF

-> Dazu auf vernünftige Plots achten!
### Writing
- [ ] Methodical Modeling:
	- [ ] Tap Changer Controls
	- [ ] Extended Ideas Controls
	- [ ] Voltage Stability Calculations
- [ ] Verification
	- [ ] Grids / Networks
	- [ ] Pi Model Validation
	- [ ] Control Circuit Validation
- [ ] Case Studies:
	- [ ] Objectives
	- [ ] Setups
	- [ ] Results
- [ ] Discussion
- [ ] Fundamentals:
	- [ ] Voltage Stability
	- [ ] Power System Modeling
	- [ ] Tap Changer Control Description
- [ ] Others (Intro, Summaries, Outlook / Research Questions)
- [ ] Appendix
### Case Studies
Idea here maybe for better comparison: If one has a critical scenario, all busses will become more critical, but are all busses are getting more critical EQUALLY or is there a problem bus? Can the FSM prohibit / improve this behavior?
1. **Voltage Stability Limits**
	- Can the different transformer tap changer control algorithm exceed the limits of voltage stability or approach the boarder closer as the standard OLTC?
	- How does the Continuous Controller compare, considering similar time constants?
2. **Influence on Machines**
3. **Comparison Standard FSM - vs - Operation Oriented Control Logic**
	- Using the OLTC within its benefits and utilize not only the maximum extended bandwith of the FSM, but the maximum damping moment as well
	  -> What would one consider as damping moment? 
	  -> Does this damping moment have a significant influence?
	  -> Can this control scheme ensure optimal, pre-determent tap position of FSM and OLTC?
	  -> First step towards Operational Oriented Control and towards WAMPC (Wide Area Monitoring Protection and Control)
4. **Change of Load Flow** -> Like model I currently have...
	- Analyze and discuss the SMIB example with load
	- Observation: Load flow direction is changing, therefore control algorithm of OLTC is not sufficient enough. -> PF same result...
# Literature
- [[Machowski, Bialek, Bumby - Power System Dynamics, Stability and Control]]
- [[IEEE Guide for Load modeling]]
- [[Danish - Voltage stability in electric power system, a practical introduction]]
- [[Rueda-Torres, Annakage, Vournas et. al - Evaluation of Voltage Stability Assessment Methodologies in Modern Power Systems with Increased Penetration of Inverter-Based Resources (TR 126)]]

# Further Tags
#orga #documentation #structure 