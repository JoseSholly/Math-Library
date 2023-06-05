import math
from sympy import *
x, y = symbols('x y')

"""
The Secant method approximates the root of a function by constructing a line through 
two points on the function curve and determining where it intersects the x-axis. 
It does not require the computation of derivatives like the Newton-Raphson method, 
making it applicable in cases where the derivative is either difficult or expensive to compute.

The convergence of the Secant method is generally slower than the Newton-Raphson method but faster than the Bisection method. 
It performs well when the initial guesses are close to the root and the function is well-behaved. 
However, it may fail to converge or converge slowly for certain functions or when the initial guesses are not sufficiently 
close to the root.
"""


def interval(equation):
    # Finding Interval
    equation = sympify(equation)
    L1, L2 = [], []
    for i in range(0, 10):
        ans = equation.subs({x: f"{i}"})
        if ans < 0:
            L1 += [i]

    for i in range(0, 10):
        ans = equation.subs({x: f"{i}"})
        if ans > 0:
            L2 += [i]
    
    if L2[0]>L1[-1]:
        return (L1[-1], L2[0])
    else:
        return (L2[-1], L1[0] )


def is_continuous(equation):
    # For any continuous function

    v1 = interval(equation)[0]
    v2 = interval(equation)[1]

    # Substititing intervals into function
    fxa = equation.subs({"x": v1})
    fxb = equation.subs({"x": v2})

    # Find two points, say a and b such that a<b and f(a)*f(b)=0
    if v1 < v2 and (fxa*fxb) < 0:
        return True
    else:
        return False


def secant(equation, E=0.0001):
    # Input the function f(x) and the desired tolerance= E
    # Checks if the equation is continuous, then proceeds to calcu;ate
    if is_continuous(equation):
        try:

            # Find the value of f(x) at a=1 and a=2
            a = interval(equation)[0]
            b = interval(equation)[1]
            # the initial guesses x0 and x1
            x0, x1 = a, b
            equation = sympify(equation)
            
            root = 0.1
            i = 0
            
            Xo, fx_Xo, X1, fx_X1, X2, fx_X2 = [], [], [], [], [], []

            while abs(root)>E and i <= 7:
                i += 1
                #  Substituting interval values into input equation
                fxa = round(equation.subs({x: x0}), 5)
                fxb = round(equation.subs({x: x1}), 5)
                #  Rounding answer to 5 decimal place
                x0= round(x0, 5)
                x1= round(x1, 5)


                # We have different formular but we still have same x2 value 
                # x2 = (x0-fxa) * ((x1-x0)/(fxb-fxa))
                x2 = ((x0*fxb) - (x1*fxa))/(fxb-fxa)

                #  Substituting mid-point into f(x)-equation
                root = equation.subs({x: x2}).n(5)
                xp, xpp= x0, x1

                #  if f(x2)= 0 then x2= root, else xo= x1, x1=x2
                # We repeat till f(x)= 0 or |f(x)|<=Tolerance
                if root!=0:
                    x0= x1
                    x1= x2
                else:
                    break
                # Appending answers into list 
                Xo+=[xp]
                fx_Xo+=[fxa]

                X1+=[xpp]
                fx_X1+=[fxb]

                X2+=[x2]
                fx_X2+=[root]
                
            # Output the approximate root x obtained after the desired number of iterations or within the desired tolerance.
            dict_answer={"xo": Xo, "f(Xo)":fx_Xo, "x1":X1, "f(x1)":fx_X1, "x2": X2, "f(x2)": fx_X2, "root":X2[-1], "iteration": len(X1)}
            return dict_answer
        except:        
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")


#  Examples

# print(secant(x**3-x-1))

# print(secant(((2*x**2)-3)))

# print(secant(2*x**3 - 2*x - 5))

# print(secant(x**2 - 12))

# print(secant(x**3-48))

# print(secant(x**3 + 2*x**2 + x -1))

# print(secant(2 + sin(x) - x ))

