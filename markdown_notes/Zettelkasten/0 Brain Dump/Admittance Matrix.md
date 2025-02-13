---
stage:
  - knowledge
date: 2025-01-30
---
Nodal admittance matrix can be calculated via the method described in the [Wikipedia entry](https://en.wikipedia.org/wiki/Nodal_admittance_matrix). The y-bus matrix is part of the algebraic equations in Power system modeling, and thus understandable more as the "static" par. Although it can be manipulated or changed during the operation.

![[3_bus_network.jpg]]

For the given network the nodal admittance matrix can be calculated as following:
$$
Y=
\begin{bmatrix}
y_1+y_{12}+y_{13}&-y_{12}&-y_{13}\\
-y_{12}&y_2+y_{12}+y_{23}&-y_{23}\\
-y_{13}&-y_{23}&y_3+y_{13}+y_{23}
\end{bmatrix}
$$
Quasi-static models, like OLTC [[Transformers]] can be represented via manipulation / re-calculation of the admittance matrix. Therefore, if calculated in each time step, control schemes can be represented as well.
## Literature
- [[Machowski, Bialek, Bumby - Power System Dynamics, Stability and Control]]
## Further Tags
#basic #modeling #power-system #simulation #load 