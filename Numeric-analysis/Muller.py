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

def muller(equation, E=0.001):
    if is_continuous(equation):
        try:

            # Find the value of f(x) at a=1 and a=2
            val_1 = interval(equation)[0]
            val_2 = interval(equation)[1]

            x0, x1 = val_1, val_2
            x0, x1= round(x0, 5), round(x1, 5)
            equation = sympify(equation)

            # Find the value of x2= x0+x1/2
            x2= round((x1+x0)/2, 5)
            i=0
            rpe=0.1
            x_0, x_1, x_2, f_x0, f_x1, f_x2, a_val,b_val, c_val, x_3, relative_percent = [], [], [], [], [], [], [], [], [], [], []

            # While loop keep running, then stop if Relative Percent error is less than Tolerance (accuracy)= 0.001
            while abs(rpe)>E  and i<10:
                i+=1
                #  Substituting the value of x0, x1, x2 into input equation
                fx_x0= equation.subs({"x":x0}).n(5)
                fx_x1= equation.subs({"x":x1}).n(5)
                fx_x2= equation.subs({"x":x2}).n(5)

                # Calculating for h1 and h2
                h1= x1-x0
                h2= x2-x1
                
                # Calculating for delta 1 and delta 2
                delta_1= (fx_x1 - fx_x0)/ h1
                delta_2= (fx_x2 - fx_x1)/ h2

                # Calculating for a, b and c
                a= round((delta_2 - delta_1) / (h2 + h1), 5)
                b= round(a *h2 + delta_2, 5)
                c= fx_x2
                # The quadratic equation formular vhas + 0r - depending on the value of b
                if b>0: 
                    x3= x2 + ((-2*c )/ (b + ((b**2) - (4*a*c))**0.5)) 
            
                else: 
                    x3= x2 + ((-2*c )/ (b - ((b**2) - (4*a*c))**0.5))
                    

                x3= round(x3, 5)
                # Relative percent error
                rpe= abs((x3- x2)/x3)
                rpe= round(rpe, 6)

                # Creating new storage location for x0, x1, x2
                p0, p1, p2=x0, x1,x2

                # x0, x1,x2 =x1, x2, x3 
                #  Calculating next iteration since RPE>Accuracy
                x0, x1,x2 =x1, x2, x3

                # Appending answer into list

                x_0+=[p0]
                x_1+=[p1]
                x_2+=[p2]

                f_x0+=[fx_x0]
                f_x1+=[fx_x1]
                f_x2+=[fx_x2]

                a_val+=[a]
                b_val+=[b]
                c_val+=[c]

                x_3+=[x3]
                relative_percent+=[rpe*100]

            dict_answer= {'x0': x_0,"x1": x_1, "x2": x_2,"f(x0)": f_x0, "f(x1)":f_x1, "f(x2)":f_x2,
                'a':a_val, 'b':b_val, 'c':c_val, "x3": x_3, 'rpe':relative_percent,
                'root': x_3[-1], "iteration": len(x_3)}
            return dict_answer
        except:        
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")

# Examples

# print(muller(x**3-x-1))

# print(muller(2*x**3 - 2*x - 5))

# print(muller(x**3 + 2*x**2 + x - 1))

# print(muller(x**2 - 12))

# print(muller(x**3 - 48))

# print(muller(2 + sin(x) - x ))
