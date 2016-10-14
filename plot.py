from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt

def plot(array):
    print(array)
    to_plot = [((item*(180/(2*math.pi)))+180)/360 for item in array]
    print(to_plot)
    plt.imshow(to_plot, cmap='gist_rainbow', interpolation='nearest')
    plt.show()
