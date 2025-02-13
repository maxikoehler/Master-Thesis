---
type:
  - book
date: 
year: 2015
stage:
  - literature
---
## Key takeaways
- [[Jacobian-based Stability Assessments]]
- [[Improved Formulations of Stability Indices]]
- Some useful and applicable Jacobian-based indices:
	- Tangent Vector Index
	- Test Function
	- i
	- Minimum Eigenvalue
	- Minimum Singular Value
	- Predicting Voltage Collapse
	- Impedance Ratio
## Excerpts
### Chapter 2
#### The improved index formulation
This section presents an introductory concept of numerical computation methods (SVD, and Pseudo-inverse) as well as the application of these methods in order to integrate the original indices as an improved indicator. Based on the load flow equations, the following customary matrices can be denoted:
$$
\begin{bmatrix}\Delta P \\ \Delta Q\end{bmatrix}=\begin{bmatrix}J_{P\delta} & J_{PV} \\ J_{Q\delta} & J_{QV}\end{bmatrix}\begin{bmatrix}\Delta \delta \\ \Delta V\end{bmatrix}=[J]\begin{bmatrix}\Delta \delta \\ \Delta V\end{bmatrix}
$$
In static analysis, from the rank of Jacobian matrix $[J]$ point of view, it is assumed that the rank of load flow Jacobian matrix is equal to the rank of system Jacobian (under certain assumptions, such as PV buses are known, loads are constant power (P and Q) types, and the slack node is an infinite bus) [49]. With taking into account the given conditions, the determinant of the load flow Jacobian matrix is identical to the product of all the eigenvalues of the system Jacobian matrix [42]. So, the rank of $[J]$ and reduced Jacobian matrix $[J_R]$ are identical. It implies that the $[J_{P\delta}]$ is nonsingular (it is symmetrical matrix). With pursue the Schur's formula we can obtain (more details are given in [24, 42, 50, 51]):
$$\begin{align}
[J_R]&=[J_{QV}]-[J_{Q\delta}][J_{P\delta}]^{-1}[J_{PV}] \\[12pt]
\mathrm{det}[J]&=\mathrm{det}[J_{P\delta}] \cdot \mathrm{det}[J_R]
\end{align}$$
Every $\mathrm{\textbf{A}}(\mathbb{R}^{m \times n})$ matrix, $m \geq n$ can be decomposed as:
$$\begin{align}
\mathrm{\textbf{A}}&=\mathrm{\textbf{U}} \sum \mathrm{\textbf{V}}^T \\[12pt]
\sum &=\mathrm{\textbf{U}}^T\mathrm{\textbf{A}}\mathrm{\textbf{V}} \\[12pt]
{\sum}^{-1} &=\mathrm{\textbf{V}}^T\mathrm{\textbf{A}}^{-1}\mathrm{\textbf{U}}
\end{align}$$
where superscript  $()^T$ denotes the transposed matrix. $\mathrm{\textbf{U}}(\mathbb{R}^{m \times n})$, and $\mathrm{\textbf{V}}(\mathbb{R}^{m \times n})$ are termed right and left singular matrixes, which satisfy
$$
\mathrm{\textbf{U}}^T\mathrm{\textbf{U}}=\mathrm{\textbf{V}}^T\mathrm{\textbf{V}}=\mathrm{\textbf{V}}\mathrm{\textbf{V}}^T=I_n
$$
where, $\sum = < \sigma_1, \dots, \sigma_n >$ these elements hold on the diagonal of the matrix. Let the $\sigma_i$'s be called in order, $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n \geq 0$. Which are the square root of the non-negative eigenvalues $\mathrm{\textbf{A}}^T\mathrm{\textbf{A}}$ and are called the singular values of matrix $\mathrm{\textbf{A}}$. If suppose, $\mathrm{\textbf{A}}$ is nonsingular and one of these conditions satisfy [52]. There is a matrix $\mathrm{\textbf{A}}^{-1}$ such that

