import numpy as np
import pandas as pd
from numba import jit
from sklearn.model_selection import train_test_split
import time
from Madre import Madre

class RegresionLogistica(Madre):
    
    def __init__(self, ruta):
        super().__init__(ruta)
    
    @staticmethod
    @jit(nopython=True)
    def regresion_logistica(X_train, y_train, X_val, y_val, num_iterations=2000, learning_rate=0.5):
      
        def funcion_sigmoide(z):
          return 1 / (1 + np.exp(-z))

        def propagacion_adelante(W, b, X):
          Z = np.dot(W, X.T) + b
          A = funcion_sigmoide(Z)
          return A

        def propagacion_atras(X, A, y):
          m = X.shape[0]
          dZ = A - y
          dW = np.dot(dZ, X) / m
          db = np.sum(dZ) / m
          return dW, db

        def optimizar(W, b, X, y, num_iterations, learning_rate):
          for i in range(num_iterations):
            A = propagacion_adelante(W, b, X)
            dW, db = propagacion_atras(X, A, y)
            W -= learning_rate * dW
            b -= learning_rate * db
          return W, b

        def predecir(W, b, X):
          Z = np.dot(W, X.T) + b
          A = funcion_sigmoide(Z)
          return np.where(A > 0.5, 1, 0)
      
        W = np.zeros((1, X_train.shape[1]))
        b = 0
        W, b = optimizar(W, b, X_train, y_train, num_iterations, learning_rate)
        y_prediction_train = predecir(W, b, X_train)
        y_prediction_validation = predecir(W, b, X_val)
        accuracy_train = 100 - np.mean(np.abs(y_prediction_train - y_train)) * 100
        accuracy_val = 100 - np.mean(np.abs(y_prediction_validation - y_val)) * 100
        return accuracy_train, accuracy_val
      
    def construir_datos(self):
      
        datos = super().leer_csv()
      
        # Datos y transformaciones
        X =  np.array(datos.drop(["Outcome"], axis = 1))
        y = np.array(datos["Outcome"])
        
        # Normalización de los datos
        X = (X - np.min(X)) / (np.max(X) - np.min(X))
        
        # Separa la muestra
        X_train, X_val, y_train, y_val = train_test_split(
            
            X, # Covaribles predictoras
            
            y, # Variable a predecir
            
            random_state = None, # (None: escoge una diferente en cada corrida)
            
            test_size = 0.20 # Cantidad de datos de entrenamiento y prueba
            
        )
        
        return X_train, X_val, y_train, y_val
    
    def medir_tiempos(self):
      
        # Se crea un array vacío para guardar los tiempo de ejecución
        tiempos = np.array([], dtype = float)
        
        # Se extrae la data
        X_train, X_val, y_train, y_val = self.construir_datos()
        
        # Se itera 10 veces para calcular el tiempo de ejecución del proceso cada vez
        for i in range(10):
        
            inicio = time.time()
            
            RegresionLogistica.regresion_logistica(
                
                X_train, y_train, 
                
                X_val, y_val, 
                
                num_iterations = 1000, learning_rate = 0.003
                
            )
        
            fin = time.time()
        
            # Se guarda el tiempo de ejecución
            tiempos = np.append(tiempos, (fin - inicio))
        
        # Se calcula el promedio del tiempo de ejecución
        tiempo_inicial = np.sum(tiempos) / 10
        
        # Dado que la primera iteración demora más tiempo que el resto debido a cómo trabaja Numba,
        # se procede a realizar el mismo proceso una segunda vez, en la cual se va a notar que el 
        # tiempo promedio de ejecución se redujo significativamente, ya que una vez "calentadas" 
        # las funciones, Numba hace el proceso mucho más rápido
        
        tiempos = np.array([], dtype = float)

        for i in range(10):
        
            inicio = time.time()
            
            self.regresion_logistica(
                
                X_train, y_train, 
                
                X_val, y_val, 
                
                num_iterations = 1000, learning_rate = 0.003
                
            )
        
            fin = time.time()
            
            tiempos = np.append(tiempos, (fin - inicio))
        
        tiempo_posterior = np.sum(tiempos) / 10
        
        return tiempo_inicial, tiempo_posterior

