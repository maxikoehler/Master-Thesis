---
stage:
  - second stage
date: 2025-02-18
---
### Theoretical
1. **P-V-Curves / Q-V-Curves** for very simple cases (SMIB; SM load model)
	- [ ] Construction 
	- [ ] Relation to calculated stability point
2. **P-V-Curves / Q-V-Curves** for complexer networks
	- Which structure (per Bus, per Line, per machine-group, ...)?
	- What data do I need for construction?
	- [ ] Construction and Visualization
	- [ ] Monitoring of current stability evaluation
### Modeling
1. **Control Circuits**
	- [x] OLTC
	- [x] FSM
	- [x] Continuous Model
2. **[[Voltage Stability Indices]]**; incl. Framework for stability evaluation / assessment
	- [ ] On-Line possible indices: System variable based
	- [ ] Jacobian Matrix based -> Using the abilities and possibilities of torch
### Validation
1. **[[Transformers]]**
	- [x] Pi Model
	- [x] Taps; Apparent Power; Reactance
	- [ ] Phase shifting angle $\phi$
2. **Control Circuits**
	- [x] Characterization of all models 
	- [ ] Validation in circuit with PF
3. **[[Voltage Stability Indices]]**
	- How to validate this? 
	  -> Slowly build up until stability margin is reached
	  -> Analyzing the point relative to the theoretical limit (e.g. linearized distance to the limit)
	  -> Is this already an evaluation criteria?
### Case Study
5. **Voltage Stability Limits**
	- Can the different transformer tap changer control algorithm exceed the limits of voltage stability or approach the boarder closer as the standard OLTC?
	- How does the Continuous Controller compare, considering similar time constants?
6. **Influence on Machines**
7. **Comparison Standard FSM - vs - Operation Oriented Control Logic**
	- Using the OLTC within its benefits and utilize not only the maximum extended bandwith of the FSM, but the maximum damping moment as well
	  -> What would one consider as damping moment? 
	  -> Does this damping moment have a significant influence?
	  -> Can this control scheme ensure optimal, pre-determent tap position of FSM and OLTC?
	  -> First step towards Operational Oriented Control and towards WAMPC (Wide Area Monitoring Protection and Control)
8. **Change of Load Flow** -> Like model I currently have...
	- Analyze and discuss the SMIB example with load
	- Observation: Load flow direction is changing, therefore control algorithm of OLTC is not sufficient enough. -> PF same result...
# Literature
- [[Machowski, Bialek, Bumby - Power System Dynamics, Stability and Control]]
- [[IEEE Guide for Load modeling]]
- [[Danish - Voltage stability in electric power system, a practical introduction]]
- [[Rueda-Torres, Annakage, Vournas et. al - Evaluation of Voltage Stability Assessment Methodologies in Modern Power Systems with Increased Penetration of Inverter-Based Resources (TR 126)]]

# Further Tags
#orga #documentation #structure 