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
    # print(fxa, fxb)

    # Find two points, say a and b such that a<b and f(a)*f(b)=0
    if v1 < v2 and (fxa*fxb) < 0:
        return True
    else:
        return False


def halley(equation, E=0.001):
    if is_continuous(equation):
        try:
            equation = sympify(equation)
            # equation= diff(equation, x)

            # Find the first derivative
            first_derivative = diff(equation, x, 1)

            # Find the second derivative
            second_derivative = diff(equation, x, 2)

            # Find the value of f(x) at a=1 and a=2
            val_1 = interval(equation)[0]
            val_2 = interval(equation)[1]

            a, b = val_1, val_2
            a, b = round(a, 5), round(b, 5)

            # Take the intervals [a, b] and find the next value
            x_0 = (a+b)/2

            f = 0.1
            i = 0

            Xo, f_x0, first_x0, second_x0, x1 = [], [], [], [], []

            # While loop keep running, then stop if f(xo) is less than Tolerance (accuracy)= 0.001
            while abs(f) > E and i < 10:
                i += 1
                # Substituting xo into input equation, first  and  second deriavative of input equation
                f = equation.subs({'x': x_0}).n(5)
                f_prime = first_derivative.subs({'x': x_0}).n(5)
                f_double_prime = second_derivative.subs({'x': x_0}).n(5)

                Xo += [x_0]
                f_x0 += [f]
                first_x0 += [f_prime]
                second_x0 += [f_double_prime]

                # Root
                x_curr = x_0 - (2*f*f_prime)/(2*f_prime**2 - f*f_double_prime)
                x_curr = round(x_curr, 5)

                xp = x_curr
                x_0 = x_curr

                x1 += [xp]

            dict_answer = {'x0': Xo, "f(x0)": f_x0, "f_prime(x0)": first_x0, "f_double_prime(x0)": second_x0, "x1": x1,
                 'root': x1[-1], "iteration": len(x1)}
            return dict_answer

        except:
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")

# Examples

# print(halley(x**3-x-1))

# print(halley(2*x**3 - 2*x - 5))

# print(halley(x**3 + 2*x**2 + x - 1))

# print(halley(x**2 - 12))

# (halley(x**3 - 48))

# print(halley(2 + sin(x) - x ))

