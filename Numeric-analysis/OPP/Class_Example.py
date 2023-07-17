import math
from sympy import *
x,y, p = symbols('x y p')

class Jose_math:
    def __init__(self, equation):
        self.equation= sympify(equation)
        

    def __repr__(self):
        expr= sympify(self.equation)

        return f"{self.equation}"
    
    def interval(self):
        # Finding Interval
        equation= sympify(self.equation)
        L1, L2=[],[]
        for i in range(-10,10):
            ans=equation.subs({x:f"{i}"})
            if ans<0:
                L1+=[i]
        
        for i in range(L1[-1],10):
            ans=equation.subs({x:f"{i}"})
            if ans>0:
                L2+=[i]
                
        if L2[0]>L1[-1]:
            return (L1[-1], L2[0])
        else:
            return (L2[-1], L1[0] )
    
    def is_continuous(self):
        # For any continuous function
        equation= sympify(self.equation)
        intervals= self.interval()
        
        x1, x2= intervals[0], intervals[1]
        # return x1, x2

        # Substititing intervals into function
        fxa=equation.subs({'x':x1})
        fxb=equation.subs({'x':x2})

        # Find two points, say a and b such that a<b and f(a)*f(b)=0
        if x1<x2 and (fxa*fxb)<0:
            return True
        else:
            return False
   
class Bisection(Jose_math):
    def __init__(self, equation, tolerance=0.0001):
        super().__init__(equation)
        self.tolerance= tolerance
    
    def solve(self):
        equation= sympify(self.equation)
        E= self.tolerance
    
        if self.is_continuous():
            try:

                # Find the value of f(x) at a=1 and a=2
                intervals= self.interval()
                a,b= intervals[0],intervals[1]

                equation= sympify(equation)
                fxa=equation.subs({x:a})
                fxb=equation.subs({x:b})
        
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
                    
                    #  Substituting mid-point into f(x)-equation
                    t= equation.subs({x:mid_point}).n(5)
                    fx_Xo+=[round(t,5)]
                    

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

                    else:
                        a,b= mid_point


                dict_answer= {"a": p1,"f(a)": fx_p1, "b":p2,"f(b)":fx_p2, "mid_point":Xo, "f(mid_point)": fx_Xo, "Point":point, "root": Xo[-1], "iteration":len(p1)}
                
                return dict_answer 
            except:
                raise Exception("Function is not continous!!!")
        else:
            raise Exception("Function is not continous!!!")
               
class False_Position(Jose_math):
    def __init__(self, equation, tolerance=0.0001):
        super().__init__(equation)
        self.tolerance= tolerance

    def solve(self):
        equation= self.equation
        E= self.tolerance
        if self.is_continuous():
            try:

                # Find the value of f(x) at a=1 and a=2
                intervals= self.interval()
                a,b= intervals[0],intervals[1]

                x0, x1 = a, b
                equation = sympify(equation)
                fxa = equation.subs({x: x0})
                fxb = equation.subs({x: x1})
                

                root = 0.1
                i = 0
                x2 = 0

                p1, fx_p1, p2, fx_p2, Xo, fx_Xo, point = [], [], [], [], [], [], []

                while abs(root) > E and i <= 20:
                    i += 1
                    # Mid-point between interval a and b
                    x2 = ((x0*fxb) - (x1*fxa))/(fxb-fxa)
                    p1 += [round(x0, 5)]
                    p2 += [round(x1, 5)]
                    Xo += [round(x2, 5)]
                    
                    #  Substituting mid-point into f(x)-equation
                    root = equation.subs({x: x2}).n(5)
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

                    fxa = equation.subs({x: x0})
                    fx_p1 += [round(fxa, 5)]
                    fxb = equation.subs({x: x1})
                    fx_p2 += [round(fxb, 5)]
                dict_answer = {"x0": p1, "f(x0)": fx_p1, "x1": p2, "f(x1)": fx_p2, "x2": Xo,
                    "f(x2)": fx_Xo, "Point": point, "root": Xo[-1], "iteration": len(p1)}
                return dict_answer
            except:
                raise Exception("Function is not continous!!!")
        else:
            raise Exception("Function is not continous!!!")

class Newton_Raphson(Jose_math):
    def __init__(self, equation, tolerance=0.0001):
        super().__init__(equation)
        self.tolerance= tolerance
    def solve(self):
        equation= self.equation
        E= self.tolerance
        if self.is_continuous():
            try:

                # Find the value of f(x) at a=1 and a=2
                intervals= self.interval()
                x1,x2= intervals[0],intervals[1]

                a,b= x1,x2
                # Input Equation 
                equation= sympify(equation)
                # We differentiate the input equation
                diff_equation= diff(equation, x)
                
                # fxa=equation.subs({x:a})
                # fxb=equation.subs({x:b})
        
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
                    
                dict_answer= {"Xo": X0[:-1], "f(Xo)":fx_X0, "f'(Xo)": fxx_X0, "X1": X1, "Point": point, "root":X0[-1], "iteration": len(fx_X0)}
                return dict_answer  


            except:
                raise Exception("Function is not continous!!!")
        else:
            raise Exception("Function is not continous!!!")

