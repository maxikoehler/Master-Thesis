---
stage:
  - idea
date: 2025-01-31
---
### Contents
1. Modeling of [[Transformers]]
2. Implementation of [[OLTC Control Schemes]] (discrete / continuous / FSM)
3. Implementation of [[Voltage Stability Indices]]
4. Influence of the OLTC on static / dynamic voltage stability
### Research question(s)
Main governing question:
>How do different control types and characteristics of Tap Changing transformers influence the voltage stability?

With following supportive steps and questions:
1. How can Voltage stability of a system be classified and be looked at? Which indices, measurements, etc.
2. Which transformer model has to be considered to show influences? Which control circuits are representative enough, which are mandatory? 
3. Which additional load models, source models, transmission model have to be modeled for an adequate assessment?
4. Which systems are useful to consider in showing effects? Which circumstances lead to a stability support, which to a decrease? Where can limits be drawn?
### Methods
- Literature research

- Mathematical modeling: [[Transformers]] and [[Voltage Stability Indices]]
- Simulation
- Verification of the mathematical model with PowerFactory
- [[Analytical Stability Calculation]]

- Showcases / [[Case Studies]]: Analysis, if a FSM transformer can exceed the boundaries of voltage stability in a system
### Excluded
More specified in [[Limitations of the Thesis]], but key take aways resp. main points:
1. **Only inductive model** (respectfully for RMS modeling / simulation)
2. **Only positive sequence (symmetrical components)**, thus only HV transmission and MV distribution grids
   -> additionally: Most of the OLTC equipped transformers are used as grid coupling between HV-HV and/or HV-MV
3. **No (actively controlled) phase shift**, due to more complex control and stability assessment?
   -> just longitudinal control or transverse control as well? 
   -> representative circuits differ and would be more complex
## Further Tags
#structure #orga #documentation 