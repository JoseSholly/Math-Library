import math
from sympy import *
x, y = symbols('x y')


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

def ridder(equation, E=0.0001):
    if is_continuous(equation):
        try:
            equation = sympify(equation)

            # Find the value of f(x) at a=1 and a=2
            val_1 = interval(equation)[0]
            val_2 = interval(equation)[1]

            x1, x2 = val_1, val_2
            x1, x2 = round(x1, 5), round(x2, 5)

            f1= equation.subs({'x': x1}).n(5)
            f2= equation.subs({"x": x2}).n(5)

            i=0
            f4= 0.1
            root=[]
            while abs(f4)>E and i<10:
                i+=1
                x3= 0.5*(x1 + x2)
                x3= round(x3, 5)

                f3= equation.subs({'x': x3})
                f3= round(f3, 5)

                s= (f3**2 - f1 * f2)**0.5
                s= round(s, 5)

                # Here, f1<f2, So we use minus sign, else we use positve sign
                if f1<f2:
                    x4= x3 - (x3 - x1)*(f3/s)
                else:
                    x4= x3 + (x3 - x1)*(f3/s)

                x4= round(x4, 5)

                f4= equation.subs({'x': x4})
                f4= round(f4, 5)

                root+=[x4]

                #  As the root lies in the interval (x3,x4), we let 
                # x1=x3,  f1=f3, x2=x4,  f2=f4
                x1=x3  
                f1=f3
                x2=x4  
                f2=f4
            dict_answer= {'root':root[-1], 'iteration': len(root)}
            return dict_answer

        except:
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")

# Examples
# print(ridder(x**3-x-1))

# print(ridder(2*x**3 - 2*x - 5))

# print(ridder(x**3 + 2*x**2 + x - 1))

# print(ridder(x**2 - 12))

# print(ridder(x**3 - 48))

# print(ridder(2 + sin(x) - x ))
