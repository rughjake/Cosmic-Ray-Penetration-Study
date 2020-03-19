#by Jake Rugh
#jakerugh@ucsb.edu
"""
Usage: read output text files from CRP_dataCollect.py and create
histograms of the results
"""
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
y_error = []
x_av = [0, 1, 2, 3, 4]
y_av = []
y_av_error = []

for n in range(10):
    text = "CRPdata" + str(n) + ".txt"
    file = open(text, "r")
    content = file.readlines()
    rate = content[-2]
    rate = rate.split(" ")
    rate = rate[3]
    rate = float(rate)
    y.append(rate)
    file.close()
    if n == 0 or n == 9:
        x.append(0)
    elif n == 1 or n == 2:
        x.append(1)
    elif n == 3 or n == 4:
        x.append(2)
    elif n == 5 or n == 6:
        x.append(3)
    else:
        x.append(4)
    error = rate / 10
    y_error.append(error)
    
plt.errorbar(x, y, y_error, capsize=2, fmt="o")
plt.title("Raw Detection Rates\n vs\n Layers of Aluminum Foil Used")
plt.xlabel("Layers of Aluminum Foil")
plt.ylabel("Detection Rate (Hz)")
plt.show()

for n in range(5):
    index = 0
    average = 0
    error = 0
    for a in x:
        if a == n:
            average += y[index]
            error += y_error[index]**2
        index += 1
    average /= 2
    error = np.sqrt(error) / 2
    y_av.append(average)
    y_av_error.append(error)
    
    

plt.errorbar(x_av, y_av, y_av_error, capsize=2, fmt="o")
plt.title("Average Detection Rates\n vs\n Layers of Aluminum Foil Used")
plt.xlabel("Layers of Aluminum Foil")
plt.ylabel("Average Detection Rate (Hz)")
plt.show()

file = open("CRPdata9.txt", "r")
content = file.readlines()
rate = content[-2]
rate = rate.split(" ")
rate = rate[3]
rate = float(rate)
y_av[0] = rate
y_av_error[0] = rate / 10
file.close()   

plt.errorbar(x_av, y_av, y_av_error, capsize=2, fmt="o")
plt.title("Average Detection Rates\n vs\n Layers of Aluminum Foil Used (No Outlier)")
plt.xlabel("Layers of Aluminum Foil")
plt.ylabel("Average Detection Rate (Hz)")
plt.show()