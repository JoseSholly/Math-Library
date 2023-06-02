
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
            # print(ans, i)
            #break
   
    for i in range(L1[-1],10):
        ans=equation.subs({x:f"{i}"})
        if ans>0:
            L2+=[i]
            # print(ans, i)
            #break
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
      
def bisection(equation,E=0.0001):
    
    if is_continuous(equation):
        try:

            # Find the value of f(x) at a=1 and a=2
            x1= interval(equation)[0]
            x2=interval(equation)[1]

            a,b= x1,x2
            equation= sympify(equation)
            fxa=equation.subs({x:a})
            fxb=equation.subs({x:b})
            # print(fxa)
            # print(fxb)
    
            t= 0.1
            i=0
            mid_point=0

            p1,fx_p1,p2,fx_p2,Xo,fx_Xo, point=[],[],[],[],[],[],[]

            while abs(t)>E and i<=20:
                i+=1
                # Mid-point between interval a and b 
                mid_point= (a+b)/2
                p1+=[round(a, 5)]
                p2+=[round(b, 5)]
                Xo+=[round(mid_point, 5)]
                # print(f"X{i-1}= {mid_point} Interval btw {a} and {b}")
                #  Substituting mid-point into f(x)-equation
                t= equation.subs({x:mid_point}).n(5)
                fx_Xo+=[round(t,5)]
                # print(t)

                fxa=equation.subs({x:a})
                fx_p1+=[round(fxa, 5)]
                fxb=equation.subs({x:b})
                fx_p2+=[round(fxb, 5)]
                
                # It is the root of the given function if f(t)=0, else follow the step:
                # Divide the interval [a, b] - if f(t)*f(a)<0, there exist a root between t and a. Then, mid-point(Xo)= b
                # if f(t)*f(b)<0, there exist a root between t and b. Then, mid-point(Xo)= a
                if t!=0:
                    if t*fxa<0:
                        b= mid_point
                        point+=["b"]

                        
                    elif t*fxb<0:
                        a=mid_point
                        point+=["a"]

                    # print("f(x{})= {}\n".format(i-1,t))

                else:
                    a,b= mid_point


            d= {"a": p1,"f(a)": fx_p1, "b":p2,"f(b)":fx_p2, "mid_point":Xo, "f(mid_point)": fx_Xo, "Point":point, "root": Xo[-1], "iteration":len(p1)}
            
            return d 
        except:
            raise Exception("Function is not continous!!!")
    else:
        raise Exception("Function is not continous!!!")

       
        
# bisection(equation, tolerance(if given))

# bisection(x**3-x-1)

# bisection(2*x**2-3)

# bisection(2*x**3-2*x-5)

# bisection(x**2-12)

# bisection(x**3-48)

# print(bisection(x**3 + 2*x**2 + x -1)


    
