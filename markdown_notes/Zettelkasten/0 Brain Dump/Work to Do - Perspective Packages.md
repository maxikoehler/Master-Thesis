---
stage:
  - second stage
date: 2025-02-18
---
### Programming
- [ ] General diffpssi
	- [x] Zeitabhängige Lasten
	- [x] Verhalten Synchronmaschine: konst. PV liefern auf konst. PQ (?)
	- [x] Second FSM Control (FSM dependent on tap skips / Voltage difference)
	- [ ] Third FSM Control (Dynamic dependent switching)
	- [ ] Fourth FSM Control: Alternative Tap Switching
	- [ ] Fifth FSM Control ...?
	- [ ] Doku?
### Writing
- [ ] Methodical Modeling:
	- [ ] Tap Changer Controls
	- [ ] Extended Ideas Controls
	- [x] Voltage Stability Calculations
	- [ ] Klassendiagramme / Flow Charts / etc.
- [ ] Verification
	- [x] Grids / Networks
	- [x] Pi Model Validation
	- [x] Control Circuit Validation
	- [x] Voltage Tools
	- [ ] Describe all parameters of the grids; All scenarios, all everything in detail
- [ ] Case Studies:
	- [ ] Objectives
	- [ ] Setups
	- [ ] Results
- [ ] Discussion
- [ ] Fundamentals:
	- [ ] Voltage Stability
	- [x] Power System Modeling
	- [x] Tap Changer Control Description
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
	- OR: Automatic Detection of the Switching direction
### For Handing In
- [ ] Basic commenting
- [ ] Clean up Repositories
- [ ] Make Releases (Better time stamps and accountable compared to a single commit)
- [ ] Send email, teams message

### Work after Hand In
- [ ] Presentation
- [ ] Making the Version print ready (if necessary?)
- [ ] Cover Design
- [ ] Code Commenting?
# Literature
- [[Machowski, Bialek, Bumby - Power System Dynamics, Stability and Control]]
- [[IEEE Guide for Load modeling]]
- [[Danish - Voltage stability in electric power system, a practical introduction]]
- [[Rueda-Torres, Annakage, Vournas et. al - Evaluation of Voltage Stability Assessment Methodologies in Modern Power Systems with Increased Penetration of Inverter-Based Resources (TR 126)]]

# Further Tags
#orga #documentation #structure 