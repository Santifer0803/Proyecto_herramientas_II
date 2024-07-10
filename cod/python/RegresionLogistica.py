from numba import jit
import numpy as np
from sklearn.model_selection import train_test_split
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
    def __init__(self, ruta, num_iterations=2000, learning_rate=0.5):
        super().__init__(ruta)
        self.__num_iterations = num_iterations
        self.__learning_rate = learning_rate
        self.__datos = self.leer_csv()
        X =  self.__datos.iloc[:, :-1].values
        y = self.__datos.iloc[:, -1].values
        X = (X - np.min(X)) / (np.max(X) - np.min(X))
    
        self.__X_train, self.__X_val, self.__y_train, self.__y_val = train_test_split(
        
            X,
            
            y, 
            
            random_state = None, 
            
            test_size = 0.20
    
        )

    @property
    def X_train(self):
        return self.__X_train

    @X_train.setter
    def X_train(self, value):
        self.__X_train = value

    @property
    def y_train(self):
        return self.__y_train

    @y_train.setter
    def y_train(self, value):
        self.__y_train = value

    @property
    def X_val(self):
        return self.__X_val

    @X_val.setter
    def X_val(self, value):
        self.__X_val = value

    @property
    def y_val(self):
        return self.__y_val

    @y_val.setter
    def y_val(self, value):
        self.__y_val = value

    def __str__(self):
        return (f"RegresionLogistica(num_iterations={self.__num_iterations}, "
                f"learning_rate={self.__learning_rate})")

    @staticmethod
    @jit(nopython=True)
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

    @staticmethod
    @jit(nopython=True)
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
        A = RegresionLogistica.funcion_sigmoide(Z)
        return A

    @staticmethod
    @jit(nopython=True)
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

    @staticmethod
    @jit(nopython=True)
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
            A = RegresionLogistica.propagacion_adelante(W, b, X)
            dW, db = RegresionLogistica.propagacion_atras(X, A, y)
            W -= learning_rate * dW
            b -= learning_rate * db
        return W, b

    @staticmethod
    @jit(nopython=True)
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
        A = RegresionLogistica.funcion_sigmoide(Z)
        return np.where(A > 0.5, 1, 0)

    def entrenar(self):
      '''
      Se ejecuta el modelo de regresión logística con las funciones anteriores
  
      Parameters
      X_train : numpy.ndarray
          Parte de los datos para entrenar al modelo, en este caso datos
          predichos
      y_train : numpy.ndarray
          Parte de los datos para entrenar al modelo, en este caso los datos
          reales
      X_val : numpy.ndarray
          Parte de los datos para validar al modelo, en este caso se validan los
          datos predichos
      Y_val : numpy.ndarray
          Parte de los datos para validar al modelo, en este caso se validan los
          datos reales
      num_iterations : int
          Cantidad de iteraciones a realizar en el algoritmo de optimización,
          por defecto en 2000
      learning_rate : double
          Factor de escala para controlar la velocidad de aprendizaje en cada
          iteración del algoritmo de optimización, suele ser menor a 1 y
          positiva, por defecto se establece en 0.5
  
      Returns
      lista : dict
          Diccionario con el ajuste de entrenamiento, el ajuste de testeo y el
          costo en proceso del modelo
      '''
        W = np.zeros((1, self.__X_train.shape[1]))
        b = 0
        W, b = RegresionLogistica.optimizar(W, b, self.__X_train, self.__y_train, self.__num_iterations, self.__learning_rate)
        y_prediction_train = RegresionLogistica.predecir(W, b, self.__X_train)
        y_prediction_val = RegresionLogistica.predecir(W, b, self.__X_val)
        accuracy_train = 100 - np.mean(np.abs(y_prediction_train - self.__y_train)) * 100
        accuracy_val = 100 - np.mean(np.abs(y_prediction_val - self.__y_val)) * 100
        return accuracy_train, accuracy_val
