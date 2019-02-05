import matplotlib.pyplot as plt
##create two list x and y
x=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
y=[10,12,20,22,21,25,30,21,32,34,35,30,50,45,55,60,66,64,67,72,74,80,79,84]
print(len(x),len(y))
##plot using scatter plot
plt.scatter(x,y)
plt.ylabel("dependent variable")
plt.xlabel("independent variable")
plt.show()
##the dependent variable has a linear distribution wrt independent
##line eq is y=mx+c where m is coeff of x and c is intercept
import numpy as np
def slope_intercept(x_val,y_val):
    xs=np.array(x_val)
    ys=np.array(y_val)
    m=(((np.mean(xs)*np.mean(ys))-np.mean(xs*ys))/(np.mean(xs)**2-np.mean(xs**2)))
    m=round(m,2)
    b=(np.mean(ys)-np.mean(x)*m)
    return m,b
##to see slope and intercept for x and y we need to call slope_intercept
print(slope_intercept(x,y))
m,b=slope_intercept(x,y)
##reg_line is the eq of regression line
reg_line=[(m*i)+b for i in x]
plt.scatter(x,y,color="red")
plt.plot(x,reg_line)
plt.ylabel("dependent variable")
plt.xlabel("independent variable")
plt.title("making a regression line")
plt.show()
