---
stage:
  - knowledge
date: 2025-02-21
---
**Some comments on functional operation:**
- $[-10;10]$ **typical** as tap positions for an OLTC
- $[-4;4]$ **mandatory** as tap positions for the FSM, simply due to topology and configuration

**Explanation for the questions in [[2025-02-10 Bi-Weekly 9]]:**
- Thoughts of Ilya for the logic of **tap skipping**: How often would the TC exceed the dead band and switch, with one voltage deviation?
	-> In case of doubt: Tending to choose and implement Ilya's parameters and logic
- But: Thinking towards operational use:
	- Slowly control OLTC towards optimal/pre-defined tap position; Thought: Keeping the FSM in an optimal operational range and ensure optimal / maximum dynamic "damping"
	  -> Maybe with different integration functions for the time delays (various dependency on v_diff)
	- Different customers: Some grid areas are characteristic / typical for to high or too low voltages; Therefore using OLTC tap position presets, which are controlled / held
- Considering **filtering** of measurement data: PT1 element
# Literature
- [[Burlakin et. al - Enhanced Voltage Control in Offshore Wind Farms with Fast-Tapping on-Load Tap-Changers]]
- [[Burlakin et. al - Enhancing Variable Shunt Reactors with a Power Electronic Fast-Switching Module]]
- Some internal documentation and meetings

# Further Tags
#control #fsm #simulation #modeling #dynamic 