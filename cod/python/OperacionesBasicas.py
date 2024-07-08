from Madre import Madre
from numba import njit

class OperacionesBasicas(Madre):
    """
    Clase que realiza diversas operaciones matemáticas y de cifrado, heredando de la clase Madre.

    Attributes
    ----------
    lista : np.array
        Array de números para realizar operaciones.
    cadena : str
        Cadena de texto para realizar cifrado.

    Methods
    -------
    operacion_matricial()
        Realiza una operación en una matriz utilizando NumExpr.
    operacion_matricial_numba()
        Realiza una operación en una matriz utilizando Numba.
    producto_acumulado()
        Calcula el producto acumulado de la lista.
    producto_acumulado_numba()
        Calcula el producto acumulado de la lista utilizando Numba.
    cifrado_cesar(n)
        Realiza un cifrado César en la cadena con un desplazamiento dado.
    """
    
    def __init__(self, ruta, lista=None, cadena=None):
        """
        Constructor de la clase OperacionesBasicas.

        Parameters
        ----------
        ruta : str
            Una cadena de texto con una ruta de un archivo.
        lista : list, optional
            Lista de números para realizar operaciones.
        cadena : str, optional
            Cadena de texto para realizar cifrado.
        """
        super().__init__(ruta)
        self.__lista = np.array(lista) if lista is not None else None
        self.__cadena = cadena

    #Get y Set

    @property
    def ruta(self):
        """np.array: Obtiene o establece la ruta del archivo."""
        return self.__ruta
    
    @ruta.setter 
    def ruta(self, nueva_ruta):
        self.__ruta = nueva_ruta
    
    @property
    def lista(self):
        """np.array: Obtiene o establece la lista de números."""
        return self.__lista

    @lista.setter
    def lista(self, nueva_lista):
        self.__lista = np.array(nueva_lista)

    @property
    def cadena(self):
        """str: Obtiene o establece la cadena de texto."""
        return self.__cadena

    @cadena.setter
    def cadena(self, nueva_cadena):
        self.__cadena = nueva_cadena

    def __str__(self):
        """
        Método para obtener una representación en cadena de la instancia de la clase.

        Returns
        -------
        str
            Una cadena que resume los atributos de la instancia.
        """
        return (f"Ruta: {self.__ruta}\n"
                f"Lista: {self.__lista}"
                f"Cadena: {self.__cadena}")
    
    def operacion_matricial(self):
        """
        Realiza una operación en una matriz utilizando NumExpr.

        Returns
        -------
        np.array
            Resultado de la operación en la matriz.
        """
        matriz = np.random.rand(10_000, 10_000)
        resultado = ne.evaluate('(matriz ** 100) * 10 + 5')
        return resultado

    @njit(parallel=True)
    def operacion(self, matriz):
        """
        Realiza una operación en una matriz utilizando Numba.

        Parameters
        ----------
        matriz : np.array
            Matriz sobre la cual se realizará la operación.

        Returns
        -------
        np.array
            Resultado de la operación en la matriz.
        """
        matriz_resultado = np.empty_like(matriz)
        for i in nb.prange(matriz.shape[0]):
            for j in range(matriz.shape[1]):
                matriz_resultado[i, j] = (matriz[i, j] ** 100) * 10 + 5
        return matriz_resultado

    def operacion_matricial_numba(self):
        """
        Realiza una operación en una matriz utilizando Numba.

        Returns
        -------
        np.array
            Resultado de la operación en la matriz.
        """
        matriz = np.random.rand(10_000, 10_000)
        resultado = self.operacion(matriz)
        return resultado

    def producto_acumulado(self):
        """
        Calcula el producto acumulado de la lista.

        Returns
        -------
        np.array
            Producto acumulado de la lista.
        
        Raises
        ------
        ValueError
            Si la lista no ha sido inicializada.
        """
        if self.__lista is None:
            raise ValueError("La lista no ha sido inicializada")
        return np.cumprod(self.__lista)

    @staticmethod
    @njit()
    def _producto_acumulado(array):
        """
        Calcula el producto acumulado de un array utilizando Numba.

        Parameters
        ----------
        array : np.array
            Array sobre el cual se calculará el producto acumulado.

        Returns
        -------
        np.array
            Producto acumulado del array.
        """
        result = np.ones_like(array)
        result[0] = array[0]
        for i in range(1, len(array)):
            result[i] = result[i - 1] * array[i]
        return result

    def producto_acumulado_numba(self):
        """
        Calcula el producto acumulado de la lista utilizando Numba.

        Returns
        -------
        np.array
            Producto acumulado de la lista.
        
        """
        if self.__lista is None:
            raise ValueError("La lista no ha sido inicializada")
        return self._producto_acumulado(self.__lista)

    def cifrado_cesar(self, n):
        """
        Realiza un cifrado César en la cadena con un desplazamiento dado.

        Parameters
        ----------
        n : int
            Desplazamiento para el cifrado César.

        Returns
        -------
        str
            Cadena cifrada.
        
        """
        if self.__cadena is None:
            raise ValueError("La cadena no ha sido inicializada")
        desplazada = []
        for char in self.__cadena:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                desplazada.append(chr(start + (ord(char) - start + n) % 26))
            else:
                desplazada.append(char)
        cadena_desplazada = ''.join(desplazada)
        return cadena_desplazada
