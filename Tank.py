# Necessary Imports
from numpy import linspace, sqrt
from scipy.constants import g
from scipy.optimize import brentq
from scipy.integrate import odeint
from matplotlib.pyplot import plot, show

# Initial Variables (in MKS units)
D0 = 1
h0 = 2
d = 0.02
tSpace = linspace(0, 1900, 10000)
hf = 0.05

def main():
    t1 = tanalytic(D0,h0)
    t2 = tanalytic(1.1 * D0, h0)
    print(height_diff(1931))
    print(height_diff(1596))
    print(brentq(height_diff,height_diff(t1),height_diff(t2)))
    # show()

# Diameter Function
def Diameter(h):
    # To get the curve we want we shift our parabola over by h0/2, put our vertex at 1.1D0, and multiply our curve by a constant that equals 0.1 D0 at 0 and h0
    D = 1.1 * D0 - (0.4 * D0 / h0**2) * (h - h0 / 2)**2
    return D

def rate(t,h):
    dhdt = - sqrt(g / 2) * (d**2 / Diameter(h)**2) * sqrt(h)
    return dhdt

def height_diff(t):
    diffTup = odeint(rate, h0, [0, t],  tfirst=True)
    diff = float(diffTup[1])
    return diff

def tanalytic(D,h):
    t = ((D**2 * sqrt(2)) * (sqrt(h0) + sqrt(h))) / (d**2 * sqrt(g))
    return t


main()
