
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




dclean = 0.    #dclean can be 0 or 1 depending upon if the data needs to be cleaned for noise
url = "https://raw.githubusercontent.com/prathampatil/lecture-spring-2025/main/data.txt"
file_path = urllib.request.urlopen(url)
data = pd.read_csv(file_path, sep='\s+', skiprows=4, header=None, names=['X','Y'])


# In[87]:


X=data['X']
Y=data['Y']


# In[88]:


if dclean == 1:
    Y = signal.savgol_filter(Y, 51, 3) # window size 51, polynomial order 3
    


# In[89]:


plt.plot(X,Y,'r')
plt.title(str(name))
plt.xlabel("Energy (eV)")
plt.ylabel("Intensity")
plt.tight_layout()

#plt.plot(X,Yhat_MXene,'b')


# In[90]:


pltname = str(name) + '.png'
plt.savefig(os.path.join(dir_path, pltname))        
plt.close('all')


# In[ ]:




