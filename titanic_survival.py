# -*- coding: utf-8 -*-
"""Titanic_Survival.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MzOaQDEx-l8eGk9YmLP8faOsLjNztkBd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/train.csv")
df

df.info()

df.columns

df.isnull().sum()

df.drop(["Cabin"],axis=1,inplace=True)
df

df["Age"] = df["Age"].fillna(0.0)
df

df["Embarked"] = df["Embarked"].fillna("N")
df

df.isnull().sum()

df.dtypes

df.corr()

sns.heatmap(df.corr())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])

df.dtypes

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

x = df.drop(["PassengerId","Name","Survived","Ticket","Fare"],axis=1)
y = df["Survived"]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=0,test_size=0.25,train_size=0.75)

x_train

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()

scale.fit_transform(x_train)
scale.transform(x_test)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)
y_pred

y_test

np.unique(y_test,return_counts=True)

np.unique(y_pred,return_counts=True)

df1 = pd.DataFrame({"Actual":y_test,"Predicted":y_pred})

df1.plot(figsize=(8,4))

sns.regplot(x="Actual",y="Predicted",data=df1,logistic=True)
sns.regplot

df1.corr()

sns.heatmap(df1.corr())

from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, mean_absolute_error, mean_squared_error, recall_score , f1_score

confusion_matrix(y_test,y_pred)

ac = accuracy_score(y_test,y_pred)
ac

precision_score(y_test,y_pred)

recall_score(y_test,y_pred)

f1_score(y_test,y_pred)

mean_squared_error(y_test,y_pred)

mean_absolute_error(y_test,y_pred)

s_prob = (116)/(116+23+21+63)
d_prob = (63)/(116+23+21+63)

print("Model Accuracy :",ac*100)

print("Probability of Surviving: ",s_prob*100)
print("Probability of Death: ",d_prob*100)

a = np.unique(y_pred,return_counts=True)
a

print("Number of People Survived after Titanic Disaster are ",a[1][1],"people.")

