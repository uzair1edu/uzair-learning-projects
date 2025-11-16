# model_training.py
# Minimal example: train a scikit-learn model on mock data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# mock data
X = np.random.rand(100,5)
y = (X.sum(axis=1) > 2.5).astype(int)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
clf = LogisticRegression(max_iter=200).fit(X_train,y_train)
pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test,pred))
