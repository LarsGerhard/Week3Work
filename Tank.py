# Necessary Imports
from numpy import linspace, sqrt
from scipy.constants import g
from scipy.optimize import brentq
from scipy.integrate import odeint
from matplotlib.pyplot import plot, show

# Initial Variables (in mKS units)
D0 = 1
h0 = 2
d = 0.02
hf = 0.05
hSpace = linspace(0, h0, 100)


def main():
    # Plots parabolic curve to verify that it meets the boundary conditions
    plot(hSpace, Diameter(hSpace))
    show()
    # Creating our bounds using the analytic solution
    t1 = tanalytic(D0, hf)
    t2 = tanalytic(1.1 * D0, hf)
    # Using our functions and bounds to find the drain time (in seconds)
    print(brentq(height_diff, t1, t2))


# Diameter Function
def Diameter(h):
    # To get the curve we want we shift our parabola over by h0/2, put our vertex at 1.1D0, and multiply our curve by
    # a constant that equals 0.1 D0 at 0 and h0
    D = 1.1 * D0 - (0.4 * D0 / h0 ** 2) * (h - h0 / 2) ** 2
    return D


# Our differential equation
def rate(t, h):
    dhdt = - sqrt(2 * g) * (d ** 2 / Diameter(h) ** 2) * sqrt(h)
    return dhdt


# Function for calculating the difference between the height at a time and our final height
def height_diff(t):
    # Uses odeint to solve above diffeq, stores result as a tuple with time and height
    diffTup = odeint(rate, h0, [0, t], tfirst=True)
    # Only want the height, so this takes the height value as a float and subtracts the final height
    diff = float(diffTup[1]) - hf
    return diff


# Our analytic solution, assuming no bulge. Used for finding bounds
def tanalytic(D, h):
    t = ((D ** 2 * sqrt(2)) * (sqrt(h0) - sqrt(h))) / (d ** 2 * sqrt(g))
    return t


# Main function. Runs the whole thing
main()
