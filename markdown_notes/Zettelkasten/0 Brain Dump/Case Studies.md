---
stage:
  - idea
date: 2025-01-31
---
### 1 Standard interaction in the SMIB
**Objective:**
- Testing the interaction of the Tap Changer Control mechanism and a Synchronous machine with variable scenarios
- Just a plain machine, with Machine Controls, with Tap Changer Controls
- 1 SC, 1 Load change, 1 Load Flow direction change
- Can the FSM hold the voltage band longer than the OLTC?

**Set-Up:**
- SMIB with given parameters and Controls
- Voltage stability Rating(s) applied to the Scenario
- Different events: SC and / or load changes
### 2 Looking at Power Swings and Possible Damping
**Objective:**
- Testing out different Time Constants and their effect on Power Swings in a SMIB (after SC with possible load change during this as well)
- Parameter variation between only OLTC and different time constants of the FSM

**Set-Up:**
- SMIB with load as before
- SC _together_ with a load change
### 3 Novel Control Strategy
**Objective:**
- Testing out different tap skipping logics
- Testing out a voltage gradient based activation of either the FSM or the OLTC 
	- Time constant dependent on voltage difference
	- Calculate the current voltage gradient -> Time constant dependent on derivative of voltage difference
- How do these changes affect the control behavior (SC or Load Change)

**Set-Up:**
- SMIB model
- LVRT with SC and HVRT with load shed
## Further Tags
#simulation #fsm #limitations #stability-assessment #dynamic #documentation 