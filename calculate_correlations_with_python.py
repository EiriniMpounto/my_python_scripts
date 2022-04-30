'''
Author: Irene Bounto
'''
'''
The current algorithm is going to be created in order 
to calculate the correlation between two variables with
two possible ways, Pearson correlation and Spearman correlation
'''

# Step_1: IMPORTING ALL THE LIBRARIES NEEDED
import statistics
import random
import pandas as pd
import numpy as np
from statistics import stdev
from scipy.stats import pearsonr
from scipy.stats import spearmanr

# Steo_2: READ YOUR DATASET OR GENERATE A RANDOM ONE
# HERE WE ARE GENERATING ONE RANDOM DATAFRAME
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
print(df)

# setting up the data columns we want to correlate
data_a = df['A']
data_b = df['B']

# Step_3: BEFORE WE CALCULATE THE CORRELATIONS
# WE ARE GOING TO CALCULATE THE MEAN AND THE 
# STANDARD DEVIATION OF BOTH DATA VARIABLES
data_a_mean = statistics.mean(data_a)
data_a_std = statistics.stdev(data_a)

data_b_mean =statistics.mean(data_b)
data_b_std = statistics.stdev(data_b)

#preparing the data
data1 = data_a_mean * data_a +data_a_std
data2 = data1 + (data_b_mean * data_b +data_b_std)
# calculating the correlation
corr, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)
# alternative way of calculating the correlation
corr, _ = spearmanr(data_a, data_b)
print('Spearmans correlation: %.3f' % corr)


