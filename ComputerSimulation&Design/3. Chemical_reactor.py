import matplotlib.pyplot as plt

a = [100]; b = [50]; c= [0]; k1 = 0.008; k2 = 0.002; t=[0]; del_t = .1

for i in range (100):
    t.append(t[i]+del_t)
    a.append(a[i]+(k2*c[i]-k1*a[i]*b[i])*del_t)
    b.append(b[i]+(k2*c[i]-k1*a[i]*b[i])*del_t)
    c.append(c[i]+(2*k1*a[i]*b[i]-2*k2*c[i])*del_t)

    plt.pause(.01)
    plt.clf()
    plt.plot(t,a,'r', label='Substance A')
    plt.plot(t,b,'g', label='Substance B')
    plt.plot(t,c,'b', label='Substance C')
    plt.legend()
    plt.grid()
    plt.xlabel('Time(s)')
    plt.ylabel('Quantity(gram)')
    plt.xlim(0,15)
plt.show()
