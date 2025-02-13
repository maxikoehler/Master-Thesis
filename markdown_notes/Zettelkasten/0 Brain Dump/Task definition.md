## Title
> *"Modeling of transformers with on-load tap-changers (OLTC) in Python"*

## Familiarization
- RMS Simulation in Python
- PowerFactory as validation
<br>
- literature research for:
	- voltage stability; indices, stability determination methods static AND dynamically
	- relevant grid mechanisms leading to voltage instability
	- transformer ratios, rotation, power angle manipulation?, influence on admittance matrix
	- dynamic behavior of transformers? -> loading / capacity / inductance of windings

## Fundamentals
-	Transformer modelling
	- Load flow equations
	- Influence of OLTCs on the voltages
	- Influence of angle rotation, due to the wiring of a transformer (Ynd5 vs. Yny0)

## ToDos and minimal
1. Voltage stability/instability
	- P-V-curves
	- Jacobi Matrix
	- Influence of OLTC

This part can be done purely analytically. The influence of the OLTC is very well described for stationary systems.
Literature research: How can voltage stability be described for dynamic systems? Bifurcation? Focus here on the influence of the transformer.

2. Installation of the transformer + OLTC control in the RMS-Python tool
	- Definition of scenarios
		- LVRT
		- HVRT
		- load application
3. Transformer controls (discrete vs. continuous)
	- Discrete control as the normal way is relatively easy to realize
	- Continuous control: Here, stage positions are not discrete. Advantage: OLTC control can be used for eigenvalue analyses (small signal stability).
4. Simulations
	- Comparison discrete vs continous control
	- Simulative proof of the analytically calculated limits of voltage stability/ instability (stationary)
	- Simulative proof of the dynamic limitations (dependent on literature research)

## Additional
- Installation of the FSM-OLTC controller and test
- Determination of small signal stability?


**General idea:**

> How does the control of Tap Changing transformers influence the voltage stability?

Therefore following questions/steps can be imagined as supportive?:
1. How can Voltage stability of a system be classified and be looked at? Which indices, measurements, etc.
2. Which transformer model has to be considered to show influences?
3. Which additional load models, source models, transmission model have to be modeled for an adequate assessment?
4. Which systems are useful to consider in showing effects? Which circumstances lead to a stability support, which to a decrease? Where can limits be shown? 

Useful and mandatory [[Limitations of the Thesis]] and restrictions are worked out during the familarization.
