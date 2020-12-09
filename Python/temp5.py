# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 17:14:03 2019

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 14:34:36 2018

@author: HP
"""
import math
import scipy.io as so
import scipy.signal as si
import numpy
import numpy.fft as npf
import matplotlib.pyplot as plt

#affichage du signal
signal = so.loadmat('100m.mat')
duration = 10
ecg = (signal["val"]-1024)/200
sig2 = so.loadmat('101m.mat')
ecg2 = (sig2["val"]-1024)/200
Fs = 360
N = Fs*duration
t = numpy.linspace(0,duration,N)

plt.plot(t,ecg.T)
#affichage du spectre des fréquences
tf = npf.fft(ecg)
f1 = numpy.arange(N)/(t[1]*N)
a = numpy.absolute(tf)/N

plt.plot(f1,a.T)
plt.grid()

#densité spectrale
f2, psd= si.periodogram(ecg,Fs)

plt.semilogy(f2,psd.T)

#spectre de puissance
plt.semilogy(f2,numpy.sqrt(psd.T))
numpy.sqrt(psd.max())

#Calcul de la moyenne du signal
moy = numpy.mean(ecg)

#Correlation du signal
p = numpy.correlate(numpy.reshape(ecg,len(ecg.T)),numpy.reshape(ecg2,len(ecg2.T)))

#Utilisation filtres
#REPONSE FREQUENTIELLE: FILTRE à ENCOCHE
'''
Pour éliminer efficacement les interférences, localisées à une fréquence bien 
définie et connue, on peut implanter un filtre à encoche qui élimine cette composante
fréquentielle et ce de la manière la plus sélective qui soit
'''
i,j = si.freqz(ecg.T)
plt.figure()
plt.stem(ecg.T)

plt.plot(i/(2*numpy.pi),50*numpy.log10(numpy.absolute(j)))
plt.xlabel("f/Fs")
plt.ylabel("GdB")
plt.grid()

plt.plot(i/(2*numpy.pi),numpy.unwrap(numpy.angle(j)))
plt.xlabel("f/Fs")
plt.ylabel("Phase")
plt.grid()


#ALGORITHME DE DETECTION DES PICS
#APPLICATION DU FILTRE PASSE BANDE

n = ecg*si.get_window("hamming",ecg.size)
w,h=si.freqz(n.T)
plt.stem(n.T)
plt.plot(t,n.T)
plt.title("APPLICATION DU FILTRE PASSE BANDE SUR 100m")
plt.subplot(211)
plt.plot(w/(2*numpy.pi),20*numpy.log10(numpy.absolute(h)))
plt.xlabel("f/fe")
plt.ylabel("GdB")
plt.grid()
plt.subplot(212)
plt.plot(w/(2*numpy.pi),numpy.unwrap(numpy.angle(h)))
plt.title("Application du filtre Passe Bande")
plt.xlabel("f/fe")
plt.ylabel("phase")
plt.grid()


#APPLICATION DU FILTRE DERIVATEUR

Fs = 360
te=1.0/Fs
t = numpy.arange(0,10,te)
c=[te]
d=[1,-1]
y = si.lfilter(d,c,n.T)
plt.figure()
plt.plot(t,y,"")
plt.title("Application du filtre dérivateur")
plt.xlabel('t')
plt.ylabel('y')

#APPLICATION D'UNE TRANSFORMEE NON LINEAIRE
r = y*y
plt.figure()
plt.plot(t,r)
plt.title("Apllication de la transformée non linéaire")
plt.xlabel('t')
plt.ylabel('r')

#APPLICATION D'UNE INTEGRATION SUR LE SIGNAL


#APPLICATION DU FILTRE PASSE BAS:

#APPLICATION DU SEUILLAGE ADAPTATIF:













