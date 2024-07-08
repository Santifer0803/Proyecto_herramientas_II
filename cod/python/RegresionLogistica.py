from numba import jit
from Madre import Madre

class RegresionLogistica(Madre):
    def __init__(self, ruta, num_iterations=2000, learning_rate=0.5):
        super().__init__(ruta)
        self.__num_iterations = num_iterations
        self.__learning_rate = learning_rate
        self.__datos = leer_txt(self.ruta)
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

    def __str__(self):
        return (f"RegresionLogistica(num_iterations={self.num_iterations}, "
                f"learning_rate={self.learning_rate})")

    @staticmethod
    @jit(nopython=True)
    def funcion_sigmoide(z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    @jit(nopython=True)
    def propagacion_adelante(W, b, X):
        Z = np.dot(W, X.T) + b
        A = RegresionLogistica.funcion_sigmoide(Z)
        return A

    @staticmethod
    @jit(nopython=True)
    def propagacion_atras(X, A, y):
        m = X.shape[0]
        dZ = A - y
        dW = np.dot(dZ, X) / m
        db = np.sum(dZ) / m
        return dW, db

    @staticmethod
    @jit(nopython=True)
    def optimizar(W, b, X, y, num_iterations, learning_rate):
        for i in range(num_iterations):
            A = RegresionLogistica.propagacion_adelante(W, b, X)
            dW, db = RegresionLogistica.propagacion_atras(X, A, y)
            W -= learning_rate * dW
            b -= learning_rate * db
        return W, b

    @staticmethod
    @jit(nopython=True)
    def predecir(W, b, X):
        Z = np.dot(W, X.T) + b
        A = RegresionLogistica.funcion_sigmoide(Z)
        return np.where(A > 0.5, 1, 0)

    def entrenar(self):
        W = np.zeros((1, self.X_train.shape[1]))
        b = 0
        W, b = RegresionLogistica.optimizar(W, b, self.X_train, self.y_train, self.num_iterations, self.learning_rate)
        y_prediction_train = RegresionLogistica.predecir(W, b, self.X_train)
        y_prediction_val = RegresionLogistica.predecir(W, b, self.X_val)
        accuracy_train = 100 - np.mean(np.abs(y_prediction_train - self.y_train)) * 100
        accuracy_val = 100 - np.mean(np.abs(y_prediction_val - self.y_val)) * 100
        return accuracy_train, accuracy_val
