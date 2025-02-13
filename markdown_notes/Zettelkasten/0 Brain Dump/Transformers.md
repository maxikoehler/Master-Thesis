---
stage:
  - primary note
date: 2025-01-31
---
## Types - Construction and usage

### Circuit types

### Where to use which type of transformer?

## Modelling
-> first approach: influencing the nodal [[Admittance Matrix]]? If static case, and not dynamically modeled, a reduced version of this admittance matrix can be used.

Two approaches usually used:
1. **Current Injection Models**:
   - Using a symmetric admittance matrix, and a unsymmetrical part. Last one is represented as Current Injection at the connected nodes
   - Often used in complex simulations: System Matrix is becoming easier to compute
2. Representation in the **[[Admittance Matrix]]**:
   - (Possibly) Unsymmetric Admittance Matrix is directly integrated in the System Matrix
   - Is this better for direct Stability Assessment? Due to complete representation in the Algebraic equations? 
### Dynamic behavior
Depending on assessment and interest, one can look at:
1. **slower grid frequency:** stationary model
2. **approx. grid frequency:** inductive representative model
3. **areas of some kHz to MHz:** representative model, including capacitive coupling of windings, windings and earth, and the capacity of the windings itself
   -> This is clearly **EMT modeling**; thus not scope of the thesis!

Integration of this dynamic equations into a [[RMS Simulation]], with an additionally describing and manipulated nodal [[Admittance Matrix]], leads to a time-dependent simulation of a symmetrical grid.
### Phase shifting
If using p.u. values, the transformer ratio is usually in unity, meaning $\theta=1$. Although neglecting it can cause difficulties, when not being in unity, especially when using tap changers, or when the rated transformer voltages slightly differ from the network rated voltages. 
In case of phase shifting transformers, the transformer ratio $\theta$ becomes a complex number $\underline{\theta}$.

If the Phase shifting angle is actively controlled, then the transformer can manipulate the reactive power injection at the secondary bus. Some transformers can actively control both, longitudinal and transverse ratio. However, control algorithms are getting more complicated.
## Control methods
[[Bifurcation]] is used for **static** applications, although not only for assessing [[Stability mechanisms]], but as well for controlling the transformer.

For dynamic applications, there are a few standard approaches, novel ideas and wide-area applications are part of the [[Literature Research]]. A general view of [[Control technology and engineering]] is researched as well.
# Literature
- [[Milano - Power System Modeling and Scripting]]
- [[Machowski, Bialek, Bumby - Power System Dynamics, Stability and Control]]
# Further Tags
#modeling #stability #power-system #power-system 