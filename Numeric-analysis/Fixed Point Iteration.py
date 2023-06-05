import math
from sympy import *
x,y = symbols('x y')
'''
In this method, the function g(x) is chosen such that g(x) = x, i.e., 
finding the root of the function f(x) is transformed into finding a fixed point of g(x). 
The convergence of the Fixed-Point Iteration method depends on the properties of the function g(x) and the initial guess x0. 
It requires g(x) to be continuous and satisfy certain conditions, such as Lipschitz continuity, to ensure convergence.

It's important to note that the Fixed-Point Iteration method may not always 
converge or converge slowly for certain functions or initial guesses. 
In such cases, other numerical methods like Newton's method or the secant method may be more appropriate.
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

def change_sub(equation):
    #  First rewrite the eqaution x = omega(x), making x sunject of the formular 

    # Covert formular to string 
    equation= str(sympify(equation))

    # Creation mathematical symbols from sympy
    p, x = symbols('p x')

    # Finding string character in  equation
    rem=[ch for ch in equation if ch.isalpha()]
    if len(rem)==1:
        equation= (sympify(equation)- sympify(10*x))/sympify(-10)
        return equation

    # if there are more one occurence of string character, then function is discontinous
    elif len(rem)==2:  #len((set(rem)))==1
        rem= tuple(set(rem))[0]

        # Covert one first occurence of x into p, sympy can't handle change of subject of same unknown.
        # Meaning: if we want p as subject, Sympy can handle p-x=2: p= 2+x  not p-2p=5: -5 
        equation=equation.replace(rem,"p",1 )

        equation = sympify(equation)
        return solve(equation, p)[0]
    
    elif len(rem)>2:
        equation = sympify(equation)
        # print(equation)
        char=list(equation.args)
        if x in char:
            char[char.index(x)]= p
            char= tuple(char)
            equation=equation.func(*char)

            return solve(equation, p)[0]
        else:
            val = [i for i in char if 'x' in str(i) and str(i).count('*')==1]
            ind=char.index(val[0])
            val= str(val[0])
            val= val.replace("x","p")
            char[ind]= sympify(val)
            equation=equation.func(*char)
            
            return solve(equation, p)[0]
        
def fixed_point_iteration(equation, E=0.0001):
    equation= sympify(equation)
    # if equation is continuous, it proceeds but, else, it raise exception 
    if is_continuous(equation):
        try:
            # Find the root that lies betwwen a=1 and a=2
            x1= interval(equation)[0]
            x2=interval(equation)[1]

            # Making x Subject of formular 
            fx = change_sub(equation)

            a,b= x1,x2
            Xo= (a + b)/2

            # Substituting mid-point to new equation
            new_x= fx.subs({'x':Xo})

            next= 0.1
            new_p=0
            i=0
            root= 0.1
            '''
            While iter < max_iter:
                - Set x = g(x0) # Compute the next iteration using the function g(x)
                - If |x - x0| < tol: # Check for convergence
                    -The root has been found. Exit the algorithm.
                - Set x0 = x # Update the initial guess for the next iteration
                - Increment iter by 1.
            '''

            mp, Fx_mp, point, diff= [round(Xo, 5)],[round(new_x,5)],["x1"],[abs(round(new_x-Xo, 5))]
            # While condition keeps working as long as root does not exceed tolerance 0.0001
            while abs(root)>E and i<20:
                i+=1
                # Substituting mid-point to new equation for next iteration
                next= fx.subs({'x':new_x})

                Xo=round(new_x, 5)

                root= new_x-next
                new_p= next
                
                mp+=[round(new_x, 5)]
                Fx_mp+=[round(new_p,5)]
                point+=["x1"]
                diff+=[abs(round(new_x-next, 5))]

                # Changing previous root to  new root
                new_x=next
                
                if root>20000: break
                else:continue
            # Output the approximate root x obtained after the desired number of iterations or within the desired tolerance.
            dict_answer= {"xo":mp, "x1":Fx_mp, "point":point, "difference": diff,"iteration": len(Fx_mp) ,"root": Fx_mp[-1]}
            return dict_answer      
        except:
            raise Exception("Function is not continous!!!") 
    else:
        raise Exception("Function is not continous!!!")


# print(fixed_point_iteration((x**3)-x-1))

# print(fixed_point_iteration(2*x**3 - 2*x - 5))

# print(fixed_point_iteration(x**2 - 12))

# print(fixed_point_iteration(x**3 - 48))

# print(fixed_point_iteration(x**3 + 2*x**2 + x -1 ))

