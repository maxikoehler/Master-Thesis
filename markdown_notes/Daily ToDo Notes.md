---
tags:
  - open
Date: 2024-10-21
---
## Programming
- [ ] **Modeling of operational units**
	- [ ] Transformer
		- [x] Distinguish between old, CIM and AM model
		- [x] Add Transformer class
		- [x] Estimate needed functions and describe them
		- [x] Programming functions
		- [ ] Add OLTC
		      -> FSM that much more? Should be another controller then...
		- [x] Standardize with abstract class modeling
		      -> super().method() working? Some variables just have to be updated then...
		- [ ] Controller
	- [ ] Loads
		- [ ] Frequency and Voltage dependent 
	- [ ] Simplifications
		- [ ] I can specify the axis or value description in the recorder; helping for plotting, gui, etc.

- [ ] **GUI** necessary / interesting?
	- [ ] Using a GUI for ```diffpssi``` simulation?
	- [ ] Defining interfaces, for returning the desired Grid Data?

- [ ] How implementing **system stability assessment**?
	- [ ] Extra classes or files with dedicated methods
	- [ ] Online assessment and post-identification based on simulation results?
	- [ ] Only voltage stability interesting or others as well?

- [ ] **GIT**
	- [ ] auto documentation somehow possible on GitLab?

## Literature
- [ ] Research on voltage stability; dynamic as well
- [ ] Literature on control theory; -> Bifurcations, chaos theory for control?
      -> other students: fuzzy control, continous control method in MATLAB / Simulink (but EMT , not RMS simulation)