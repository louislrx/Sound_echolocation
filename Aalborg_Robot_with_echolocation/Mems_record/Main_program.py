import serial
from serial import *
import time
import io
import serial
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import wave
import sys
import sounddevice as sd

temps=time.time()   #define the time
temps2=time.time()
i=0

def Mems_record(datatxt):   #here is the function to record the microphone mems
        rawdata=[]  #array which stock the data
        compt=0



        while compt<25000:                          #while loop to say how much value do we want
            rawdata.append(str(STM32.readline()))   #we stock on rawdata the readed data
            compt+=1

        #FUNCTIONS
        def nettoie(L):             #function which clean the data to have just values
            newL=[]
            for i in range(len(L)):
                temp=L[i][2:]
                newL.append(temp[:-5])
            return newL

        def write(L):               #function which whrite the data in a text file
            blanks=0
            file=open(datatxt,mode="w")
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

        blanks_nb = write(cleandata)

        vals1,vals2=np.loadtxt(datatxt,delimiter=";",unpack=True)


entry = '0'
while(time.time()-temps<180):   #We are running the program for 3min


    if(entry!='r'):
        entry = input("press r to record and m to move the robot Or s to stop the program") #We ask the user to enter the command

    temps2=time.time()

    if (entry == "m"):
            try:
                arduino = serial.Serial('COM3', baudrate=115200, timeout=None)  #initialisation of the arduino for the robot
                while (time.time()-temps2<10):  #we move the robot for 10s max
                    nombre = input("press 8(forward), 2(backward), 4(left), 6(right), 0(stop), r to record and stop the robot")
                    arduino.write(nombre.encode('ascii'))
                    if(nombre == 'r'):
                        entry = nombre  #If we want to record, we go out of the loop and record
                        break
                arduino.close()#close the serial
            except:
                print("check the serial port")

    elif (entry == "r"):
            try:
                arduino.open()      #we stop the robot before recording
                arduino.write(str(0).encode('ascii'))
                arduino.close()
                STM32 = serial.Serial('COM14', baudrate=500000, timeout=None)   #We need to move the robot one time before recording, after we can record when we want
                datatxt = "data{}.txt".format(i+1)  #We loading the data on a text file. The text file is different for each recording
                Mems_record(datatxt)    # Recording
                STM32.close()   #close the serial
                i+=1
                entry='0'
            except:
                print("check the serial port")

    elif (entry == "s"):
        sys.exit()#exit the program
