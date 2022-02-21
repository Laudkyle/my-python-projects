import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-por.csv", sep =";")
data = data[['G1','G2','G3','studytime']]
predict= "G3"

X=np.array(data.drop([predict], 1))
Y= np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,Y, test_size = 0.2)
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
accuracy = linear.score(x_test, y_test)

print(f"The accuracy of the predict is going to be : {int(accuracy*100)}%")

predictions=linear.predict(x_test)
for x in range(len(predictions)):
	print(int(predictions[x]),x_test[x],y_test[x])