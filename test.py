import pandas as pd
import numpy as np



print(np.array([1,2,3,4,5]))

np.random.seed(100)

x3 = np.random.randint(15,size=(1,4,6))
print(x3)

df = pd.DataFrame(x3[0],columns=['a','b','c','d','e','f'])
df.to_csv("C:\\Users\\phime\\Desktop\\python\\DisplayDataWebPage\\static\\aaa.csv")