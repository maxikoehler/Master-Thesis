def get_output(self, vbb=None):
    if vbb is None: 
        try:
            # get current bus bar voltage
            vbb = self.trafo.to_voltage
        except:
            raise ValueError('No access to instantaneous bus voltage.')
    
    self.v_diff = (torch.abs(vbb) - torch.abs(self.v_ref)) * torch.ones((self.parallel_sims, 1), dtype=torch.float64)
    
    v_dead_prev = self.v_dead
    
    self.v_dead = self.deadband.get_output(self.v_diff)

    # reset the integrator, if the v_diff falls under the deadband (could as well be == 0)
    # OR if the sign suddenly changing
    if torch.abs(self.v_dead) == torch.zeros_like(self.v_dead):
        self.integrator.reset()
    elif torch.sign(self.v_dead) != torch.sign(v_dead_prev):
        self.integrator.reset()
        
    self.integ = self.integrator.get_output(torch.abs(torch.sign(self.v_diff))) # or v_dead/self.v_diff for variable gain
    
    if (self.integ > self.t_1):
        # reset the integrator after the switching operation mandatory for remaining operatbility of t_1 s window
        # if the deadband is continously overstepped for more than t_1 s, switching operation is triggered
        self.m = self.switching(self.v_diff)
        self.integrator.reset()
        self.u_l += self.delta_m * self.m

    return self.u_l