- ﻿$\mathrm{\textbf{A}}^{-1}\mathrm{\textbf{A}}=\mathrm{\textbf{A}}\mathrm{\textbf{A}}^{-1}=I$
- ﻿﻿$\mathrm{det}(\mathrm{\textbf{A}}) \neq 0$
- ﻿﻿The eigenvalues of $\mathrm{\textbf{A}}$ are nonzero
- ﻿﻿The singular values of $\mathrm{\textbf{A}}$ are nonzero

To infer by linear algebra analogy, the linear equation can be express as $\mathrm{\textbf{A}}x = b$. The solution can be rearranged as $x = \mathrm{\textbf{A}}^{-1}b$; where, we intent to consider the variation of $V - Q$, so change in $P$ is neglected in the formulation ($[\Delta P] = 0$). Therefore, we can obtain
$$\begin{align}
\begin{bmatrix}0 \\ \Delta Q\end{bmatrix}&=[J]\begin{bmatrix}\Delta \delta \\\Delta V\end{bmatrix}\Leftrightarrow\begin{bmatrix}\Delta \delta \\\Delta V\end{bmatrix}=[J]^{-1}\begin{bmatrix}0 \\ \Delta Q\end{bmatrix} \\[12pt]
[\Delta Q]&=[J_{Q\delta}][\Delta \delta]+[J_{QV}][\Delta V] \\[12pt]
[\Delta \delta]&=-[J_{P\delta}]^{-1}[J_{PV}][\Delta V]
\end{align}$$
with the substitution the $[\Delta \delta]$ in (9), can be obtained
$$\begin{align}
[\Delta Q]&=([J_{QV}]-[J_{Q\delta}][J_{P\delta}]^{-1}[J_{PV}])[\Delta V] \\[12pt]
[\Delta V]&=[J_R]^{-1}[\Delta Q] \\[12pt]
[J_R]^{-1}&=(U\sum V)^{-1}=\sum^n_{i=1} \frac{1}{\sigma_i}[v_i][u_i]^T
\end{align}$$

In order to overcome the computational constraints, the Pseudo-inverse method can be introduced as optimization technique for non-square matrix [53]. This method is based on the SVD [51]. For this purpose, a numerical technique (Pseudo-inverse) is employed that is free of computational difficulties [54]. The Pseudo-inverse of matrix $\mathrm{\textbf{A}}(\mathbb{R}^{m \times n})$ is a matrix $\mathrm{\textbf{A}}^+(\mathbb{R}^{n \times m})$ that pursue the following affirmation:
$$
\mathrm{\textbf{A}}^+=(\mathrm{\textbf{A}}^T\mathrm{\textbf{A}})^{-1}\mathrm{\textbf{A}}^T
$$
Obviously, the $\mathrm{\textbf{A}}^T(\mathbb{R}^{n \times m})\cdot\mathrm{\textbf{A}}^T(\mathbb{R}^{m \times n})=\mathrm{\textbf{A}}^T\mathrm{\textbf{A}}$ matrixes defines a square matrix with these properties:
$$
\dots
$$
where the superscript ) signifies the conjugate transpose of the matrix. Li m ≥ n and A = UV, the Pseudo-inverse of A is
$$
\dots
$$
If $m < n$, in this case instead of $\mathrm{\textbf{A}}$, we consider the transpose of $\mathrm{\textbf{A}}$ to obtain the Pseudo-inverse.
$$
\dots
$$
There are substitutional expressions for power flow equations in terms of the Pseudo-inverse factorizations of Jacobian matrix. It has been found that, the proposed applied technique can influence the solvability of all probable conditions. From (13), variation of bus voltage related to change in injected reactive power and other involved parameters, can be summarized as voltage stability indicator, as given by
$$
[\Delta V]=\sum^n_{i=1}\frac{1}{\sigma_i}[v_i][u_i]^T[\Delta Q]
$$
The above indicator implies that the factorization of the load flow Jacobian, explains that the smallest value of $\sigma$ can be used as approximate index for describing the voltage stability in the power system. That the corresponding right and left singular vectors indicate sensitive bus voltages and angles, and sensitive direction for the changes in active and reactive power injections.

