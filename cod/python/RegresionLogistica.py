import numpy as np
import pandas as pd
from numba import jit
from sklearn.model_selection import train_test_split
import time
from Madre import Madre

class RegresionLogistica(Madre):
    """
    Clase para realizar una regresión logística
  
    Attributes
    ----------
    ruta : str
        una cadena de texto con una ruta de un archivo
    
    repeticiones : int
        numero de repeticiones para la ejecición de un módulo, por default es 10
        
    num_iterations : int
        Cantidad de iteraciones para la optimización por descenso de gradiente,
        por default es 2000
        
    learning_rate : double
      Tasa de aprendizaje en cada iteración del modelo, es un peso, por default
      es 0.5
  
    Methods
    -------
    def funcion_sigmoide(z)
        Calcula la función logística de un vector
    
    def propagacion_adelante(W, b, X)
        Calcula el resultado z de una función lineal, la probabilidad con la
        función sigmoide y una función de pérdida conocida como "pérdida de
        entropía cruzada binaria"
    
    def propagacion_atras(X, A, y)
        Calcula el gradiente, en este caso, las derivadas de W y b
    
    def optimizar(W, b, X, y, num_iterations, learning_rate):
        Utiliza un algoritmo iterativo llamado "descenso de gradiente" para
        optimizar los parámetros
        
    def predecir(W, b, X):
        Se calculan las probabilidades con base en la función logística (A) y se
        ponen los "y" predichos con base en las probabilidades de A
        
    def entrenar(self):
      Se ejecuta el modelo de regresión logística con las funciones anteriores
    """

    def __init__(self, ruta):
      """
      Constructor de la clase RegresionLogistica
      
      Parameters
      ----------
      ruta : str
          una cadena de texto con una ruta de un archivo
      
      Returns
      -------
      None
      """

        super().__init__(ruta)
    
    @staticmethod
    @jit(nopython=True)
    def regresion_logistica(X_train, y_train, X_val, y_val, num_iterations=2000, learning_rate=0.5):
      
        def funcion_sigmoide(z):
          '''
          Calcula la función logística de un vector
      
          Parameters
          z : numpy.ndarray
              Vector de valores numéricos, calculado con numpy
      
          Returns
          double
              Valor entre 0 y 1, este es el resultado de la función logística
          '''

          return 1 / (1 + np.exp(-z))

        def propagacion_adelante(W, b, X):
          '''
          Calcula el resultado z de una función lineal, la probabilidad con la
          función sigmoide y una función de pérdida conocida como "pérdida de
          entropía cruzada binaria"
      
          Parameters
          W : numpy.ndarray
              Tensor de pesos, uno de los parámetros del modelo
          b : double
              Término de sesgo, uno de los parámetros del modelo
          X : numpy.ndarray
              Datos usados como conjunto de entrenamiento del modelo, son los datos
              predichos
          y : numpy.ndarray
              Los datos reales del modelo
      
          Returns
          A : double
              Valor entre 0 y 1, este es el resultado de la función logística con un
              vector Z calculado con los valores del modelo
          cost : double
              Resultado de la función de pérdida de entropía cruzada binaria, usando
              la logverosimilitud
          '''

          Z = np.dot(W, X.T) + b
          A = funcion_sigmoide(Z)
          return A

        def propagacion_atras(X, A, y):
          '''
          Calcula el gradiente, en este caso, las derivadas de W y b
      
          Parameters
          X : numpy.ndarray
              Datos usados como conjunto de entrenamiento del modelo, son los datos
              predichos
          A : double
              Resultado de la función logística con un vector Z calculado con los
              valores del modelo, se obtiene con la función de forward_propagation
          y : numpy.ndarray
              Los datos reales del modelo
      
          Returns
          dW : numpy.ndarray
              Vector con las derivadas de cada entrada de W
          db : double
              Valor que representa la derivada del término del sesgo
          '''

          m = X.shape[0]
          dZ = A - y
          dW = np.dot(dZ, X) / m
          db = np.sum(dZ) / m
          return dW, db

        def optimizar(W, b, X, y, num_iterations, learning_rate):
          '''
          Utiliza un algoritmo iterativo llamado "descenso de gradiente" para
          optimizar los parámetros
      
          Parameters
          W : numpy.ndarray
              Tensor de pesos, uno de los parámetros del modelo
          b : double
              Término de sesgo, uno de los parámetros del modelo
          X : numpy.ndarray
              Datos usados como conjunto de entrenamiento del modelo, son los datos
              predichos
          y : numpy.ndarray
              Los datos reales del modelo
          num_iterations : int
              Cantidad de iteraciones a realizar en el algoritmo
          learning_rate : double
              Factor de escala para controlar la velocidad de aprendizaje en cada
              iteración, suele ser menor a 1 y positiva
      
          Returns
          params : dict
              Parámetros del modelo optimizados
          gradients : dict
              Gradientes del modelo optimizados
          '''

          for i in range(num_iterations):
            A = propagacion_adelante(W, b, X)
            dW, db = propagacion_atras(X, A, y)
            W -= learning_rate * dW
            b -= learning_rate * db
          return W, b

        def predecir(W, b, X):
          '''
          Se calculan las probabilidades con base en la función logística (A) y se
          ponen los "y" predichos con base en las probabilidades de A
      
          Parameters
          W : numpy.ndarray
              Tensor de pesos, uno de los parámetros del modelo
          b : double
              Término de sesgo, uno de los parámetros del modelo
          X : numpy.ndarray
              Datos usados como conjunto de entrenamiento del modelo, son los datos
              predichos
      
          Returns
          y_prediction : numpy.ndarray
              Parámetros del modelo optimizados
          '''

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
      '''
      Se construye la separación de datos correspondiente
  
      Parameters
      None
  
      Returns
        X_train : numpy.ndarray
            Parte de los datos para entrenar al modelo, en este caso datos
            predichos
        y_train : numpy.ndarray
            Parte de los datos para entrenar al modelo, en este caso los datos
            reales
        X_val : numpy.ndarray
            Parte de los datos para validar al modelo, en este caso se validan
            los datos predichos
        Y_val : numpy.ndarray
            Parte de los datos para validar al modelo, en este caso se validan
            los datos reales

      '''

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
      '''
      Se miden los tiempos necesarios
  
      Parameters
      None
  
      Returns
        tiempo_inicial : double
            Tiempo de las primeras 10 iteraciones que se realizan con Numba
        tiempo_posterior : double
            Tiempo de las posteriores 10 iteraciones que se realizan con Numba,
            con el código analizado internamente por las primeras iteraciones

      '''
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

