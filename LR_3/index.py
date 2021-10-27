import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import untitled

from math import fabs,sqrt
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import *


def func1old(x1, x2):
    return (x1-N)**2+(2*x2-N)**2

def func2old(x1, x2):
    return 10*(3*N*x2-x1**2)**2 + (N-x1)**2

def e(j,n):
    arg=zeros(n)
    arg[j-1]=1
    return arg

N=16
x10=-1.2*N
x20=1.5*N
eps=0.001
Kmax=20

Xk=[]
Fk=[]
Dk=[]

phi = 0.5 * (1.0 + sqrt(5.0))

def func1(x):
    x=array(x).T
    return (x[0]-N)**2+(2*x[1]-N)**2

def func2(x):
    x=array(x).T
    return 10*(3*N*x[1]-x[0]**2)**2 + (N-x[0])**2



def minimize(f,eps,a,b,ind,var): 
    dd=fabs(f(b,var)-f(a,var)) 
    if ind:
        dd=fabs(f(var,b)-f(var,a)) 
    if dd < eps:
        return (a+b)/2 
    else:
        t = (b-a)/phi
        x1, x2 = b - t, a + t 
        q=f(x1,var) 
        Q=f(x2,var)
        if ind:
            q=f(var,x1) 
            Q=f(var,x2)
        if q>=Q:
            return minimize(f, eps, x1, b, ind,var)
        else:
            return minimize(f, eps, a, x2,ind,var)

def FindLocalMinima(f,a,b,xoper):
    eps=0.001
    if fabs(b - a) < eps: 
        return 0.5 * (a + b)
    else:
        t = (b - a) / phi
        B,A = b - t, a + t
        if f(B,xoper) >= f(A,xoper):
            return FindLocalMinima(f,B,b,xoper)
        else:
            return FindLocalMinima(f,a,A,xoper)

class Window(QMainWindow, untitled.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ButtonExit.clicked.connect(self.methodClose)
        self.ButtonApply.clicked.connect(self.methodApply)
        self.Button3DG.clicked.connect(self.method3DG)
        self.ButtonProj.clicked.connect(self.methodProj)
    
    def methodApply(self):
        self.drawProjInd=False
        self.f=func1 # functions applying
        self.methodCycleCoordDrop()
        self.methodTable()
        
    def methodClose(self):
        self.close()

    def method3DG(self):
        f=self.f
        a1=-2*N
        b1=2*N
        if(f==func2):
            a1=-1.5*N*N
            b1=1.5*N*N
        self.draw3D(a1,b1)

    def methodProj(self):
        f=self.f
        a1=-2*N
        b1=2*N
        if(f==func2):
            a1=-1.5*N*N
            b1=1.5*N*N
        self.drawProjInd=True
        self.methodCycleCoordDrop()
        self.drawProjection(a1,b1)
        self.drawProjInd=False

    def methodTable(self):
        self.Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Table.setColumnCount(self.K)
        k=0
        while(k<self.K):
            self.Table.setItem(0,k,QTableWidgetItem(str(Xk[k][0])))
            self.Table.setItem(1,k,QTableWidgetItem(str(Xk[k][1])))
            self.Table.setItem(2,k,QTableWidgetItem(str(Fk[k])))
            k+=1

    def draw3D(self,a,b):
        f=self.f
        h=(b-a)/200
        x=arange(a,b,h)
        y=arange(a,b,h)
        z=zeros((len(x),len(y)))
        for i in range(len(x)):
            for j in range(len(y)):
                z[i][j]=f([x[i],y[i]])
        x,y=meshgrid(x,y)
        fig=plt.figure()
        axes=Axes3D(fig)
        axes.plot_surface(x,y,z, cmap=cm.jet)
        plt.title("Graphic")
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.show()

    def drawProjection(self,a,b):
        K=self.K
        k=0
        plt.plot(x10,x20,'bo')
        f=self.f
        # if(f==func2):
        #     a=a/N
        #     b=b/N
        h=(b-a)/100
        X=arange(a,b,h)
        Y=arange(a,b,h)
        X,Y=meshgrid(X,Y)
        if (f==func1):
            plt.contour(X,Y,func1old(X,Y),10)
        else:
            plt.contour(X,Y,func2old(X,Y),10)
        plt.plot(Xk[K][0],Xk[K][1],'ro')
        plt.show()

    def methodCycleCoordDrop(self):
        f=self.f
        n=2
        a1=-2*N
        b1=2*N
        if(f==func2):
            a1=-1.5*N*N
            b1=1.5*N*N
        y=[x10,x20]    
        x=y.copy()
        x0=zeros(n)
        k=0
        cont=True
        Xk.append([float(x[0]),float(x[1])])
        Fk.append(f(y))
        while(k<Kmax and cont):
            d=e(k-int(k/n)*n+1,n)
            j=0
            def Fi(lym,xoper):
                return f(xoper+lym*d)
            if(j==1):
                    a=0
                    b=1.5*N*N
            else:
                a=-2*N
                b=2*N
            lym=FindLocalMinima(Fi,a,b,y)
            x0=y.copy()
            y=y+lym*d
            j+=1
            if(self.drawProjInd==True):
                plt.plot([x[0],x[0],y[0]],[x[1],y[1],y[1]],'-b')
            if(linalg.norm(x0-y)<=eps):     
                cont=False
            else:
                x=y.copy()
            k+=1
            Xk.append([float(y[0]),float(y[1])])
            Fk.append(f(y))
        self.K=k   
        
def main():
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    app.exec_()
    
    

if __name__=="__main__":
    main()