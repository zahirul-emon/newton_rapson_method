import math
""" Newton-Rapson method for f(x) = 2*x^3 - 2*x - 5
 Newton-Rapson equation ​xn+1 = xn− f(xn)/f′(xn)
Notations:
a, b intial guess
x0 is equal xn and xn is equal xn+1 in main equation
"""
#f(x) for main function
def f(x):
    return 2*math.pow(x,3) - 2*x - 5
#f1d(x) is for first derivative of f(x)
def f1d(x):
    return 6*math.pow(x,2) - 2
#root_calc(x) is for iteration
def root_calc(x):
    return x - (f(x)/f1d(x))
#newton_rapson() is the main function.    
def newton_rapson():
    global xn
    a = float(input("Input intial guess a: "))
    b = float(input("Input intial guess b: "))
    if f(a)*f(b)>0:
        print("Enter a and b again")
        newton_rapson()
    else:
        x0 = root_calc(a)
        condition = True
        i = 0
        while condition:
            i += 1
            print("Iteration No: ",i)
            
            xn = root_calc(x0)
            if abs(xn - x0)!= 0:
                condition = True
                x0 = xn
            elif abs(xn-x0)== 0:
                condition = False
            
newton_rapson()                 
print("The final root is : %0.6f"% xn)    
   


                   
