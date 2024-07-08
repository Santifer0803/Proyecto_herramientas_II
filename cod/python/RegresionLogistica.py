import numpy as np
from numba import jit

class RegresionLogistica:
    """
    Clase para implementar un modelo de regresión logística utilizando Numba para acelerar las operaciones.
    
    Attributes
    ----------
    X_train : numpy.ndarray
        Matriz de características de entrenamiento del modelo.
    y_train : numpy.ndarray
        Vector de etiquetas de entrenamiento.
    X_val : numpy.ndarray
        Matriz de características de testeo del modelo.
    y_val : numpy.ndarray
        Vector de etiquetas de testeo.
    num_iterations : int
        Número de iteraciones para el entrenamiento.
    learning_rate : float
        Tasa de aprendizaje para el entrenamiento.
    
    Methods
    -------
    funcion_sigmoide(z)
        Aplica la función sigmoide al parámetro dado.
    propagacion_adelante(W, b, X)
        Realiza la propagación hacia adelante del modelo de regresión logística.
    propagacion_atras(X, A, y)
        Calcula la propagación hacia atrás para actualizar los gradientes.
    optimizar(W, b, X, y, num_iterations, learning_rate)
        Optimiza los parámetros W y b del modelo mediante el descenso de gradiente.
    predecir(W, b, X)
        Realiza predicciones de clases binarias utilizando los parámetros optimizados.
    entrenar()
        Entrena un modelo de regresión logística y evalúa su rendimiento.
    """

    def __init__(self, X_train, y_train, X_val, y_val, num_iterations=2000, learning_rate=0.5):
        """
        Constructor de la clase RegresionLogistica.

        Parameters
        ----------
        X_train : numpy.ndarray
            Matriz de características de entrenamiento del modelo.
        y_train : numpy.ndarray
            Vector de etiquetas de entrenamiento.
        X_val : numpy.ndarray
            Matriz de características de testeo del modelo.
        y_val : numpy.ndarray
            Vector de etiquetas de testeo.
        num_iterations : int, optional
            Número de iteraciones para el entrenamiento (por defecto es 2000).
        learning_rate : float, optional
            Tasa de aprendizaje para el entrenamiento (por defecto es 0.5).
        """
        self.X_train = X_train
        self.y_train = y_train
        self.X_val = X_val
        self.y_val = y_val
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate

    # Get y Set
    @property
    def X_train(self):
        return self._X_train

    @X_train.setter
    def X_train(self, value):
        self._X_train = value

    @property
    def y_train(self):
        return self._y_train

    @y_train.setter
    def y_train(self, value):
        self._y_train = value

    @property
    def X_val(self):
        return self._X_val

    @X_val.setter
    def X_val(self, value):
        self._X_val = value

    @property
    def y_val(self):
        return self._y_val

    @y_val.setter
    def y_val(self, value):
        self._y_val = value

    @property
    def num_iterations(self):
        return self._num_iterations

    @num_iterations.setter
    def num_iterations(self, value):
        self._num_iterations = value

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        self._learning_rate = value

    def __str__(self):
        """
        Representación en cadena de la clase RegresionLogistica.
        
        Returns
        -------
        str
            Representación en cadena de la clase.
        """
        return (f"RegresionLogistica(num_iterations={self.num_iterations}, "
                f"learning_rate={self.learning_rate})")

    @staticmethod
    @jit(nopython=True)
    def funcion_sigmoide(z):
        """
        Aplica la función sigmoide al parámetro dado.

        Parameters
        ----------
        z : numpy.ndarray
            Escalar, vector o matriz a la que se le quiere aplicar la función sigmoide.

        Returns
        -------
        numpy.ndarray
            Resultado después de aplicar la función sigmoide.
        """
        return 1 / (1 + np.exp(-z))

    @staticmethod
    @jit(nopython=True)
    def propagacion_adelante(W, b, X):
        """
        Realiza la propagación hacia adelante del modelo de regresión logística.

        Parameters
        ----------
        W : numpy.ndarray
            Matriz de tamaño (1, numero_de_caracteristicas) que contiene los pesos del modelo.
        b : float
            Sesgo del modelo.
        X : numpy.ndarray
            Matriz de tamaño (numero_de_muestras, numero_de_caracteristicas) que contiene las características de las muestras de entrada.

        Returns
        -------
        numpy.ndarray
            Salidas del modelo después de aplicar la función sigmoide.
        """
        Z = np.dot(W, X.T) + b
        A = RegresionLogistica.funcion_sigmoide(Z)
        return A

    @staticmethod
    @jit(nopython=True)
    def propagacion_atras(X, A, y):
        """
        Calcula la propagación hacia atrás para actualizar los gradientes.

        Parameters
        ----------
        X : numpy.ndarray
            Matriz de tamaño (numero_de_muestras, numero_de_caracteristicas) que contiene las características de las muestras de entrada.
        A : numpy.ndarray
            Salidas del modelo después de aplicar la función sigmoide.
        y : numpy.ndarray
            Vector de tamaño (numero_de_muestras) que contiene las etiquetas verdaderas para las muestras de entrada.

        Returns
        -------
        dW : numpy.ndarray
            Gradiente del costo respecto a los pesos W.
        db : float
            Gradiente del costo respecto al sesgo b.
        """
        m = X.shape[0]
        dZ = A - y
        dW = np.dot(dZ, X) / m
        db = np.sum(dZ) / m
        return dW, db

    @staticmethod
    @jit(nopython=True)
    def optimizar(W, b, X, y, num_iterations, learning_rate):
        """
        Optimiza los parámetros W y b del modelo mediante el descenso de gradiente.

        Parameters
        ----------
        W : numpy.ndarray
            Matriz de tamaño (1, numero_de_caracteristicas) que contiene los pesos del modelo.
        b : float
            Sesgo del modelo.
        X : numpy.ndarray
            Matriz de tamaño (numero_de_muestras, numero_de_caracteristicas) que contiene las características de las muestras de entrada.
        y : numpy.ndarray
            Vector de tamaño (numero_de_muestras) que contiene las etiquetas verdaderas para las muestras de entrada.
        num_iterations : int
            Número de iteraciones del descenso de gradiente.
        learning_rate : float
            Tasa de aprendizaje para actualizar los parámetros.

        Returns
        -------
        dict
            Diccionario que contiene los parámetros optimizados:
            - "W": Matriz de pesos optimizada.
            - "b": Sesgo optimizado.
        """
        for i in range(num_iterations):
            A = RegresionLogistica.propagacion_adelante(W, b, X)
            dW, db = RegresionLogistica.propagacion_atras(X, A, y)
            W -= learning_rate * dW
            b -= learning_rate * db
        return W, b

    @staticmethod
    @jit(nopython=True)
    def predecir(W, b, X):
        """
        Realiza predicciones de clases binarias utilizando los parámetros optimizados.

        Parameters
        ----------
        W : numpy.ndarray
            Matriz de tamaño (1, numero_de_caracteristicas) que contiene los pesos del modelo.
        b : float
            Sesgo del modelo.
        X : numpy.ndarray
            Matriz de tamaño (numero_de_muestras, numero_de_caracteristicas) que contiene las características de las muestras de entrada.

        Returns
        -------
        numpy.ndarray
            Vector de predicciones de tamaño (1, numero_de_muestras), donde cada elemento es 1 o 0.
        """
        Z = np.dot(W, X.T) + b
        A = RegresionLogistica.funcion_sigmoide(Z)
        return np.where(A > 0.5, 1, 0)

    def entrenar(self):
        """
        Entrena un modelo de regresión logística y evalúa su rendimiento.

        Returns
        -------
        tuple
            Tupla que contiene la precisión en el conjunto de entrenamiento y en el conjunto de validación.
        """
        W = np.zeros((1, self.X_train.shape[1]))
        b = 0
        W, b = RegresionLogistica.optimizar(W, b, self.X_train, self.y_train, self.num_iterations, self.learning_rate)
        y_prediction_train = RegresionLogistica.predecir(W, b, self.X_train)
        y_prediction_val = RegresionLogistica.predecir(W, b, self.X_val)
        accuracy_train = 100 - np.mean(np.abs(y_prediction_train - self.y_train)) * 100
        accuracy_val = 100 - np.mean(np.abs(y_prediction_val - self.y_val)) * 100
        return accuracy_train, accuracy_val
