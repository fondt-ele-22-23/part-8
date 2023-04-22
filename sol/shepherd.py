import numpy as np

class Shepherd:
    def __init__(self, r, N=1):
        self.r = r
        self.N = N
    
    def __call__(self, x, k):
        r, N = self.r, self.N # Rinomino per compattezza
        xnext = r * x / (1 + (x / N)**2)
        return xnext
    
