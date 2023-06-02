import math
from sympy import *
x,y = symbols('x y')

def interval(equation):
    # Finding Interval
    equation= sympify(equation)
    L1, L2=[],[]
    for i in range(-10,10):
        ans=equation.subs({x:f"{i}"})
        if ans<0:
            L1+=[i]

    for i in range(L1[-1],10):
        ans=equation.subs({x:f"{i}"})

        if ans>0:
            L2+=[i]
        
    return L1[-1],L2[0]


def is_continuous(equation):

    # For any continuous function
    x1= interval(equation)[0]
    x2=interval(equation)[1]

    # Substititing intervals into function
    fxa=equation.subs({x:x1})
    fxb=equation.subs({x:x2})

    # Find two points, say a and b such that a<b and f(a)*f(b)=0
    if x1<x2 and (fxa*fxb)<0:
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
    
    if is_continuous(equation):
        try:
            # Find the root that lies betwwen a=1 and a=2
            x1= interval(equation)[0]
            x2=interval(equation)[1]
            # print(x1, x2)
            

            # Making x Subject of formular 
            fx = change_sub(equation)

            a,b= x1,x2
            Xo= (a + b)/2

            # Substituting mid-point to new equation
            new_x= fx.subs({'x':Xo})
            
            # print("Start",round(Xo, 5),round(new_x,5),abs(round(new_x-Xo, 5)))

            next= 0.1
            new_p=0
            i=0
            root= 0.1

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

                dic= {"xo":mp, "x1":Fx_mp, "point":point, "difference": diff,"iteration": len(Fx_mp) ,"root": Fx_mp[-1]}

                # Changing previous root to  new root
                new_x=next
                if root>20000: break
                else:continue
            # Returns answer in a dictionary
            return dic

                
        except:
            raise Exception("Function is not continous!!!") 
    else:
        raise Exception("Function is not continous!!!")


# print(fixed_point_iteration((x**3)-x-1))

# print(fixed_point_iteration(2*x**3 - 2*x - 5))

# print(fixed_point_iteration(x**2 - 12))

# print(fixed_point_iteration(x**3 - 48))

# print(fixed_point_iteration(x**3 + 2*x**2 + x -1 ))

