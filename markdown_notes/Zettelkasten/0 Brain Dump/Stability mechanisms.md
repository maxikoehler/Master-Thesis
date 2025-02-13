---
stage:
  - primary note
date:
---
## Voltage stability
Due to imbalances in reactive power generation and demand. Large grids demand higher reactive power, therefore are more critical to stabilize. Methods for ensuring voltage stability are applied locally, most of the times with STATCOMs, compensation, FACTs, or similar. However, voltage stability can be further classified with following aspects:
1. Short-term vs. Long-term Voltage Stability 
2. Static vs. Dynamic Voltage Stability
3. Contributions from Transmission, Load, and Generation

How to determine voltage stability?
- [[Bifurcation]]; meaning P-Q-V Curves and their saddle points as max. stable operation points 
- [[Voltage Stability Classification]]
- [[Voltage Stability Indices]]

OLTCs are usually are restoring the voltage level in the first place, but secondary it is not supporting with reactive power capabilities. Meaning at the same time it is increasing the risk of a voltage collapse. (Danish 2015)
In real-life application the OLTC is restricted in its use as voltage stabilizer, due to its small operational margin. (Danish 2015)
## Power angle stability (Transient)
Due to electromagnetic behavior of the synchronous machines. Maximum generator power at power angle $\delta=90^\circ$, therefore a partly utilization is leading to a power angle smaller than that. Dynamically, the power angle can be higher than this static limit, but other dependencies have to be fulfilled. 

General idea on this: Does a fast-switching transformer influence this rather short-term appearing phenomena? If yes, does it have a positive or negative impact?
## Frequency stability
Due to imbalances in load power vs. generated power. Different equipment is responding with another behavior, e.g. synchronous machines $P\sim f^3$ , while lightbulbs / -sources mostly $P\sim f^1$.

**BUT:** This is definitely not scope of the thesis!
# Literature
- [[Danish - Voltage stability in electric power system, a practical introduction]]
- [[Machowski, Bialek, Bumby - Power System Dynamics, Stability and Control]]
- [[Rueda-Torres, Annakage, Vournas et. al - Evaluation of Voltage Stability Assessment Methodologies in Modern Power Systems with Increased Penetration of Inverter-Based Resources (TR 126)]]
# Further Tags
#stability #bifurcation #stability-assessment #power-system