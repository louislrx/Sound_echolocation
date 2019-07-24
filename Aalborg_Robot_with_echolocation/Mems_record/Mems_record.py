#IMPORT
import serial
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import wave
import sys
import sounddevice as sd

#SETUP
try:
    arduino = serial.Serial('COM14', baudrate=500000, timeout=None)
except:
    print("verifier le port serie utilisé")

#VARIABLES
rawdata=[]
compt=0



while compt<25000:
    rawdata.append(str(arduino.readline()))
    compt+=1

#FUNCTIONS
def nettoie(L):
    newL=[]
    for i in range(len(L)):
        temp=L[i][2:]
        newL.append(temp[:-5])
    return newL

def write(L):
    blanks=0
    file=open("data.txt",mode="w")
    for i in range(1, len(L)-2):
        if L[i] != '':
            file.write(L[i]+'\n')
        else:
            blanks+=1
    file.write(L[len(L)-1])
    file.close()
    return blanks


def Clean_array(myarray):

    return myarray
#MAIN
cleandata=nettoie(rawdata)
print(cleandata)

blanks_nb = write(cleandata)

#If we want to plot the data of the recorded microphones
#vals1,vals2=np.loadtxt("data.txt",delimiter=";",unpack=True)
#vals1=np.loadtxt("data.txt", unpack=True)
sr = 80
dur = (len(cleandata)-2-blanks_nb)/sr
print(len(vals1))
t=np.arange(0, dur, 1/sr)
plt.figure(figsize = (10,8))
plt.subplot(3, 1, 1)
plt.plot(t,vals1, 'b')
plt.plot(t,vals2, 'r')
plt.subplot(3, 1, 2)
plt.plot(t,vals1, 'b')
plt.subplot(3, 1, 3)
plt.plot(t,vals2, 'r')
plt.show()

#read_audio(vals1)

