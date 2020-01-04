import torch
import torch.nn as nn
import torch.optim as optim




class AdaSqrt(optim.Optimizer):
    """
    Implementation of AdaSqrt optimizer described in https://arxiv.org/pdf/1912.09926.pdf. 

    Update rule
    
    alpha(t) = sqrt(t)
    S(t) = S(t-1) + gradients(theta(t-1))^2
    tetha(i) = theta(i-1) - lr * d(i)
    theta(t) = theta(i-1) - lr * alpha(t) * gradient(theta(t))/(S(t) + eps)

    Parameters
    ----------
    paramaters (iterable):
        The model parameters to be optimized.
    lr  (float, optional):
        Learing rate hyperparamater (default: 1e-3)

    """

    def __init__(self, paramaters, lr=1e-3):

        assert lr>=0.0, "Learning rate should be non negative"
        defaults = dict(lr=lr)
        super(AdaSqrt, self).__init__(paramaters, defaults)
        self.eps = 1e-8
        
    def step(self, closure=None):
        """
        Performas a single optimization step.

        Parameters
        ----------
        closure (callable, optional):
            closure to calculate loss of a model

        Returns
        -------
        torch.tensor
            Loss of model when reevaluated using closure

        """
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
                    state["st"] = torch.zeros_like(dp)
                    state["t"] = torch.tensor(0.0)

                state["st"].data.add_(torch.sum(dp**2))
                state["t"].data.add_(1.0)

                alph_t = torch.sqrt(state["t"])
                step = (alph_t * dp ) / (state["st"] + self.eps)
                p.data.add_(-group["lr"], step)
        return loss