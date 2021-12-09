import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import joblib
import warnings
warnings.filterwarnings("ignore")
from azureml.core import Run
run = Run.get_context()
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv("diabetes.csv")
data.head()


data.info()


corr = data.corr()
print(corr)
sns.heatmap(corr, 
         xticklabels=corr.columns, 
         yticklabels=corr.columns, annot=True)


data.describe()


sns.pairplot(data, diag_kind= "kde", hue= "Outcome")



from sklearn.model_selection import train_test_split

x = data.drop("Outcome", axis = 1)

y = data["Outcome"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=7)


model1 = LogisticRegression()
model1.fit(x_train, y_train)
y_predict = model1.predict(x_test)
model1_score = model1.score(x_test, y_test)
print("accuracy :", accuracy_score(y_test, y_predict))
print("classification report :", classification_report(y_test, y_predict))
print("confusion matrix :", confusion_matrix(y_test, y_predict))

model2 = RandomForestClassifier()
model2.fit(x_train, y_train)
y_predict1 = model2.predict(x_test)
model2_score = model2.score(x_test, y_test)
print("accuracy :", accuracy_score(y_test, y_predict1))
print("classification report :", classification_report(y_test, y_predict1))
print("confusion matrix :", confusion_matrix(y_test, y_predict1))

from sklearn.model_selection import RandomizedSearchCV

Ran_para = {'bootstrap': [True, False],
 'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, None],
 'max_features': ['auto', 'sqrt'],
 'min_samples_leaf': [1, 2, 4],
 'min_samples_split': [2, 5, 10],
 'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]}


rf_model = RandomizedSearchCV(RandomForestClassifier(), Ran_para, n_iter=100, cv=3, verbose=2, random_state=42, n_jobs=-1)
rf_model.fit(x_train, y_train)


run.log("Parameter",rf_model.get_params())


print("Accuracy on training set: {:.3f}".format(rf_model.score(x_train, y_train)))
print("Accuracy on test set: {:.3f}".format(rf_model.score(x_test, y_test)))


y_predict2 = rf_model.predict(x_test)
rfmodel_score = rf_model.score(x_test, y_test)
print("accuracy :", accuracy_score(y_test, y_predict2))
print("classification report :", classification_report(y_test, y_predict2))
print("confusion matrix :", confusion_matrix(y_test, y_predict2))


import joblib
joblib.dump(rf_model, "dibetismodel.pkl")