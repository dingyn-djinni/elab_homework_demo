
# -*- coding: utf-8 -*-
# author:djinni
# 一款仅实现基本的加减乘除括号功能的科学计算器，没怎么测试过，可能有bug
# development enviroment：ubuntu18.04+python3.6+pyqt5

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import sys
from calculator import Ui_calculator     # 导入生成form.py里生成的类
from PyQt5 import QtCore
from PyQt5.QtCore import *

class mywindow(QtWidgets.QWidget,Ui_calculator):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)
    sigdic={'(':0,'+':1,'-':1,'*':2,'/':2}
    
    inputText=""	
    
     # 检测键盘回车按键，函数名字不要改，这是重写键盘事件
    def keyPressEvent(self, event):
        #这里event.key（）显示的是按键的编码
        print("按下：" + str(event.key()))
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感
        if (event.key() == Qt.Key_Escape):
            exit(0)
        if (event.key() == Qt.Key_1):
            self.pressButton1()
        if (event.key() == Qt.Key_2):
            self.pressButton2()
        if (event.key() == Qt.Key_3):
            self.pressButton3()
        if (event.key() == Qt.Key_4):
            self.pressButton4()
        if (event.key() == Qt.Key_5):
            self.pressButton5()
        if (event.key() == Qt.Key_6):
            self.pressButton6()
        if (event.key() == Qt.Key_7):
            self.pressButton7()
        if (event.key() == Qt.Key_8):
            self.pressButton8()
        if (event.key() == Qt.Key_9):
            self.pressButton9()
        if (event.key() == Qt.Key_0):
            self.pressButton0()
        if (event.key() == Qt.Key_0):
            self.pressButton0()
            
        # 当需要组合键时，要很多种方式，这里举例为“shift+单个按键”，也可以采用shortcut、或者pressSequence的方法。
        # 61, 16777220:enter
        if (event.key() == 61 or event.key()==16777220):
                self.pressButtonEnter()
                
        if (event.key() == 43):
            self.pressButtonPlus()
            
        if (event.key() == 95):
            self.pressButtonSub()
            
        if (event.key() == 42):
            self.pressButtonMult()
            
        if (event.key() == 47):
            self.pressButtonDevide()
            
        if (event.key() == 46):
            self.pressButtonDot()
        # del    
        if (event.key() == 16777219):
            self.pressButtonDel()
            
        if (event.key() == 67):
            self.pressButtonCE()

        if (event.key() == 40):
            self.pressButtonLparent()

        if (event.key() == 41):
            self.pressButtonRparent()
            
	#输入函数,参数为输入框内容
    def textInput(self,a):
        self.inputText=self.inputText+a
        self.textEdit.setText(self.inputText)

    #计算逆波兰式，参数为逆波兰式
    def calc(self,a):
        calcSt=[]
        for i in a:
            if i =='+':
                calcSt[-2]=calcSt[-2]+calcSt[-1]
                calcSt=calcSt[:-1]
            elif i =='-':
                calcSt[-2]=calcSt[-2]-calcSt[-1]
                calcSt=calcSt[:-1]
            elif i =='*':
                calcSt[-2]=calcSt[-2]*calcSt[-1]
                calcSt=calcSt[:-1]
            elif i =='/':
                calcSt[-2]=calcSt[-2]/calcSt[-1]
                calcSt=calcSt[:-1]
            else:
                calcSt.append(i)
        print(calcSt[0])
        return calcSt[0]
    #定义槽函数
    def pressButton1(self):
        self.textInput("1")
    def pressButton2(self):
        self.textInput("2")
    def pressButton3(self):
        self.textInput("3")
    def pressButton4(self):
       	self.textInput("4")
    def pressButton5(self):
       	self.textInput("5")
    def pressButton6(self):
       	self.textInput("6")
    def pressButton7(self):
       	self.textInput("7")
    def pressButton8(self):
       	self.textInput("8")
    def pressButton9(self):
       	self.textInput("9")
    def pressButton0(self):
       	self.textInput("0")
    def pressButtonCE(self):
       	self.inputText=""
        self.textEdit.setText(self.inputText)
    def pressButtonDot(self):
       	self.textInput(".")
    def pressButtonLparent(self):
        self.textInput("(")
    def pressButtonRparent(self):
        self.textInput(")")
    def pressButtonEnter(self):
        num=0
        numflag=0
        dotflag=0
        outputQue=[]
        sigSt=[]
        lpnum=0
        for i in self.inputText:
            if ord(i)>=48 and ord(i)<=57:
                numflag=1
                if dotflag==0:
                    num=num*10+(ord(i)-48)
                    continue
                else:
                    num=num+(ord(i)-48)/(pow(10,dotflag))
                    dotflag=dotflag+1
                    continue
            if i=='.':
                dotflag=1
                continue
            if numflag==1:
                outputQue.append(num)
                numflag=0
            num=0
            dotflag=0
            if i=='+' or i=='-':
                while len(sigSt)!=0:
                    if self.sigdic[sigSt[-1]]>=1:
                        outputQue.append(sigSt[-1])
                        sigSt=sigSt[:-1]
                    else:
                        break
                sigSt.append(i)
            elif i=='*' or i=='/':
                while len(sigSt)!=0:
                    if self.sigdic[sigSt[-1]]>=2:
                        outputQue.append(sigSt[-1])
                        sigSt=sigSt[:-1]
                    else:
                        break
                sigSt.append(i)    
            elif i=='(':
                sigSt.append(i)
                lpnum=lpnum+1
            elif i==')':
                while sigSt[-1]!='(':
                    outputQue.append(sigSt[-1])
                    sigSt=sigSt[:-1]
                sigSt=sigSt[:-1]
                lpnum=lpnum-1
            else:
                reply = QMessageBox.information(self,"error","invalid charcter",QMessageBox.Yes | QMessageBox.No)
                return
        if lpnum!=0:
            reply = QMessageBox.information(self,"error","parent mismatch",QMessageBox.Yes | QMessageBox.No)
            return                 
        if numflag==1:
            outputQue.append(num)
            numflag=0
        while len(sigSt)!=0:
            outputQue.append(sigSt[-1])
            sigSt=sigSt[:-1]
        print(outputQue)
        try:
            ans=self.calc(outputQue)
        except:
            reply = QMessageBox.information(self,"error","calculate error",QMessageBox.Yes | QMessageBox.No)
            return
        self.inputText=str(ans)
        self.textEdit.setText(self.inputText)
    def pressButtonPlus(self):
        self.textInput("+")
    def pressButtonSub(self):
        self.textInput("-")
    def pressButtonMult(self):
        self.textInput("*")
    def pressButtonDevide(self):
        self.textInput("/")
    def pressButtonDel(self):
        if len(self.inputText)!=0:
            self.inputText=self.inputText[:-1]
            self.textEdit.setText(self.inputText)
       

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
