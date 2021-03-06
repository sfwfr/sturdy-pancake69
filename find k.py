from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Read Data
df=pd.read_csv("heart.csv")
# data
x=df.drop("cp",axis=1).values
# outcome data
y=df['cp'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
k_neighbors=np.arange(1,9) 

train_score = np.empty(len(k_neighbors))
test_score = np.empty(len(k_neighbors))

for i,k in enumerate(k_neighbors): 
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    train_score[i]=knn.score(x_train,y_train)
    test_score[i]=knn.score(x_test,y_test)
            
plt.title("69 k")
plt.plot(k_neighbors,test_score,label="test score")
plt.plot(k_neighbors,train_score,label="train score")
plt.xlabel("K number")
plt.ylabel("Score")
plt.show()