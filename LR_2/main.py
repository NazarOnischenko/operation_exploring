import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from math import fabs,sqrt

import window

def func1(x):
    return (x-N)**2

def func2(x):
    return (x-N)**2-N*x

def func3(x):
    return (x-N)**2+N*x**2

# global vars
N=15
Xmin=-N
Xmax=3*N
K=20
funcs=[True,True,True]
Funcs=[func1,func2,func3]
Xopt=[N,3*N/2,N/(N+1)]
Fopt=[func1(Xopt[0]),func2(Xopt[1]),func3(Xopt[2])]
#

class Window(QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ButtonExit.clicked.connect(self.methodClose)
        self.ButtonApply.clicked.connect(self.methodApply)

    def methodApply(self):
        if(self.ComboMethod.currentIndex()==0):
            self.result=dyhotomicSearch(Xmin,Xmax)
        else:
            self.result=goldenSlice(Xmin,Xmax)
        
        n=self.ComboGraphic.currentIndex()
        
        if(n < 3):
            Ox=[]
            Oy=[]
            lenght=1
            while(lenght < K and self.result[0][n][lenght-1]!="---"):
                lenght+=1 
            k=1
            while(k<lenght):
                Ox.append(k)
                Oy.append(self.result[0][n][k-1])
                k+=1
            plt.plot(Ox,Oy)
        elif(n==3):
            Ox=[[],[],[]]
            Oy=[[],[],[]]
            i=0
            while(i<3):
                lenght=1
                while(lenght < K and self.result[0][i][lenght-1]!="---"):
                    lenght+=1
                k=1
                while(k<lenght):
                    Ox[i].append(k)
                    Oy[i].append(self.result[0][i][k-1])
                    k+=1
                i+=1
            plt.plot(Ox[0],Oy[0],Ox[1],Oy[1],Ox[2],Oy[2])
        elif(n==4):
            Ox=[[],[],[]]
            Oy=[[],[],[]]
            Ox1=[[],[],[]]
            Oy1=[[],[],[]]
            self.result=dyhotomicSearch(Xmin,Xmax)
            i=0
            while(i<3):
                lenght=1
                while(lenght < K and self.result[0][i][lenght-1]!="---"):
                    lenght+=1
                k=1
                while(k<lenght):
                    Ox[i].append(k)
                    Oy[i].append(self.result[0][i][k-1])
                    k+=1
                i+=1
            self.result=goldenSlice(Xmin,Xmax)
            i=0
            while(i<3):
                lenght=1
                while(lenght < K and self.result[0][i][lenght-1]!="---"):
                    lenght+=1
                k=1
                while(k<lenght):
                    Ox1[i].append(k)
                    Oy1[i].append(self.result[0][i][k-1])
                    k+=1
                i+=1
            plt.plot(Ox[0],Oy[0],Ox[1],Oy[1],Ox[2],Oy[2],Ox1[0],Oy1[0],Ox1[1],Oy1[1],Ox1[2],Oy1[2])
        else:
            result1=dyhotomicSearch(Xmin,Xmax)
            result2=goldenSlice(Xmin,Xmax)
            Zk1=[[],[],[]]
            Zk2=[[],[],[]]
            Ox=[]
            k=0
            while(k<K):
                i=0
                while(i<3):
                    if(result1[1][i][k]!="---"):
                        Zk1[i].append(fabs(result1[1][i][k]-Fopt[i]))
                    else:
                        Zk1[i].append("---")

                    if(result2[1][i][k]!="---"):
                        Zk2[i].append(fabs(result2[1][i][k]-Fopt[i]))
                    else:
                        Zk2[i].append("---")
                    i+=1
                Ox.append(k+1) 
                k+=1
            plt.plot(Ox,Zk1[0],Ox,Zk1[1],Ox,Zk1[2],Ox,Zk2[0],Ox,Zk2[1],Ox,Zk2[2])
            #plt.plot(Ox,Zk1[2],Ox,Zk2[2])

        plt.grid()
        plt.show()
        self.methodTableOne()
        self.methodTableTwo()

    def methodClose(self):
        plt.close()
        self.close()
        
    def methodTableOne(self):
        self.Table1.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Table1.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Table1.setRowCount(K)
        k=0
        while(k<K):
            self.Table1.setItem(k,0,QTableWidgetItem(str(self.result[0][0][k])))
            self.Table1.setItem(k,1,QTableWidgetItem(str(self.result[1][0][k])))
            self.Table1.setItem(k,2,QTableWidgetItem(str(self.result[0][1][k])))
            self.Table1.setItem(k,3,QTableWidgetItem(str(self.result[1][1][k])))
            self.Table1.setItem(k,4,QTableWidgetItem(str(self.result[0][2][k])))
            self.Table1.setItem(k,5,QTableWidgetItem(str(self.result[1][2][k])))
            k+=1

    def methodTableTwo(self):
        self.Table2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Table2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.Table2.setRowCount(K)
        k=0
        Zk=[[],[],[]]
        while(k<K):
            i=0
            while(i<3):
                if(self.result[1][i][k]!="---"):
                    Zk[i].append(fabs(self.result[1][i][k]-Fopt[i]))
                else:
                    Zk[i].append("---")
                i+=1
            k+=1

        k=0
        while(k<K):
            self.Table2.setItem(k,0,QTableWidgetItem(str(Zk[0][k])))
            self.Table2.setItem(k,1,QTableWidgetItem(str(Zk[1][k])))
            self.Table2.setItem(k,2,QTableWidgetItem(str(Zk[2][k])))
            k+=1


def dyhotomicSearch(a,b):
    A=[a,a,a]
    B=[b,b,b]
    delta=0.0001
    eps=0.001
    k=1
    Xk=[[],[],[]]
    Fk=[[],[],[]]
    ind=[True,True,True]
    while(k <= K):
        i=0
        while(i<3):
            if(fabs(B[i]-A[i])<eps):
                    ind[i]=False
            if(ind[i]==True):
                p=(A[i]+B[i])/2-delta
                q=(A[i]+B[i])/2+delta
                if(funcs[i]==True):
                    if(Funcs[i](p)<Funcs[i](q)):
                        B[i]=q
                        Xk[i].append(p)
                        Fk[i].append(Funcs[i](p))
                    else:
                        A[i]=p
                        Xk[i].append(q)
                        Fk[i].append(Funcs[i](q))
            else:
                Xk[i].append("---")
                Fk[i].append("---")    
            i+=1
        k+=1
    return [Xk,Fk]

def goldenSlice(a,b):
    Xk=[[],[],[]]
    Fk=[[],[],[]]
    A=[a,a,a]
    B=[b,b,b]
    eps=0.001
    k=1
    P=[0,0,0]
    P[0]=A[0]+(1-0.618)*(B[0]-A[0])
    P[2]=P[1]=P[0]
    Q=[0,0,0]
    Q[0]=A[0]+0.618*(B[0]-A[0])
    Q[2]=Q[1]=Q[0]
    ind=[True,True,True]

    while(k<=K):
        i=0
        while(i<3):
            if(fabs(B[i]-A[i])<eps):
                    ind[i]=False
            if(ind[i]==True):
                L=Funcs[i](P[i])
                R=Funcs[i](Q[i])
                put=0
                if(L>R):
                    A[i]=P[i]
                    P[i]=Q[i]
                    Q[i]=A[i]+0.618*(B[i]-A[i])
                    put=Q[i]
                else:
                    B[i]=Q[i]
                    Q[i]=P[i]
                    P[i]=A[i]+(1-0.618)*(B[i]-A[i])
                    put=P[i]
                Xk[i].append(put)
                Fk[i].append(Funcs[i](put))
            
            else:
                Xk[i].append("---")
                Fk[i].append("---")  
            i+=1
        k+=1
    return [Xk,Fk]
                
def main():
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    app.exec_()

if __name__=="__main__":
    main()