import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *# Это наш конвертированный файл дизайна
import matplotlib.pyplot as plt
from math import fabs
import form
import table
import result as res

class FormTable(QtWidgets.QMainWindow, table.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class FormResult(QtWidgets.QMainWindow, res.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Window(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Apply.clicked.connect(self.methodApply)
        self.Close.clicked.connect(self.close)
        self.ComboBox.currentTextChanged.connect(self.methodAmountChange)

    def methodAmountChange(self):
        if(self.ComboBox.currentIndex()==0):
            self.SpinAmount.setProperty("value", 400)
        else:
            self.SpinAmount.setProperty("value", 20)

    def methodApply(self):
        if(self.ComboBox.currentIndex()==0):
            mas = []
            if(self.CheckFormula1.isChecked()):
                mas.append(self.search(self.SpinAmount.value(), self.SpinStart.value(), self.SpinEnd.value(), first))
                plt.plot(mas[0][0], mas[0][1])
            else:
                mas.append(None)
            if(self.CheckFormula2.isChecked()):
                mas.append(self.search(self.SpinAmount.value(), self.SpinStart.value(), self.SpinEnd.value(), second))
                plt.plot(mas[1][0], mas[1][1])
            else:
                mas.append(None)
            if(self.CheckFormula3.isChecked()):
                mas.append(self.search(self.SpinAmount.value(), self.SpinStart.value(), self.SpinEnd.value(), third))
                plt.plot(mas[2][0], mas[2][1])
            else:
                mas.append(None)
            self.resultFirst(mas)
        elif(self.ComboBox.currentIndex()==1):
            mas = []
            if(self.CheckFormula1.isChecked()):
                mas.append(self.specification(self.SpinAmount.value(), self.SpinStart.value(), self.SpinEnd.value(), first, firstPoh))
                plt.plot(mas[0][0], mas[0][1])
            else:
                mas.append(None)
            if(self.CheckFormula2.isChecked()):
                mas.append(self.specification(self.SpinAmount.value(), self.SpinStart.value(), self.SpinEnd.value(), second, secondPoh))
                plt.plot(mas[1][0], mas[1][1])
            else:
                mas.append(None)
            if(self.CheckFormula3.isChecked()):
                mas.append(self.specification(self.SpinAmount.value(), self.SpinStart.value(), self.SpinEnd.value(), third, thirdPoh))
                plt.plot(mas[2][0], mas[2][1])
            else:
                mas.append(None)
            self.resultSecond(mas,20)
        plt.show()

    def resultFirst(self,functs):
        self.result = FormResult()
        if functs[0]!=None:
            self.result.tableWidget.setItem(0,0,QTableWidgetItem(str(functs[0][2])))
            self.result.tableWidget.setItem(1,0,QTableWidgetItem(str(functs[0][3])))
        else:
            self.result.tableWidget.setItem(1,0,QTableWidgetItem('---'))
        if functs[1]!=None:
            self.result.tableWidget.setItem(0,0,QTableWidgetItem(str(functs[1][2])))
            self.result.tableWidget.setItem(2,0,QTableWidgetItem(str(functs[1][3])))
        else:
            self.result.tableWidget.setItem(2,0,QTableWidgetItem('---'))
        if functs[2]!=None:
            self.result.tableWidget.setItem(0,0,QTableWidgetItem(str(functs[2][2])))
            self.result.tableWidget.setItem(3,0,QTableWidgetItem(str(fabs(functs[2][3]))))
            print(str(functs[2][3]))
        else:
            self.result.tableWidget.setItem(3,0,QTableWidgetItem('---'))
        self.result.show()

    def resultSecond(self,functs,n):
        self.table = FormTable()
        self.table.tableWidget.setColumnCount(n+1)
        self.table.tableWidget.setRowCount(12)
        k = 0
        ind = 0
        while k<len(functs): 
            r = 0
            if functs[k]!=None:
                for i in functs[k]:
                    if r == 1:
                        for j in range(len(i)):
                            self.table.tableWidget.setItem(ind,j,QTableWidgetItem(str(i[j])))
                        ind+=1
                    elif r == 2:
                        for j in range(len(i)):
                            self.table.tableWidget.setItem(ind,j,QTableWidgetItem(str(i[j])))
                        ind+=1
                    elif r == 3:
                        for j in range(len(i)):
                            self.table.tableWidget.setItem(ind,j,QTableWidgetItem(str(i[j])))
                        ind+=1
                    elif r == 4:
                        for j in range(len(i)):   
                            self.table.tableWidget.setItem(ind,j,QTableWidgetItem(str(fabs(i[j]))))
                        ind+=1
                    r+=1
            else:
                if k == 0:
                    ind += 4
                if k == 1:
                    ind += 4
                    
            k+=1
        self.table.show()


    def close(self):
        plt.close()

    def search(self, n, a, b, funct):
        N = b
        fx = []
        x = []
        mas = []
        poh =  (b-a) / n
        x.append(a)
        fx.append(funct(x[0],N))
        for i in range(1,n):
            x.append(a + i*(b - a) / n)
            fx.append(funct(x[i],N))
        temp = funct(x[0],N)
        xi = x[0]
        for i in x:
            if funct(i,N) < temp:
                xi = i
                temp = funct(i,N)
        mas = [x,fx,poh,xi]
        return mas

    def specification(self, n, a, b, funct, Poh):
        N = b
        Z = []
        eps = []
        iteration = []
        fx = []
        x = []
        xi = []
        mas = []
        optX = Poh(N)
        ii = 0
        iteration.append(0)
        x.append(a)
        fx.append(funct(x[0],N))
        eps.append(2**(-1)/(b-a)/n**0)
        Z.append(optX - x[0])
        for i in range(1,n+1):
            xmin =  a
            for k in range(0,n+1):
                xi.append(a + k*(b - a) / n)
                if(funct(xmin,N) > funct(xi[k],N)):
                    xmin = xi[k]
                    ii = k
            if(ii==0):
                a = xi[ii]
                b = xi[ii+1] 
            elif(ii==n-1):
                b = xi[ii]
                a = xi[ii-1]
            else:
                a = xi[ii-1]
                b = xi[ii+1]
            xi = []
            x.append(xmin)
            fx.append(funct(x[i],N))
            iteration.append(i)
            eps.append(2**(i-1)/(b-a)/n**i)
            Z.append(optX - x[i])
            print(x[i])
            print(fx[i])
            print(eps[i])
            print(Z[i])
        mas = [iteration,x,fx,eps,Z]
        return mas

def first(x,N):
        return (x - N / 2) ** 2

def firstPoh(N):
        return N / 2

def second(x,N):
        return (x - N / 2) ** 2 + N * x

def secondPoh(N):
        return 0

def third(x,N):
        return (x - N / 2) ** 2 + N * x ** 2

def thirdPoh(N):
        return N/(2+2*N)

def main():
    app=QtWidgets.QApplication(sys.argv)
    window=Window()
    window.show()
    app.exec_()

if __name__=="__main__":
    main()