class Fixed_Point(Jose_math):
    def __init__(self, equation, tolerance= 0.0001):
        super().__init__(equation)
        self.tolerance= tolerance
    def change_sub(self):
        equation= self.equation
        #  First rewrite the eqaution x = omega(x), making x sunject of the formular 

        # Covert formular to string 
        equation= str(sympify(equation))

        # Creation mathemtical symbols from sympy
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
            
    def solve(self):
        equation= sympify(self.equation)
        E= self.tolerance
        
        if self.is_continuous():
            try:
                # Find the root that lies betwwen a=1 and a=2
                intervals= self.interval()
                x1,x2= intervals[0],intervals[1]
                
                # Making x Subject of formular 
                fx = self.change_sub()

                a,b= x1,x2
                Xo= (a + b)/2

                # Substituting mid-point to new equation
                new_x= fx.subs({'x':Xo})

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
                return dic

                    
            except:
                raise Exception("Function is not continous!!!") 
        else:
            raise Exception("Function is not continous!!!")
        
class Secant(Jose_math):
    def __init__(self, equation, tolerance= 0.0001):
        super().__init__(equation)
        self.tolerance= tolerance
    

    def solve(self):
        equation= sympify(self.equation)
        E= self.tolerance
        if self.is_continuous():
            try:

                # Find the root that lies betwwen a=1 and a=2
                intervals= self.interval()
                a,b= intervals[0],intervals[1]

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
                    root = round(equation.subs({x: x2}).n(5), 6)

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

                dict_answer={"xo": Xo, "f(Xo)":fx_Xo, "x1":X1, "f(x1)":fx_X1, "x2": X2, "f(x2)": fx_X2, "root":X2[-1], "iteration": len(X1)}
                return dict_answer
            except:        
                raise Exception("Function is not continous!!!")
        else:
            raise Exception("Function is not continous!!!")
    
class Halley(Jose_math):
    def __init__(self, equation, tolerance= 0.001):
        super().__init__(equation)
        self.tolerance= tolerance
    
    def solve(self):
        equation= sympify(self.equation)
        E= self.tolerance
        if self.is_continuous():
            try:
                equation = sympify(equation)
                # equation= diff(equation, x)

                # Find the first derivative
                first_derivative = diff(equation, x, 1)

                # Find the second derivative
                second_derivative = diff(equation, x, 2)

                # Find the root that lies betwwen a=1 and a=2
                res= self.interval()
                val_1, val_2= res[0],res[1]

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

class Muller(Jose_math):
    def __init__(self, equation, tolerance= 0.001):
        super().__init__(equation)
        self.tolerance= tolerance
    def solve(self):
        equation= self.equation
        E= self.tolerance
        if self.is_continuous():
            try:

                # Find the root that lies betwwen a=1 and a=2
                res= self.interval()
                val_1,val_2= res[0],res[1]

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


                dict_answer= {'x0':x_0,"x1":x_1, "x2":x_2,"f(x0)":f_x0, "f(x1)":f_x1, "f(x2)":f_x2,
                    'a':a_val, 'b':b_val, 'c':c_val, "x3": x_3, 'rpe':relative_percent,
                    'root':x_3[-1], "iteration": len(x_3)}
                return dict_answer
                    
                

            except:        
                raise Exception("Function is not continous!!!")
        else:
            raise Exception("Function is not continous!!!")

class Steffensen(Jose_math):
    def __init__(self, equation, tolerance= 0.001):
        super().__init__(equation)
        self.tolerance= tolerance
    def solve(self):
        equation= self.equation
        E= self.tolerance
        if self.is_continuous():
            try:
                equation = sympify(equation)

                # Find the root that lies betwwen a=1 and a=2
                res= self.interval()
                val_1, val_2= res[0],res[1]

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
                    x0 = x1

                dict_answer= {"x0": x_0, "f(x0)":f_x_0, "f(x0+f(x0))": f_x0_fx0, "x1": x_1, "root": x_1[-1], "iteration": len(x_1)}
                return dict_answer

            except:
                raise Exception("Function is not continous!!!")
        else:
            raise Exception("Function is not continous!!!")

class Ridder(Jose_math):
    def __init__(self, equation, tolerance= 0.0001):
        super().__init__(equation)
        self.tolerance= tolerance
    def solve(self):
        equation= self.equation
        E= self.tolerance
        if self.is_continuous():
            try:
                equation = sympify(equation)

                # Find the root that lies betwwen a=1 and a=2
                res= self.interval()
                val_1, val_2= res[0],res[1]

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




