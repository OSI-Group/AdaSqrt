import torch
import torch.nn as nn
import torch.optim as optim




class MomentumOptimizer(optim.Optimizer):
    def __init__(self, paramaters, beta=0.9, lr=1e-3):
        assert lr>=0.0, "Learning rate should be non negative"
        defaults = dict(lr=lr, beta=beta)
        super(MomentumOptimizer, self).__init__(paramaters, defaults)
        
    def step(self, closure=None):
        loss = None
        if closure is not None:
            loss = closure()
        for group in self.param_groups:
            for p in group["params"]:
                if p.grad is None:
                    continue
                
                dp = p.grad.data

                state = self.state[p]
                if len(state)==0:
                    state["vt"] = torch.zeros_like(dp)
                state["vt"].data = group["beta"] * state["vt"] + group["lr"] * dp

                p.data.add_(-state["vt"])
        return loss

# class NAGOptimizer(optim.Optimizer):
#     def __init__(self, parameters, gamma = 0.9, lr = 1e-3):
#         defaults = dict(lr=lr, gamma=gamma)
#         super(NAGOptimizer, self).__init__(parameters, defaults)
#     def step(self, closure = None):
#         loss = None
#         if closure is not None:
#             loss = closure()
    
#         for group in self.param_groups:
#             for p in group["params"]:
#                 if p.grad is None:
#                     continue
                
#                 dp = p.grad.data

#                 state = self.state[p]
#                 if len(state)==0:
#                     state["dp"] = torch.zeros_like(dp)
#                     state["di"] = torch.zeros_like(dp)
#                 di  = group["gamma"] * state["di"] + state["dp"] + group["gamma"] * (state["dp"] - step["dp"]
#                 state["vt"].data = group["beta"] * state["vt"] + group["lr"] * dp

#                 p.data.add_(-state["vt"])

#         return loss


