import math
import matplotlib.pyplot as plt

def combination(n, k):
    return (math.factorial(n)/float(math.factorial(n-k)*math.factorial(k)))

def bezier_curve(control_x, control_y):
    x = []; y = []; n = len(control_x)-1; u=0

    while u<=1:
        p,q = 0,0
        for k in range (n+1):
            bez = combination(n,k)*(u**k)*((1-u)**(n-k))
            p+=bez*control_x[k]
            q+=bez*control_y[k]
        x.append(p)
        y.append(q)
        u+=0.01
        
        plt.clf()
        plt.plot(x,y)
        plt.plot(control_x, control_y)
        plt.pause(0.01)

    plt.show()



control_x =  [1, 7, 15, 21];control_y=[5, 10, 5, 10]
bezier_curve(control_x, control_y)