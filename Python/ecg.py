# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\CHAKA\Documents\Projet Python\ECG Processing\test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import scipy.io as so
import scipy.signal as si
import numpy
import numpy.fft as npf
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_fenetre(object):
    def setupUi(self, fenetre):
        fenetre.setObjectName("fenetre")
        fenetre.resize(998, 629)
        fenetre.setStyleSheet("background-color: rgb(0, 52, 77);\n"
"color: rgb(170, 255, 255);\n"
"")
        self.Titre = QtWidgets.QLabel(fenetre)
        self.Titre.setGeometry(QtCore.QRect(10, 10, 931, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Titre.setFont(font)
        self.Titre.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.Titre.setObjectName("Titre")
        self.line = QtWidgets.QFrame(fenetre)
        self.line.setGeometry(QtCore.QRect(10, 270, 971, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(fenetre)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 60, 721, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Graphe = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Graphe.setContentsMargins(0, 0, 0, 0)
        self.Graphe.setObjectName("Graphe")
        self.layoutWidget = QtWidgets.QWidget(fenetre)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 155, 205))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChargerEcg = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.ChargerEcg.setFont(font)
        self.ChargerEcg.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.ChargerEcg.setObjectName("ChargerEcg")
        self.verticalLayout.addWidget(self.ChargerEcg)
        self.afficheSignal = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.afficheSignal.setFont(font)
        self.afficheSignal.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.afficheSignal.setObjectName("afficheSignal")
        self.verticalLayout.addWidget(self.afficheSignal)
        self.RepFrec = QtWidgets.QPushButton(self.layoutWidget)
        self.RepFrec.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.RepFrec.setObjectName("RepFrec")
        self.verticalLayout.addWidget(self.RepFrec)
        self.SpectAmp = QtWidgets.QPushButton(self.layoutWidget)
        self.SpectAmp.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.SpectAmp.setObjectName("SpectAmp")
        self.verticalLayout.addWidget(self.SpectAmp)
        self.SpectPhase = QtWidgets.QPushButton(self.layoutWidget)
        self.SpectPhase.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.SpectPhase.setObjectName("SpectPhase")
        self.verticalLayout.addWidget(self.SpectPhase)
        self.DenSpect = QtWidgets.QPushButton(self.layoutWidget)
        self.DenSpect.setStyleSheet("background-color: rgb(0, 131, 191);")
        self.DenSpect.setObjectName("DenSpect")
        self.verticalLayout.addWidget(self.DenSpect)
        self.splitter = QtWidgets.QSplitter(fenetre)
        self.splitter.setGeometry(QtCore.QRect(30, 280, 811, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(fenetre)
        self.tabWidget.setGeometry(QtCore.QRect(20, 290, 951, 321))
        self.tabWidget.setStyleSheet("color: rgb(0, 85, 127);\n"
"background-color: rgb(170, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(10, 0, 811, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AfficheStats = QtWidgets.QPushButton(self.tab_3)
        self.AfficheStats.setGeometry(QtCore.QRect(40, 240, 391, 23))
        self.AfficheStats.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(170, 255, 255);")
        self.AfficheStats.setObjectName("AfficheStats")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 70, 391, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Moy = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Moy.setFont(font)
        self.Moy.setObjectName("Moy")
        self.gridLayout.addWidget(self.Moy, 0, 0, 1, 1)
        self.MoyVal = QtWidgets.QLabel(self.layoutWidget1)
        self.MoyVal.setText("")
        self.MoyVal.setObjectName("MoyVal")
        self.gridLayout.addWidget(self.MoyVal, 0, 1, 1, 1)
        self.Var = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Var.setFont(font)
        self.Var.setObjectName("Var")
        self.gridLayout.addWidget(self.Var, 1, 0, 1, 1)
        self.VarVal = QtWidgets.QLabel(self.layoutWidget1)
        self.VarVal.setText("")
        self.VarVal.setObjectName("VarVal")
        self.gridLayout.addWidget(self.VarVal, 1, 1, 1, 1)
        self.Max = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Max.setFont(font)
        self.Max.setObjectName("Max")
        self.gridLayout.addWidget(self.Max, 2, 0, 1, 1)
        self.MaxVal = QtWidgets.QLabel(self.layoutWidget1)
        self.MaxVal.setText("")
        self.MaxVal.setObjectName("MaxVal")
        self.gridLayout.addWidget(self.MaxVal, 2, 1, 1, 1)
        self.Min = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Min.setFont(font)
        self.Min.setObjectName("Min")
        self.gridLayout.addWidget(self.Min, 3, 0, 1, 1)
        self.MinVal = QtWidgets.QLabel(self.layoutWidget1)
        self.MinVal.setText("")
        self.MinVal.setObjectName("MinVal")
        self.gridLayout.addWidget(self.MinVal, 3, 1, 1, 1)
        self.EType = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EType.setFont(font)
        self.EType.setObjectName("EType")
        self.gridLayout.addWidget(self.EType, 4, 0, 1, 1)
        self.ETypeVal = QtWidgets.QLabel(self.layoutWidget1)
        self.ETypeVal.setText("")
        self.ETypeVal.setObjectName("ETypeVal")
        self.gridLayout.addWidget(self.ETypeVal, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 811, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.AfficheEng = QtWidgets.QPushButton(self.tab_4)
        self.AfficheEng.setGeometry(QtCore.QRect(40, 250, 421, 23))
        self.AfficheEng.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(170, 255, 255);")
        self.AfficheEng.setObjectName("AfficheEng")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget2.setGeometry(QtCore.QRect(40, 80, 421, 161))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Eng = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Eng.setFont(font)
        self.Eng.setObjectName("Eng")
        self.gridLayout_2.addWidget(self.Eng, 0, 0, 1, 1)
        self.EngVal = QtWidgets.QLabel(self.layoutWidget2)
        self.EngVal.setText("")
        self.EngVal.setObjectName("EngVal")
        self.gridLayout_2.addWidget(self.EngVal, 0, 1, 1, 1)
        self.PuiMoy = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PuiMoy.setFont(font)
        self.PuiMoy.setObjectName("PuiMoy")
        self.gridLayout_2.addWidget(self.PuiMoy, 1, 0, 1, 1)
        self.PuiMoyVal = QtWidgets.QLabel(self.layoutWidget2)
        self.PuiMoyVal.setText("")
        self.PuiMoyVal.setObjectName("PuiMoyVal")
        self.gridLayout_2.addWidget(self.PuiMoyVal, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 50, 681, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.CorrGraph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.CorrGraph.setContentsMargins(0, 0, 0, 0)
        self.CorrGraph.setObjectName("CorrGraph")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget3.setGeometry(QtCore.QRect(750, 60, 181, 191))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FiltEncG = QtWidgets.QPushButton(self.layoutWidget3)
        self.FiltEncG.setStyleSheet("background-color: rgb(0, 131, 191);\n"
"color: rgb(170, 255, 255);")
        self.FiltEncG.setObjectName("FiltEncG")
        self.verticalLayout_2.addWidget(self.FiltEncG)
        self.FiltEncPH = QtWidgets.QPushButton(self.layoutWidget3)
        self.FiltEncPH.setStyleSheet("background-color: rgb(0, 131, 191);\n"
"color: rgb(170, 255, 255);")
        self.FiltEncPH.setObjectName("FiltEncPH")
        self.verticalLayout_2.addWidget(self.FiltEncPH)
        self.FiltPB = QtWidgets.QPushButton(self.layoutWidget3)
        self.FiltPB.setStyleSheet("background-color: rgb(0, 131, 191);\n"
"color: rgb(170, 255, 255);\n"
"")
        self.FiltPB.setObjectName("FiltPB")
        self.verticalLayout_2.addWidget(self.FiltPB)
        self.FiltD = QtWidgets.QPushButton(self.layoutWidget3)
        self.FiltD.setStyleSheet("background-color: rgb(0, 131, 191);\n"
"color: rgb(170, 255, 255);")
        self.FiltD.setObjectName("FiltD")
        self.verticalLayout_2.addWidget(self.FiltD)
        self.Tnl = QtWidgets.QPushButton(self.layoutWidget3)
        self.Tnl.setStyleSheet("background-color: rgb(0, 131, 191);\n"
"color: rgb(170, 255, 255);")
        self.Tnl.setObjectName("Tnl")
        self.verticalLayout_2.addWidget(self.Tnl)
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setGeometry(QtCore.QRect(40, 0, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(fenetre)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(fenetre)
        self.ChargerEcg.clicked.connect(self.getSignal)
        self.afficheSignal.clicked.connect(self.plot)
        self.RepFrec.clicked.connect(self.plotFrec)
        self.AfficheStats.clicked.connect(self.PropStats)
        self.AfficheEng.clicked.connect(self.PropEng)

        self.SpectAmp.clicked.connect(self.plotAmp)
        self.SpectPhase.clicked.connect(self.plotPhase)

        self.DenSpect.clicked.connect(self.densiteSpect)

        self.FiltEncG.clicked.connect(self.FiltreEncocheGain)
        self.FiltEncPH.clicked.connect(self.FiltreEncochePhase)
        self.FiltPB.clicked.connect(self.FiltrePasseBande)
        self.FiltD.clicked.connect(self.FiltreDerivateur)
        self.Tnl.clicked.connect(self.TransNline)



        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.Graphe.addWidget(self.canvas)

        self.canvas1 = FigureCanvas(self.figure)
        self.CorrGraph.addWidget(self.canvas1)



    def plot(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        t = numpy.linspace(0,duration,N)

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(t,ecg.T)
        # refresh canvas
        self.canvas.draw()
    def plotFrec(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        t = numpy.linspace(0,duration,N)

        tf = npf.fft(ecg)
        f1 = numpy.arange(N)/(t[1]*N)
        a = (tf)/N

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(f1,a.T)
        # refresh canvas
        self.canvas.draw()
    def plotAmp(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        t = numpy.linspace(0,duration,N)

        tf = npf.fft(ecg)
        f1 = numpy.arange(N)/(t[1]*N)
        a = numpy.absolute(tf)/N

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(f1,a.T)
        # refresh canvas
        self.canvas.draw()
    def plotPhase(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        t = numpy.linspace(0,duration,N)

        tf = npf.fft(ecg)
        f1 = numpy.arange(N)/(t[1]*N)
        a = numpy.angle(tf)/N

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(f1,a.T)
        # refresh canvas
        self.canvas.draw()



    def getSignal(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        if filePath != "":
            print ("Repertoire",filePath)
            self.signal = so.loadmat(str(filePath))


    def PropStats(self):
        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        self.MoyVal.setText(str(numpy.mean(ecg)))
        self.MinVal.setText(str(numpy.min(ecg)))
        self.MaxVal.setText(str(numpy.max(ecg)))
        self.VarVal.setText(str(numpy.var(ecg)))
        self.ETypeVal.setText(str(numpy.std(ecg)))

    def PropEng(self):
        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        tf = npf.fft(ecg)

        energie=abs(ecg)**2
        energie=energie.sum()
        puissance=energie/N

        self.EngVal.setText(str(energie)+" Joule (s)")
        self.PuiMoyVal.setText(str(puissance)+" Watt(s)")
    def densiteSpect(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration

        f2, psd= si.periodogram(ecg,Fs)
        #plt.subplot(713)

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.semilogy(f2,psd.T)
        # refresh canvas
        self.canvas.draw()
    def SpectPuiss(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration

        f2, psd= si.periodogram(ecg,Fs)
        #plt.subplot(713)

        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.semilogy(f2,numpy.sqrt(psd.T))
        # refresh canvas
        self.canvas.draw()

    def FiltreEncocheGain(self):
        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration

        ax = self.figure.add_subplot(111)

        i,j = si.freqz(ecg.T)
        

        # create an axis
        

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(i/(2*numpy.pi),50*numpy.log10(numpy.absolute(j)))
        ax.grid()
        # refresh canvas
        self.canvas1.draw()

    def FiltreEncochePhase(self):
        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration

        ax = self.figure.add_subplot(111)

        i,j = si.freqz(ecg.T)
        

        # create an axis
        

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        ax.plot(i/(2*numpy.pi),numpy.unwrap(numpy.angle(j)))
        ax.grid()
        # refresh canvas
        self.canvas1.draw()

    def FiltrePasseBande(self):
        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration
        t = numpy.linspace(0,duration,N)
        i,j = si.freqz(ecg.T)

        ax = self.figure.add_subplot(111)

        n = ecg*si.get_window("hamming",ecg.size)
        w,h=si.freqz(n.T)
        #ax.stem(n.T)
        ax.plot(t,n.T)
        
        

        # discards the old graph
        ax.hold(False) # deprecated, see above

        # plot data
        self.canvas1.draw()

    def FiltreDerivateur(self):

        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration

        ax = self.figure.add_subplot(111)
        te=1.0/Fs
        t = numpy.arange(0,10,te)
        c=[te]
        d=[1,-1]
        n = ecg*si.get_window("hamming",ecg.size)
        y = si.lfilter(d,c,n.T)        

        # create an axis
        

        # discards the old graph
        ax.hold(False) # deprecated, see above

        ax.plot(t,y,"")

        # refresh canvas
        self.canvas1.draw()

    def TransNline(self):
        duration = 10
        ecg = (self.signal["val"]-1024)/200
        Fs = 360
        N = Fs*duration

        ax = self.figure.add_subplot(111)
        te=1.0/Fs
        t = numpy.arange(0,10,te)
        c=[te]
        d=[1,-1]
        n = ecg*si.get_window("hamming",ecg.size)
        y = si.lfilter(d,c,n.T) 
        

        r = y*y

        ax.hold(False) 

        ax.plot(t,r)
    
        self.canvas1.draw()

    def retranslateUi(self, fenetre):
        _translate = QtCore.QCoreApplication.translate
        fenetre.setWindowTitle(_translate("fenetre", "Analyse de Signaux ECG"))
        self.Titre.setText(_translate("fenetre", "                 Analyse de signaux des Electrocardiogrammes"))
        self.ChargerEcg.setText(_translate("fenetre", "Charger ECG"))
        self.afficheSignal.setText(_translate("fenetre", "Afficher Signal"))
        self.RepFrec.setText(_translate("fenetre", "Representation Frequentielle"))
        self.SpectAmp.setText(_translate("fenetre", "Spectres d\'Amplitudes"))
        self.SpectPhase.setText(_translate("fenetre", "Spectres de Phases"))
        self.DenSpect.setText(_translate("fenetre", "Densité Spectrale"))
        self.label.setText(_translate("fenetre", ". Propriétes Statistiques"))
        self.AfficheStats.setText(_translate("fenetre", "Afficher les Propriétés Statistiques"))
        self.Moy.setText(_translate("fenetre", "Moyenne"))
        self.Var.setText(_translate("fenetre", "Variance"))
        self.Max.setText(_translate("fenetre", "Maximum"))
        self.Min.setText(_translate("fenetre", "Minimum"))
        self.EType.setText(_translate("fenetre", "Ecart Type"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("fenetre", "Propriétés Statistiques"))
        self.label_12.setText(_translate("fenetre", ". Propriétes Enérgétiques"))
        self.AfficheEng.setText(_translate("fenetre", "Afficher Propriétés Enérgétiques"))
        self.Eng.setText(_translate("fenetre", "Enérgie"))
        self.PuiMoy.setText(_translate("fenetre", "Puissance Moyenne"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("fenetre", "Propriétés Enérgétiques"))
        self.FiltEncG.setText(_translate("fenetre", "Filtre a encoche (Gain)"))
        self.FiltEncPH.setText(_translate("fenetre", "Filtre a encoche (Phase)"))
        self.FiltPB.setText(_translate("fenetre", "Filtre Passe Bande"))
        self.FiltD.setText(_translate("fenetre", "Filtre Dérivateur"))
        self.Tnl.setText(_translate("fenetre", "Transformé Non-Lineaire"))
        self.label_2.setText(_translate("fenetre", ".Filtres"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("fenetre", "Filtres"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fenetre = QtWidgets.QDialog()
    ui = Ui_fenetre()
    ui.setupUi(fenetre)
    fenetre.show()
    sys.exit(app.exec_())

