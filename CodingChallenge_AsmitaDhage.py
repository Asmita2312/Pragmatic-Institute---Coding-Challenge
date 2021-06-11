import numpy as np
import pandas as pd
import sys
import statistics

def running_mean(arr, N):
    running_mean = sum(arr[0:N]) / N
    return round(running_mean,2)

def running_std(arr):
    running_std = np.std(arr)
    return round(running_std,2)

def running_median(arr):
    running_median = statistics.median(arr)
    return round(running_median, 2)


inputFile = open('C:/Users/Administrator/Desktop/input.txt', "r")
input_array = []

try:
    for line in inputFile:
        output = []
        input_array.append(float(line.rstrip('\n')))
        N = len(input_array)

        mean = running_mean(input_array,N)
        std = running_std(input_array)
        median = running_median(input_array)
        print(mean, ', ', std, ', ', median)
        
except ValueError:
    print("No valid number in line.")
    
inputFile.close()
