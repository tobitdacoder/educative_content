import pandas as pd       # data manipulation, querying, data cleansing and preprocessing 
import numpy as np      # arrays, matrices and other math 
from matplotlib import pyplot as plt     # this is the one we use for ploting, creating graphs, animating, graphs
                                                                # this pyplot is used for basic 
                                                                
pair_of_shoes = 200 + np.random.randn(100)  # pair of shoes sold in undred days (that 100 is the number of days on which we are doing the study)
                                                                          # here the 200 means, the maximum number of show that can be sold in  a day  for this specific study (the y axis max)
day = [day for day in range(100)] # this 100 here is that number of days on which we want to study our sales 

plt.plot(day,pair_of_shoes,"-") # this is for ploting 
plt.fill_between(day,pair_of_shoes,195,where=(pair_of_shoes>195), facecolor="green", alpha=0.5)
plt.title("UCU Datascience Lab 1 - Visualization")

plt.show()