class InductionMachine(object):
    """
    Represents an Induction Machine in power system simulations.

    The IMdynamic class models an induction motor or generator, including its dynamic behavior and
    interactions with external control systems such as voltage and frequency controllers.

    Attributes:
        s_n, v_n, p_soll_mw, v_soll, h, d, r_s, r_r, x_s, x_r, x_m, t_r0:
            Parameters defining the electrical and mechanical characteristics of the machine.
    """

    def __init__(self, f_n_sys, s_n_sys, v_n_sys, mode='dynamic',
                 param_dict=None,
                 name=None,
                 bus=None,
                 s_n=None,
                 v_n=None,
                 p=None,
                 v=None,
                 h=None,
                 d=None,
                 r_s=None,
                 r_r=None,
                 x_s=None,
                 x_r=None,
                 x_m=None,
                 t_r0=None,
                 ):
        """
        Initializes the IMdynamic object with specified parameters.

        Args:
            param_dict (dict, optional): A dictionary of parameters for the machine.
            name (str, optional): The name of the machine.
            bus (Bus, optional): The bus the machine is connected to.
            s_n (float, optional): The apparent power rating of the machine in MVA.
            v_n (float, optional): The rated voltage of the machine in kV.
            p (float, optional): The active power of the machine in MW.
            v (float, optional): The voltage of the machine in per unit.
            h (float, optional): The inertia constant of the machine in seconds.
            d (float, optional): The damping coefficient of the machine in pu.
            r_s (float, optional): The stator resistance of the machine in pu.
            r_r (float, optional): The rotor resistance of the machine in pu.
            x_s (float, optional): The stator reactance of the machine in pu.
            x_r (float, optional): The rotor reactance of the machine in pu.
            x_m (float, optional): The magnetizing reactance of the machine in pu.
            t_r0 (float, optional): The rotor time constant of the machine in seconds.
        """
        if param_dict is None:
            param_dict = {
                'name': name,
                'bus': bus,
                'S_n': s_n,
                'V_n': v_n,
                'P': p,
                'V': v,
                'H': h,
                'D': d,
                'R_s': r_s,
                'R_r': r_r,
                'X_s': x_s,
                'X_r': x_r,
                'X_m': x_m,
                'T_r0': t_r0,
            }

        self.parallel_sims = None

        self.name = param_dict['name']
        self.bus = param_dict['bus']
        self.s_n = param_dict['S_n']
        self.v_n = param_dict['V_n']
        self.p_soll_mw = param_dict['P']
        self.v_soll = param_dict['V']
        self.h = param_dict['H']
        self.d = param_dict['D']
        self.r_s = param_dict['R_s']
        self.r_r = param_dict['R_r']
        self.x_s = param_dict['X_s']
        self.x_r = param_dict['X_r']
        self.x_m = param_dict['X_m']
        self.t_r0 = param_dict['T_r0']
        self.mode = mode

        # initialize system vars
        self.fn = f_n_sys
        self.s_n_sys = s_n_sys
        self.v_n_sys = v_n_sys

        # initialize states
        if self.mode == 'dynamic':
            self.omega = 0
            self.delta = 0
            self.i_s_d = 0
            self.i_s_q = 0
            self.i_r_d = 0
            self.i_r_q = 0

        # initialize internal variables
        self.p_m = 0
        self.p_e = 0
        self.v_bb = 0

    def differential(self):
        """
        Computes the differential equations governing the dynamics of the induction machine.

        Returns:
            torch.Tensor: A tensor containing the derivatives of the state variables.
        """
        if self.mode == 'dynamic':
            t_m = self.p_m / (1 + self.omega)
            d_omega = 1 / (2 * self.h) * (t_m - self.p_e - self.d * self.omega)
            d_delta = self.omega * 2 * torch.pi * self.fn
            d_i_s_d = (self.v_bb.real - self.r_s * self.i_s_d + self.omega * self.x_s * self.i_s_q) / self.x_s
            d_i_s_q = (self.v_bb.imag - self.r_s * self.i_s_q - self.omega * self.x_s * self.i_s_d) / self.x_s
            d_i_r_d = (-self.r_r * self.i_r_d + self.omega * self.x_r * self.i_r_q) / self.x_r
            d_i_r_q = (-self.r_r * self.i_r_q - self.omega * self.x_r * self.i_r_d) / self.x_r

            deriv_vec = torch.stack([d_omega, d_delta, d_i_s_d, d_i_s_q, d_i_r_d, d_i_r_q], axis=1)
            return deriv_vec
        elif self.mode == 'static':
            pass
            # return torch.zeros((self.parallel_sims, 6), dtype=torch.complex128)

    def set_state_vector(self, x):
        """
        Sets the state vector of the induction machine based on provided values.

        Args:
            x (torch.Tensor): A tensor representing the new state vector.
        """
        if self.mode == 'dynamic':
            self.omega = x[:, 0]
            self.delta = x[:, 1]
            self.i_s_d = x[:, 2]
            self.i_s_q = x[:, 3]
            self.i_r_d = x[:, 4]
            self.i_r_q = x[:, 5]

    def get_state_vector(self):
        """
        Retrieves the current state vector of the induction machine.

        Returns:
            torch.Tensor: The current state vector of the machine.
        """
        if self.mode == 'dynamic':
            state_vec = torch.stack([self.omega, self.delta, self.i_s_d, self.i_s_q, self.i_r_d, self.i_r_q], axis=1)
            return state_vec
        elif self.mode == 'static':
            pass

    def calc_current_injections(self):
        """
        Calculates the current injections from the induction machine into the network.

        Returns:
            torch.Tensor: A tensor representing the current injections at the machine's terminals.
        """
        if self.mode == 'dynamic':
            i_inj = (self.i_s_d + 1j * self.i_s_q) * (self.s_n / self.s_n_sys)
            return i_inj
        elif self.mode == 'static':
            pass

    def update_internal_vars(self, v_bb):
        """
        Updates internal variables of the induction machine based on the voltage at the busbar.

        Args:
            v_bb (float or torch.Tensor): Voltage at the busbar.
        """
        self.v_bb = v_bb

        if self.mode == 'dynamic':
            e_st = self.i_s_d * torch.exp(1j * self.delta) + self.i_s_q * torch.exp(1j * (self.delta - torch.pi / 2))
            self.p_e = (v_bb * torch.conj((e_st - v_bb) / (1j * self.x_s))).real
            i_gen = (e_st - v_bb) / (1j * self.x_s)
            self.i_s_d = (i_gen * torch.exp(1j * (torch.pi / 2 - self.delta))).real
            self.i_s_q = (i_gen * torch.exp(1j * (torch.pi / 2 - self.delta))).imag

    def initialize(self, s_calc, v_bb):
        """
        Initializes the induction machine's states based on provided conditions.

        Args:
            s_calc (float or torch.Tensor): Calculated apparent power.
            v_bb (float or torch.Tensor): Voltage at the busbar.
        """
        i_gen = torch.conj(s_calc / v_bb) / (self.s_n / self.s_n_sys)
        e = v_bb + 1j * self.x_m * i_gen

        self.delta = torch.angle(e)
        self.omega = torch.zeros_like(self.delta)

        i_dq = i_gen * torch.exp(1j * (torch.pi / 2 - self.delta))
        self.i_s_d = i_dq.real
        self.i_s_q = i_dq.imag

        self.p_m = s_calc.real / (self.s_n / self.s_n_sys)

    def get_admittance(self, dyn):
        """
        Returns the admittance value of the induction machine.

        Args:
            dyn (bool): Flag indicating whether to calculate dynamic (True) or static (False) admittance.

        Returns:
            torch.Tensor: Admittance of the induction machine.
        """
        if dyn:
            return -1j / self.x_s * (self.s_n / self.s_n_sys)
        else:
            return torch.zeros((self.parallel_sims, 1), dtype=torch.complex128)

    def get_lf_power(self):
        """
        Retrieves the load flow power of the induction machine.

        Returns:
            torch.Tensor: The load flow power.
        """
        return (self.p_soll_mw + 1j * 0) / self.s_n_sys

    def enable_parallel_simulation(self, parallel_sims):
        """
        Enables running parallel simulations for the induction machine by converting parameters to tensors

        Args:
            parallel_sims (int): Number of parallel simulations.
        """
        self.parallel_sims = parallel_sims

        self.s_n = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.s_n
        self.v_n = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.v_n
        self.p_soll_mw = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.p_soll_mw
        self.v_soll = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.v_soll

        self.h = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.h
        self.d = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.d
        self.r_s = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.r_s
        self.r_r = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.r_r
        self.x_s = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.x_s
        self.x_r = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.x_r
        self.x_m = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.x_m
        self.t_r0 = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.t_r0

        self.omega = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.omega
        self.delta = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.delta
        self.i_s_d = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.i_s_d
        self.i_s_q = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.i_s_q
        self.i_r_d = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.i_r_d
        self.i_r_q = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.i_r_q

        self.p_m = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.p_m
        self.p_e = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.p_e
        self.v_bb = torch.ones((parallel_sims, 1), dtype=torch.complex128) * self.v_bb