The inverse of the minimum singular value will indicate the greatest change in the state variables. The results were obtained using Neplan voltage stability function [55] considering these assumptions: the load flow was solved based on Extended Newton-Raphson (ENR) method. The length of the overhead conductors are kept constant (1.0 km).

Note: The vector quantities are denoted as bold or either show in square brackets.
#### Voltage stability indices comparative analysis
This susceptibility behavior of the power system leads the system to mismatch between generation and load. At long last, it gives rise to frequency deviation in the system. Herein the three techniques are studied, which are mostly based on reactive power deviation in the system. These techniques include the proposed voltage stability indicator (smallest eigenvalue with its associated eigenvectors), bus participation factor, and sensitivity analysis.

In [16, 56] denoted that in view of the voltage collapse mechanism, the bus participation factor can be used for recognition of weakest bus in the system. That the bus participation factors is employed as one of the indicators for identification of the weakest node in the system. Meanwhile, the associated right eigenvectors related to the smallest eigenvalue (the improved indicator) pursues the behavior at the same manner. So, the right eigenvectors of the smallest eigenvalue can be used for weak bus identification as well.

The comparative analysis in Figures 2.1 and 2.2, states the agreement of both techniques, in which the largest participation factor, as well as the largest right eigenvector at the least eigenvalues, indicate the most contribution of the bus to voltage unstable. Although sensitivity analysis is effective for weak bus identification [57, 58] in order to provide sufficient reactive power at the week bus to ensure the secure and reliable operation [59]. From dQ/dV sensitivity point of view; 14, 10, and 7 buses of 4-bus test system, and 26, 30, and 29 buses of 30-bus test system are the 3 top weak buses in the systems respectively. Whereas, from the proposed technique and previous research effort on the same test cases [39, 56], easily can be observed (Figures 2. 1 and 22) that the ranking of the 3 top weak buses are 14, 10, and 9 buses in 14-bus; and 30, 26, and 29 buses in 30-bus systems.

The greatest magnitudes for the indicators denote the weakest bus in the system. The Figure 2.1 demonstrates the S (Sensitivity (% Mvar)), BPF (Bus Participation Factor), and RE (Right Eigenvector) corresponding to the minimum eigenvalue ($\sigma_\mathrm{min}= 2.079206$) of the 14-bus system. The Figure

2.2 indicates the S, BPF, and RE values for 3 top weak buses (30, 26, and 29 buses respectively) corresponding to the minimum eigenvalue ($\sigma_\mathrm{min}=0.621337$) of the 30-bus system. The recognition of the 3 top weak buses for IEEE 14-bus, and 30-bus test systems (the simulation results are provided in Annex 2.1) , based on sensitivity analysis, bus participation factor and proposed right eigenvector indicators are compared in Table 2.1.
#### Chapter consequence
There are many other direct techniques beside of the Jacobian matrix method, to diminish the computation time and storage, but tend to fail, if system controls are considered [34]. However, the Jacobian matrix-based techniques have their demerit such: much computation cost and storage requirement, offline application, and lack of perception explicitly. Their merits are also significant from the view of an explicit model, and applicability purpose.

From (13), with considering the solution space and the dimensional subspace of the Jacobian matrix's rank; often, the aforesaid suppositions are not applicable and usually the load flow Jacobian matrix appears that either it is singular or non-square matrix. So in this case, directly the inverse is not exist [60], and under this condition the inverse of Jacobian matrix is known as a juncture for some load flow and voltage stability analysis methods. At the collapse point (saddle-node bifurcation point), the Jacobian matrix is singular at this critical point its eigenvalue is zero [50]. Although, the load flow Jacobian matrix can have a zero eigenvalue whereas the Jacobian matrix is nonsingular [35]. But the static reaction of the system (maximum power transfer point) can motivate the Jacobian matrix to become singular [33].

In order to provide the solution for over-determined system and minimal norm solutions for the under-determined systems according to the rank of A. There is possibility of two general conditions for non-square matrixes, $m \geq n$, and $m < n$. So that, this study investigates both possibility with connive of the previous studies computational restrictions. In order to avoid these constraints, the Pseudo-inverse method was applied as optimization technique for non-square matrix [53], which is based on the SVD [51].

