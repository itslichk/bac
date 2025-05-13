from PyQt5.QtWidgets import *
from PyQt5.uic import*
from math import sqrt
from numpy import array



def differ(ch):
    x = 0
    while i < len(ch) and x<3:
        for j in range(0,i):
            if 'A'<= ch[i] <='F':
                if ch[i] != ch[j] :
                    x += 1
                i+= 1
    return x<3
            
def premier(x):
    b = True
    i = 2
    while i < sqrt(x) or b:
        if x%i == 0:
            b = False
        else : i+= 1
    return b
        
def paland(x):
    w = str(x)
    b = True
    i = 0
    while i < len(w)/2 and b:
        if w[i] != w[len(x)-i]:
            b = False
        else : i +=1
    return b
            
            
def ajouter():
    ln1 = w.ln1.text()
    min = w.comboBox.currentText()
    if len(ln1) < int(min) or differ(ln1) :QMessageBox.critical (w,'error','HEX est invalide')
    else:
        f = open('data.bin', 'ab')
        e={}
        e['comp'] = complement(ln1)
        e['decimal'] = conv16to10(e['comp'])
        if w.r1.isChecked():
            e['clef'] = premier(e['decimal'])
        if w.r2.isChecked():
            e['clef'] = paland(e['decimal'])
        f.dump(e)
        close(f)
        QMessageBox.information(w,'success','Element ajoute avec succes')
        
        
        
def complement (x):
    ch=''
    for i in range(len(x)):
        ch = ch + conv10to16(15 - conv16to10(x[i]))
    return ch
def conv16to10(ch):
    x = 0
    for i in range(len(ch)):
        if ch[i] >= 'A' :
            x = ((ord(ch[i])-55) * pow(16,(len(ch)-i))) + x
        else :
            x = (int(ch[i]) * pow(16,(len(ch)-i)))  + x
    return x

def trier(t,n):
    for i in range(n):
        for j in range(i+1,n):
            if t[i] > t[j]:
                x = t[i]
                t[i] = t[j]
                t[j] = x
    return t

def generer():
    t = array()
    f = open('data.bin', 'rb')
    b = True
    i = 0
    while b:
        try:
            load(f,e)
            t[i] = e['clef']
            i += 1
        except:
            b = False
    close(f)
    trier(t,i)
    f = open('list_clefs.txt', 'w')
    for j in range(i):
        f.write(str(t[i])+"\n")
    close(f)

def lister():
    f = open('list_clefs.txt', 'r')
    i = 0
    e = readline(f)
    while e != '':
        w.lw2.addItem(e)
    close(f)

def chercher():
    
    
def conv10to16(nb) :
    x = ''
    while (nb > 0):
        if nb%16 <10:
            x = str( nb % 16 )+x
        else :
            x = str( chr(nb % 16 +55 ))+x
        nb = nb/16
        
    return x

def afficher () :
    b = True
    i = 0
    f = open('data.bin','rb')
    while b:
        try:
            load(f,e)
            insertRow(i)
            setItem(i,0,QTableWidgetItem(e['comp']))
            setItem(i,1,QTableWidgetItem(e['decimal']))
            setItem(i,2,QTableWidgetItem(e['clef']))
        except:
            b=False
    close(f)
        
app = QApplication([])
w= loadUi('interface_Clef.ui')
# les connections
w.nom_bt1.clicked.connect(ajouter)
w.nom_bt2.clicked.connect(afficher)
w.nom_bt5.clicked.connect(generer)
w.nom_bt4.clicked.connect(lister)
w.show()
app.exec_()
