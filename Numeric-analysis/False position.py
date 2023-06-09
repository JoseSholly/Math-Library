import math
from sympy import *
x, y = symbols('x y')

'''
The False Position method provides a convergence guarantee when the function is continuous and changes sign over the interval [a, b]. 
However, it may suffer from slow convergence for certain types of functions, 
such as those with steep slopes or multiple roots close together. 
In such cases, other methods like Newton's method or the secant method may be more efficient.
'''


def interval(equation):
    # Finding Interval
    equation = sympify(equation)
    L1, L2 = [], []
    for i in range(0, 10):
        ans = equation.subs({'x': f"{i}"})
        if ans < 0:
            L1 += [i]

    for i in range(0, 10):
        ans = equation.subs({'x': f"{i}"})
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


def false_position(equation, E=0.0001):
    # Input the function f(x), the interval [a, b], 
    # the desired tolerance (tol) .

    if is_continuous(equation):
        try:

            # Find the value of f(x) at a=1 and a=2
            a = interval(equation)[0]
            b = interval(equation)[1]

            x0, x1 = a, b
            equation = sympify(equation)
            fxa = equation.subs({'x': x0})
            fxb = equation.subs({'x': x1})

            root = 0.1
            i = 0
            x2 = 0

            p1, fx_p1, p2, fx_p2, Xo, fx_Xo, point = [], [], [], [], [], [], []
            
            # If |f(c)| < tol or (b - a) / 2 < tol: # Check for convergence
            # The root has been found. Exit the algorithm.
            # Maximum iteration is specified in the 

            while abs(root) > E and i <= 20:
                i += 1
                # Mid-point between interval a and b
                x2 = ((x0*fxb) - (x1*fxa))/(fxb-fxa)
                p1 += [round(x0, 5)]
                p2 += [round(x1, 5)]
                Xo += [round(x2, 5)]

                #  Substituting mid-point into f(x)-equation
                root = equation.subs({'x': x2}).n(5)
                fx_Xo += [round(root, 5)]

                # It is the root of the given function if f(t)=0, else follow the step:
                # Divide the interval [a, b] - if f(t)*f(a)<0, there exist a root between t and a. Then, mid-point(Xo)= b
                # if f(t)*f(b)<0, there exist a root between t and b. Then, mid-point(Xo)= a
                if root != 0:
                    if root*fxa < 0:
                        x1 = x2
                        point += ["x1"]

                    elif root*fxb < 0:
                        x0 = x2
                        point += ["x0"]

                else:
                    x0, x1 = x2

                fxa = equation.subs({'x': x0})
                fx_p1 += [round(fxa, 5)]
                fxb = equation.subs({'x': x1})
                fx_p2 += [round(fxb, 5)]
                
            # Output the approximate root c obtained after the desired number of iterations or within the desired tolerance.
            dict_answer = {"x0": p1, "f(x0)": fx_p1, "x1": p2, "f(x1)": fx_p2, "x2": Xo,
                 "f(x2)": fx_Xo, "Point": point, "root": Xo[-1], "iteration": len(p1)}
            return dict_answer
        except:
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")


# print(false_position(x**3-x-1))

# print(false_position(2*x**2 - 3))

# print(false_position(2*x**3 - 2*x-5))

# print(false_position(x**2 - 12))

# print(false_position(x**3-48, 0.0001))

# print(false_position(x**3 + 2*x**2 + x -1, 0.0001))

