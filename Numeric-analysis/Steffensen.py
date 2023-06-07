import math
from sympy import *
x, y = symbols('x y')

'''
The Steffensen's method uses the fixed-point iteration technique to approximate the root of a function. 
It improves the rate of convergence by applying the fixed-point iteration twice in each iteration step. 
By using this accelerated iterative approach, it can achieve faster convergence than standard fixed-point iteration methods.

It's important to note that like other iterative methods, the Steffensen's method may not converge 
or converge slowly for certain functions or when the initial guess is far from the root. 
In such cases, alternative numerical methods may be more suitable for finding the root.
'''

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

def steffensen(equation, E=0.001):
    if is_continuous(equation):
        try:
            equation = sympify(equation)

            # Find the value of f(x) at a=1 and a=2
            val_1 = interval(equation)[0]
            val_2 = interval(equation)[1]

            a, b = val_1, val_2
            a, b = round(a, 5), round(b, 5)

            # Take the intervals [a, b] and find the next value
            x0 = (a+b)/2

            i = 0
            f_x0 = 0.1

            x_0, f_x_0, f_x0_fx0, x_1 = [], [], [], []
            # Repeat steps 2 to 4 until f(xi)=0 or |f(xi)|≤Accuracy
            while abs(f_x0) > E and i < 20:
                i += 1
                
                # Evaluate the function at the current guess x0
                # Substituting next value in input equation
                f_x0 = equation.subs({"x": x0}).n(5)

                # Adding  value F of next value and its result, subing it in eqaution: f(x0+f(x0))
                ff_x0 = equation.subs({"x": f_x0+x0}).n(5)

                #  Finding the root using formular
                x1 = x0 - (f_x0**2 / (ff_x0-f_x0))
                x1 = round(x1, 5)
               
                xp= x0
                # Appending into list
                x_0+=[xp]
                f_x_0+=[f_x0] 
                f_x0_fx0+=[ff_x0] 
                x_1+=[x1]
                
                # Changing initial x_north to new value
                # # Update the current guess for the next iteration
                x0 = x1
                
            # Output the approximate root x3 obtained after the desired number of iterations or within the desired tolerance.
            dict_answer= {"x0": x_0, "f(x0)":f_x_0, "f(x0+f(x0))": f_x0_fx0, "x1": x_1, "root": x_1[-1], "iteration": len(x_1)}
            return dict_answer

        except:
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")

# Examples
 
# print(steffensen(x**3-x-1))

# print(steffensen(2*x**3 - 2*x - 5))

# print(steffensen(x**3 + 2*x**2 + x - 1))

# print(steffensen(x**2 - 12))

# print(steffensen(x**3 - 48))

# print(steffensen(2 + sin(x) - x ))