Consequently, through employing the optimization numerical technique the Jacobian matrix would be invertible for all cases regardless the singularity and other constraints.

From (21) can be noted that the greatest right eigenvectors (RE) at the minimum eigenvalue indicates the weakest bus in the system. The magnitude of minimum eigenvalues presents how close the system is to voltage collapse point. If all eigenvalues are positive, then the system is considered to be stable [39]. Inversely, the negative eigenvalues (even if only one) indicates the voltage instability, and zero eigenvalue means that the system in on the border of voltage stability. When $\sigma_n<0$, the bus voltage variation in respect to the reactive power are opposite that indicate the unstable voltage [2].

From Section 2.4, can be recalled that the both indicators (the proposed (RE) and BPF) are completely agree on both test systems for the 3 top weak buses identification. However, the S indicator varies on both test systems for three ranking (Table 2.1). Therefore, it could be implied that the sensitivity assessment alone will not be sufficient for the purpose of weak bus identification (often in interconnected system), and the results (that obtain from reactive power deviation, especially near to the collapse point) are not in agreement with aforesaid techniques. The sensitivity analysis could be a useful tool when the system is suffered of heavily load in a stressed situation, in which the dV/dQ and dV/dP sensitivities play and important role in voltage collapse prediction [61].
### Chapter 3
#### Predicting voltage collapse index $\frac{V}{V_0}$
The simple $\frac{V}{V_0}$ index [83] is proposed; thus, voltage magnitude (V) is obtained from load flow for the operating point of the system. Where, V_0 (no load voltage) is known new values of voltage when the system all loads set to zero. Simply, this index ranking orders the critical buses in the system in respect to the voltage sensitivity. This index indicates an overall picture of the system stability state to determine the weak bus easily. The smallest index value indicates the most sensitive weak bus in the system. This index can be used for on-line and off-line applications. While, with respect to change in loading parameters, this index shows nonlinear profile. As, authors in [2, 67] argued that the $\frac{V}{V_0}$ index is poor in all three computational cost, accuracy of collapse point prediction and adequacy to nonlinearity performances.
#### Test function
References [2, 93] are proposed the test function index based on the quadratic shape of the proposed model. The test function index is more reliable than other Jacobian matrix-based method especially eigenvalue and singular value methods (more details are given in [2, 93]).
$$
t_\mathrm{lk}=\left\lvert e_\mathrm{l}^\mathrm{T}JJ_\mathrm{lk}^{-1}e_\mathrm{l} \right\rvert
$$
where, $J$ is the Jacobian matrix of the system, $e_\mathrm{l}$ is the $l^\mathrm{th}$ unit vector, i.e., a vector with all entries zero except the $l^\mathrm{th}$ row, and $J_\mathrm{lk}$ is defined by
$$
J_\mathrm{lk}=(I-e_\mathrm{l}e_\mathrm{l}^\mathrm{T})J+e_\mathrm{l}e_\mathrm{l}^\mathrm{T}
$$
By rearranging the Jacobian matrix with the $l^\mathrm{th}$ row removed and replaced by row $e_\mathrm{l}^\mathrm{T}$. If $l = k = c$, the function shows critical test function as expressed
$$
t_\mathrm{cc}=\left\lvert e_\mathrm{c}^\mathrm{T}JJ_\mathrm{cc}^{-1}e_\mathrm{c} \right\rvert
$$
It is found that the test function can be used to proximate the voltage collapse in a system, but it will not be able to identify the critical bus, since several buses should be monitored at the same time and that is time-consuming [2].
#### Second order index ($i$ Index)
Berizzi et al. [94] proposed a voltage stability index, which is named index $i$ (or second order index). This index is driven based on maximum singular value concept and its derivative. The aim behind this index is to overcome the deficiencies of the previous indices such as minimum singular Value index, which are inadequate in non-linearity condition. This index is considered in respect of the system total load and maximum singular value of the inverse Jacobian matrix changes. This index is introduced a useful tool in order to predict the distance to voltage collapse [94]. The range for this index is defined 1.0 at stable condition and zero, when the system tends to collapse.
$$
i=\frac{1}{i_0}\frac{\sigma_\mathrm{max}}{\frac{d\sigma_\mathrm{max}}{d\lambda_\mathrm{total}}}
$$
$\sigma_\mathrm{max}$ is the maximum singular value of the Jacobian inverse matrix,
$\lambda_\mathrm{total}$ is the system total load,
$i_0$ is the value of $\frac{\sigma_\mathrm{max}}{\frac{d\sigma_\mathrm{max}}{d\lambda_\mathrm{total}}}$ at the initial operating point.
#### Tangent Vector Index ($TVI_i$)
Zambroni de Souza [105] derived the tangent vector index, which is on the load change and corresponding tangent vector concept. This index directly measure the effect of load changes on the vector elements such bus voltage magnitudes and angels. Therefore, it can be counted as good approach to assess how far away the system is operating from the collapse point. This index is given by
$$
TVI_i=\left\lvert \frac{dV_i}{d\lambda} \right\rvert ^{-1}
$$
$V_i$ is the voltage at bus $i$, $\lambda$ is the load. When the value of the derivative tends to infinity, then $TVI_i \rightarrow 0$.
#### Smallest Eigenvalue
Gao et al. [16] introduced the model analysis-based indices, which the smallest eigenvalue associated with right eigenvectors, is one of these techniques as expressed:
$$
\Delta V=\sum_i \frac{\xi_i\eta_i}{\lambda_i} \Delta Q
$$
The above equation obviously show the relationship between involved parameters, in which the changes in reactive power, eigenvalue and eigenvectors have directly effect on $\Delta V$.

