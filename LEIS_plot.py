
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import tkinter as tk
from tkinter import filedialog
import os
import urllib.request
import scipy

from scipy import signal

x_data = []
y_data = []


dclean = 0.    #dclean can be 0 or 1 depending upon if the data needs to be cleaned for noise
url = "https://raw.githubusercontent.com/prathampatil/lecture-spring-2025/main/data.txt"
response = urllib.request.urlopen(url)
lines = response.read().decode('utf-8').splitlines()
for line in lines:
    x, y = map(float, line.strip().split())
    x_data.append(x)
    y_data.append(y)



# In[87]:


X= x_data
Y= y_data


# In[88]:


if dclean == 1:
    Y = signal.savgol_filter(Y, 51, 3) # window size 51, polynomial order 3
    


# In[89]:


plt.plot(X,Y,'r')
plt.title("LEIS Plot")
plt.xlabel("Energy (eV)")
plt.ylabel("Intensity")
plt.tight_layout()
plt.show()

print("Plotting Successful")






# In[ ]:




