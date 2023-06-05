import math
from sympy import *
x,y = symbols('x y')
'''
The Newton-Raphson method utilizes the derivative of the function to iteratively refine the approximation of the root. 
It converges rapidly for well-behaved functions and when the initial guess is close to the root. 
However, it may fail to converge or converge slowly for certain functions or when the initial guess is far from the root. 
In such cases, alternative methods like the bisection method or the secant method can be used.
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
    # print(fxa, fxb)

    # Find two points, say a and b such that a<b and f(a)*f(b)=0
    if v1 < v2 and (fxa*fxb) < 0:
        return True
    else:
        return False

def newton_raphson(equation,E=0.0001):
    #  the desired tolerance (E)
    # If equation is continuous, it proceeds but, if not, it raises an exception 
    if is_continuous(equation):
        try:

            # Find the value of f(x) at a=1 and a=2
            x1= interval(equation)[0]
            x2=interval(equation)[1]

            a,b= x1,x2
            # Input the function f(x),
            equation= sympify(equation)
            # its derivative f'(x),
            diff_equation= diff(equation, x)
            
            F_x= 0.1
            i=0
            dx_x=0
            root=0

            mid_point= (a+b)/2

            X0,fx_X0, fxx_X0, X1, point=[mid_point],[],[],[],[]

            while abs(F_x)>E and abs(F_x)!=0 and i<=20:
                i+=1
                # Substituting Mid-point between interval a and b into input equation
                F_x= equation.subs({x:mid_point}).n(5)
                fx_X0+=[round(F_x, 5)]

                # Substituting Mid-point between interval a and b into differential  equation
                dx_x= diff_equation.subs({x:mid_point}).n(5)
                fxx_X0+=[round(dx_x,5)]
                
                # Substituting values into root formular
                root= mid_point - (F_x/dx_x)
                point+=["x1"]
                
                X0+=[(round(root,5)) ]

                mid_point= root
                X1+=[(round(root,5)) ]
                
            # Output the approximate root x obtained after the desired number of iterations or within the desired tolerance.
            answer= {"Xo": X0[:-1], "f(Xo)":fx_X0, "f'(Xo)": fxx_X0, "X1": X1, "Point": point, "root":X0[-1], "iteration": len(fx_X0)}

            return answer  


        except:
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")

# print(newton_raphson(x**3 - x - 1))

# print(newton_raphson(2*x**3 - 2*x - 5))

# print(newton_raphson(x**2 - 12))

# print(newton_raphson(x**3 - 48))

# print(newton_raphson(x**3 + 2*x**2 + x -1))

# print(newton_raphson(2 + sin(x) - x ))

