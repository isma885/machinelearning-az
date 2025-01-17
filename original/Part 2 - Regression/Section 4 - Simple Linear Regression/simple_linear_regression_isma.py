# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:23:17 2024

@author: ismac
"""

# Regresion Lineal Simple

# Como importar las librerias
import numpy as np    
import matplotlib.pyplot as plt    
import pandas as pd    


# Importar el dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1].values    # Podria ser [:, 0]
y = dataset.iloc[:, 1].values     





# Divirdir el dataset en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)    
                                                                                               

                                                                                               
# Escalado de variables
"""from sklearn.preprocessing import StandardScaler 
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


# Crear modelo de Regresion Lineal Simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)


# Predecir el conjunto de test
y_pred = regression.predict(X_test)


# Visualizar los resultados de entrenamiento
plt.scatter(X_train, y_train, color = "r")
plt.plot(X_train, regression.predict(X_train), color = "b")
plt.title("Sueldo vs Agnos de Experiencia")
plt.xlabel("Agnos de Experiencia")
plt.ylabel("Sueldo ($)")
plt.show()


# Visualizar los resultados de test
plt.scatter(X_test, y_test, color = "r")
plt.plot(X_train, regression.predict(X_train), color = "b")
plt.title("Sueldo vs Agnos de Experiencia")
plt.xlabel("Agnos de Experiencia")
plt.ylabel("Sueldo ($)")
plt.show()