$\Delta V$ indicates the deviation in voltage magnitudes
$\Delta Q$ indicates the deviation in injected reactive power
$\xi_i$ is the $i^\mathrm{th}$ column right eigenvector
$\eta_i$ is the $i^\mathrm{th}$ row left eigenvector of Reduced Jacobian matrix 
$\lambda$ is the diagonal eigenvalue matrix of Reduced Jacobian matrix

A system is voltage stable if the eigenvalues of the Jacobian are all positive and an eigenvalue with positive real part indicates that the system is unstable.
#### Singular Value Indicator
Lof et al. [36] proposed a static voltage stability index that is based on a singular value decomposition of power flow Jacobian matrix. The aim of this index is to proximate the voltage instability to collapse and identifies the critical nodes in the system. Supposed that the matrix A is and n x n quadratic (real) matrix.
$$
\mathrm{\textbf{A}}=\mathrm{\textbf{U}}\sum\mathrm{\textbf{V}}^T=\sum^n_{i=1} \sigma_iu_iv_i^T
$$
$\mathrm{\textbf{U}}$ and $\mathrm{\textbf{V}}$ are $n \times n$ orthonormal matrices
$v_i$ and $u_i$ are singular vector and the columns of the $\mathrm{\textbf{U}}$ and $\mathrm{\textbf{V}}$ matrices 
$\sum$ is a diagonal matrix with
$$
\sum(\mathrm{\textbf{A}})=\mathrm{diag}[\sigma_i(\mathrm{\textbf{A}})]
$$
$i = 1,2,\dots,n$; where $\sigma_i \geq 0$ for all $i$. The order of the diagonal matrix is $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n \geq 0$. With considering the power flow Jacobian matrix the result is yielded
$$\begin{align}
\begin{bmatrix}\Delta \theta \\ \Delta V \end{bmatrix}=\mathrm{\textbf{V}}{\sum}^{-1}\mathrm{\textbf{U}}^T
\begin{bmatrix}\Delta F \\ \Delta G\end{bmatrix}
\end{align}$$
From singular value decomposition of the power flow Jacobian matrix these point are observed:
1. The smallest singular value ($\sigma_n$) can be used as steady-state stability limit indicator
2. The right singular vector ($v_n$) corresponding to smallest singular value ($\sigma_n$) indicated sensitive voltages and angles;
3. The left singular vector ($u_n$) corresponding to smallest singular value ($\sigma_n$) indicated the most sensitive direction for changes of the active and reactive power injections.
#### Impedance Ratio Indicator
Cheboo et al. [12] introduced the impedance ration as a voltage collapse proximity indicator. This index is driven from 2-bus system (Figure 3.15) by employing the Thevenin theorem, as given by
$$\begin{align}
\frac{Z_{ii}}{Z_i} &\leq 1 \\[6pt]
Z_{ii}\angle\beta_i&=i^\mathrm{th} \quad \text{diagonal element of } [\mathrm{\textbf{Z}}]\\[6pt]
[\mathrm{\textbf{Z}}] &= [\mathrm{\textbf{Y}}]^{-1}
\end{align}$$
The aim of this indicator is said, the assessment of the validity and robustness of the indicator over the operating range.

