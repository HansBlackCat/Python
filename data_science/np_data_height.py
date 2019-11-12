import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
from scipy import special

data=pd.read_csv('./data/president_heights.csv')
heights=np.array(data['height(cm)'])
print(heights)

print("Mean               = ",heights.mean())
print("Standard deviation = ",heights.std())
print("Minimum  height    = ",heights.min())
print("Maximum height     = ",heights.max())
print("25 perc            = ",np.percentile(heights,25))
print("Median             = ",np.median(heights))
print("75 perc            = ",np.percentile(heights,75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number');
