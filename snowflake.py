import matplotlib.pyplot as plt
import numpy as np
import math

def AffineTrans(Line):
    a, e = np.array([Line[0],Line[1]]), np.array([Line[2], Line[3]])
    V = e - a

    Llist = []

    b = a + V / 3.0
    d = b + V / 3.0
    alpha = math.radians(60)
    mat = np.array([[np.cos(alpha),np.sin(alpha)], [-np.sin(alpha), np.cos(alpha)]])
    c = b + np.dot(V / 3.0, mat)

    Llist.append([a[0],a[1],b[0],b[1]])
    Llist.append([b[0],b[1],c[0],c[1]])
    Llist.append([c[0],c[1],d[0],d[1]])
    Llist.append([d[0],d[1],e[0],e[1]])

    return Llist


def DrawFractal(Llist):
    for j in range(4):
        temp = []
        for i in Llist:
            Llist1 = AffineTrans(i)
            temp += Llist1
        Llist = temp
    for i in Llist:
        plt.plot([i[0],i[2]],[i[1],i[3]])
    plt.show()


L = 21.87
Llist=[[0,0,L/2.0,L/2.0*math.sqrt(3)],[L/2.0,L/2.0*math.sqrt(3),L,0],[L,0,0,0]]

DrawFractal(Llist)



