import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle


data = pd.read_csv("student-por.csv", sep= ";")
data = data[["G1","G2","G3","studytime","failures","absences"]]

predict = "G2"

X = np.array(data.drop([predict], 1))
Y= np.array(data[predict])

xtr,xts,ytr,yts = sklearn.model_selection.train_test_split(X,Y, test_size = 0.1)
"""
best_acc = 0

for _ in range(50):
	linear = linear_model.LinearRegression()
	linear.fit(xtr,ytr)
	accuracy=linear.score(xts,yts)
	if accuracy > best_acc:
		best_acc = accuracy
		with open("sm.pickle", "wb") as f:
			pickle.dump(linear, f)
		with open("bs.pickle", "wb") as f:
			pickle.dump(best_acc, f)
			"""
pickle_in = open("sm.pickle", "rb")
best = open("bs.pickle", "rb")
best_acc = pickle.load(best)
linear = pickle.load(pickle_in)
print(f'Prediction accuracy : {best_acc}')
print("------------------------------------------------")
print("PREDICTIONS")
print("------------------------------------------------")
predictions= linear.predict(xts)
for x in range(len(predictions)):
	print(int(predictions[x]),xts[x],yts[x])
	
