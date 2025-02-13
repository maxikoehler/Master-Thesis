---
stage:
  - idea
date: 2025-01-28
---
Voltage assessments for evaluation of control circuits doesn't have to be online. Because of offline nature, the system with its event(s) can be simulated, and afterwards it can be evaluated. 

Every needed parameter can be recorded, and evaluated afterwards. This eases looking at derivatives, or integrals (esp. numerical nature) a lot.

Proposed procedure:
- Simulate the experiment with all bus voltages
- Gather all the necessary values for the indices
- Numerically calculate the indice in dependence of the simulation time ($Index(t)$) 
- Plot the Index next to the Bus voltages

Following, the assessment should't be from chaotic nature.
## Literature
- [[Danish - Voltage stability in electric power system, a practical introduction]]

## Further Tags
#stability-assessment #simulation #structure #algorithm