$Z_{ii}\angle\beta_i$ is the Thevenin's equivalent impedance
$Z_{i}\angle\phi_i$ is the impedance of the load

In addition, useful information regarding the critical threshold values are formulated in this paper as follows (details are given in [12, 74]):
$$\begin{align}
P_\mathrm{crit}&=\frac{V_\mathrm{s}^2}{Z_\mathrm{s}}\frac{\cos \varnothing}{4\cos^2(\beta-\varnothing)/2} \\[6pt]
Q_\mathrm{crit}&=\frac{V_\mathrm{s}^2}{Z_\mathrm{s}}\frac{\sin \varnothing}{4\cos^2(\beta-\varnothing)/2} \\[6pt]
V_\mathrm{crit}&=\frac{V_\mathrm{s}}{2\cos\frac{\beta-\varnothing}{2}}
\end{align}$$
where, $V_\mathrm{s}$ is constant voltage source (sending end), $Z_\mathrm{s}\angle\beta$ is the internal impedance of the network, and $\varnothing$ is the phase angle of the load impedance.
### References
[1] Liscouski, B., and W. Elliot. "Final report on the august 14, 2003 blackout in the united states and Canada: Causes and recommendations." A report to US Department of Energy 40, no. 4 (2004).

[2] Doig Cardet, Christine Elizabeth. "Analysis on Voltage Stability Indices."

[3] Steinmetz, Charles P. "Power control and stability of electric generating stations." American Institute of Electrical Engineers, Transactions of the 39, no. 2(1920): 1215-1287.

[4] Kundur, Prabha, John Paserba, Venkat Ajjarapu, Göran Andersson, Anjan Bose, Claudio Canizares, Nikos Hatziargyriou et al. "Definition and classification of power system stability IEEE/CIGRE joint task force on stability terms and definitions." Power Systems, IEEE Transactions on 19, no. 3 2004): 1387-1401. 

[5] Kundur, Prabha. Power system stability and control. Edited by Neal J. Balu, and Mark G. Lauby. Vol. 7. New York: McGraw-hill, 1994.

[6] Nakawiro, Worawat, and István Erlich. "Online voltage stability monitoring using artificial neural network." In Electric Utility Deregulation and Restructuring and Power Technologies, 2008. DRPT 2008. Third International Conference on, pp. 941-947. IEEE, 2008.

[7] Power system security: web-based design tools. http://seniord.ece.iastate.edu/may0323/voltage_stab_def.html (accessed April, 2014).

[8] Kearsley, Roger. "Restoration in Sweden and experience gained from the blackout of 1983." Power Systems, IEBE Transactions on 2, no. 2 (1987): 422-428.

[9] Ohno, T., and S. Imai. "The 1987 tokyo blackout." In Power Systems Conference and Exposition, 2006. PSCE:06. 2006 BEE PES, pp. 314-318. IEEE, 2006.

[10] Kurta, Atsushi, and T. Sakurai. "The power system failure on July 23, 1987 in Tokyo." In Decision and Control, 1988. Proceedings of the 27th IBEE Conference on, pp. 2093-2097. IEEE, 1988.

[11] Machowski, Jan, Janusz Bialek, and Jim Bumby. Power system dynamics: stability and control. John Wiley & Sons, 2011.

