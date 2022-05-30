import pandas as pd
import numpy as np

def detect_outliers_with_zscore(data):
    outliers=[]
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score = (np.abs(i) - mean)/std
        if z_score > threshold:
           outliers.append(i)
    return outliers

data = [1,2,3,4,5,6,7,8,9,100,-100]

outliers = detect_outliers_with_zscore(data)
print(outliers)