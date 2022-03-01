#boilerplate daqui: https://medium.com/@tarammullin/dbscan-parameter-estimation-ff8330e3a3bd

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler

print("Importante a base\n")
df=pd.read_csv('data/Para_juntar/Grande Base2.csv',encoding='latin1')
df=df.dropna()
x=df.iloc[:,np.r_[4:24,25:29,36:47,48,51,52,54:6]]
y=df.iloc[:,3]
scaler = StandardScaler().fit(x)
x=scaler.transform(x)


print("Calculando...")
dim=len(x[0])
neighbors = NearestNeighbors(n_neighbors=2*dim)
neighbors_fit = neighbors.fit(x)
distances, indices = neighbors_fit.kneighbors(x)
distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)
plt.show()
