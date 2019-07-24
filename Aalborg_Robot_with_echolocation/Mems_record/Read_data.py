import serial
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import wave
import sys
import sounddevice as sd
import math
import time
import binascii


#var
readData1=[]
readData2=[]

def read_audio(x):      #function pyaudio, to read the text file
    array_wave=[]
    xs=x*2**14
    print("len x = ", len(x))
    print("len xs = ", len(xs))

    CHUNK = 128
    sr = int(500000/(CHUNK))    #to have the sample rate, we need to divied the baud rate by the chunk
    n_channels = 1
    lendata = len(x)
    audioOutidx = np.arange(CHUNK)
    format = pyaudio.paInt16

    # instantiate PyAudio

    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format = format,
                    channels = n_channels,
                    rate = sr,
                    output=True,
                    frames_per_buffer = CHUNK)


    for i in range (0 , math.floor(lendata/CHUNK)):
        if (audioOutidx[0]<(lendata-CHUNK)):
            play_data=xs[audioOutidx].astype(np.int16).tostring()

            stream.write(play_data)
            array_wave.append(play_data)
            audioOutidx = audioOutidx + CHUNK


    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
    return array_wave


def write_Wave(data):   #here is the function to create a wave file of the data text file
    CHUNK = 128
    sr = int(500000/(CHUNK))
    obj = wave.open('sound.wav','wb')
    obj.setnchannels(1) # mono
    obj.setsampwidth(2)
    obj.setframerate(sr)
    obj.writeframesraw(b''.join(data))
    obj.close()


#reading of the files

readData1,readData2=np.loadtxt("data1.txt",delimiter=";",unpack=True)
readData1/=max(readData1)
readData2/=max(readData2)
print(len(readData1))

array_wave1=read_audio(readData1)
time.sleep(3)
array_wave2=read_audio(readData2)

print(array_wave1)
write_Wave(array_wave1)

import winsound
winsound.PlaySound('sound.wav',winsound.SND_FILENAME)