[12] Chebbo, A. M., M. R. Irving, and M. J. H. Sterling. "Voltage collapse proximity indicator: behaviour and implications." In TEE Proceedings C (Generation, Transmission and Distribution), vol. 139, no. 3, pp. 241-252. IEE, 1992.

[13] Kessel, P., and H. Glavitsch. "Estimating the voltage stability of a power system." Power Delivery, IEEE Transactions on 1, no. 3 (1986): 346-354.

[14] Tamura, Y., H. Mori, and S. Iwamoto. "Relationship between voltage instability and multiple load flow solutions in electric power systems." Power Apparatus and Systems, IEEE Transactions on 5 (1983): 1115-1125.

[15] Kwatny, Harry G., A. Pasrija, and L. Bahar. "Static bifurcations in electric power networks: loss of steady-state stability and voltage collapse." Circuits and Systems, IEEE Transactions on 33, no. 10 (1986): 981-991.

[16] Gao, Baofu, G. K. Morison, and Prabhashankar Kundur. "Voltage stability evaluation using modal analysis." Power Systems, IEEE

[17] Transactions on 7, no. 4 (1992): 1529-1542. Electric Power Research Institute Technical Report, EPRI Power

[18] Systems Dynamics Tutorial. EPRI, Palo Alto, CA: 2009. 1016042. Chakrabarti, Abhijit, et al. An introduction to reactive power control and voltage stability in power transmission systems. PHI Learning Pvt. Ltd., 2010.

[19] FGL's 3 bus Test System. hp://fglongat.org/OLD/Test_Case_FGL's%203%20bus.html (accessed February, 2014).

[20] ﻿Mansour, Yakout, Wilsun Xu, Fernando Alvarado, and Chhewang Rinzin. "SVC placement using critical modes of voltage instability." Power Systems, IEEE Transactions on 9, no. 2 (1994): 757-763.

[21] ﻿﻿﻿﻿﻿Taylor, Carson W. Power system voltage stability. McGraw-Hill, 1994.

[22] Momoh, James A., and Mohamed E. El-Hawary. Electric systems, dynamics, and stability with artificial intelligence applications. CRC  
Press, 1999.

[23] Hill, David J., MK PAL, XU WILSUN, YAKOUT MANSOUR, CO NWANKPA, L. Xu, and R. Fischl. 'Nonlinear dynamic load models with recovery for voltage stability studies. Discussion. Authors' response." IEEE Transactions on Power Systems 8, no. 1 (1993): 166-176.

[24] Ajjarapu, Venkataramana. Computational techniques for voltage stability assessment and control. Springer, 2007.

[25] Li, Wenyuan. Probabilistic transmission system planning. Vol. 65. John Wiley & Sons, 2011.

[26] Danish, Mir Sayed Shah, Atsushi Yona, and Tomonobu Senjyu.  
"Voltage stability assessment index for recognition of proper bus for load shedding. "Information Science, Electronics and Electrical Engineering (ISEEE), 2014 International Conference on, vol. 1, pp. 636-639. IEEE, 2014.

[27] Milkovic, Sladjana, Marko Miladinovic, Predrag Stanimirovic, and Igor Stojanovic. "Application of the pseudoinverse computation in reconstruction of blurred images." Filomat 26, no. 3 (2012): 453-465.

[28] Calderon-Guizar, J. G., and E. F. Noriega. "Speeding up the computations of the minimum singular value of the load flow Jacobian matrix." Power Engineering Review, IEEE 19, no. 9 (1999): 55-56.

[29] Chang, Po Rong, and C. S. G. Lee. "Residue arithmetic VLS array architecture for manipulator pseudo-inverse Jacobian computation." Robotics and Automation, IEEE Transactions on 5, no. 5 (1989): 569-582.

[30] Prada, R. B., and J. O. R. Dos Santos. "Fast nodal assessment of static voltage stability including contingency analysis." Electric power

# Citation
> Danish, M. S. S. (2015). _Voltage stability in electric power system: A practical introduction_. Logos-Verl.
# Further Tags
