import numpy as np
class ActivateFunction:
    
    def sigmoid(self,x):
        return (1/(1+(np.e) ** (-x)))
    
    def relu(self, x):
        if x < 0:
            return 0
        return x
    
    def identity(self, x):
        return x