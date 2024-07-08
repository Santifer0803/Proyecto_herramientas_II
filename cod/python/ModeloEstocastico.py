import pandas as pd
import numpy as np
from scipy.stats import norm
import time
from Madre import Madre

class ModeloEstocastico(Madre):
    """
    Clase para modelar y calcular primas estocásticas basadas en tablas de mortalidad y sobrevivencia.

    Attributes
    ----------
    ruta : str
        Una cadena de texto con una ruta de un archivo
    qx_hombres : pandas.DataFrame
        Tabla de mortalidad de hombres.
    px_hombres : numpy.ndarray
        Tabla de sobrevivencia de hombres.
    
    Methods
    -------
    fila_muerte(fila)
        Modifica una fila de probabilidades de sobrevivencia para reflejar la muerte.
    calcular_primas()
        Calcula las primas estocásticas basadas en la tabla de sobrevivencia.
    calcular_tiempo_promedio()
        Calcula el tiempo promedio en segundos que tarda en ejecutarse el modelo.
    """
    
    def __init__(self, ruta, hoja):
        """
        Constructor de la clase ModeloEstocastico
        
        Parameters
        ----------
        ruta : str
            Ruta al archivo Excel que contiene la tabla de mortalidad.
        hoja : str
            Nombre de la hoja en el archivo Excel que contiene la tabla de mortalidad.
        
        Returns
        -------
        None
        """
        super().__init__(ruta)
        self.__qx_hombres = pd.read_excel(self.__ruta, sheet_name=hoja)
        self.__px_hombres = 1 - self.__qx_hombres.values
    
    @property
    def qx_hombres(self):
        """
        Método get de la clase ModeloEstocastico
        
        Parameters
        ----------
        None
        
        Returns
        -------
        qx_hombres : pandas.DataFrame
            Tabla de mortalidad de hombres
        """
        return self.__qx_hombres

    @qx_hombres.setter
    def qx_hombres(self, nuevo_qx_hombres):
        """
        Método set de la clase ModeloEstocastico
        
        Parameters
        ----------
        nuevo_qx_hombres : pandas.DataFrame
            Nueva tabla de mortalidad de hombres
        
        Returns
        -------
        None
        """
        self.__qx_hombres = nuevo_qx_hombres
        self.__px_hombres = 1 - self.__qx_hombres.values  

    @property
    def px_hombres(self):
        """
        Método get de la clase ModeloEstocastico
        
        Parameters
        ----------
        None
        
        Returns
        -------
        px_hombres : numpy.ndarray
            Tabla de sobrevivencia de hombres
        """
        return self.__px_hombres

    def __str__(self):
        """
        Devuelve una cadena de texto que resume la clase ModeloEstocastico.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        cadena : str
            Texto explicativo que resume la clase ModeloEstocastico
        """
        return f"ModeloEstocastico con {self.__qx_hombres.shape[0]} filas y {self.__qx_hombres.shape[1]} columnas en qx_hombres"
    
    
    def fila_muerte(self, fila):
        """
        Modifica una fila de probabilidades de sobrevivencia para reflejar la muerte.
        
        Parameters
        ----------
        fila : numpy.ndarray
            Fila de probabilidades de sobrevivencia
        
        Returns
        -------
        fila : numpy.ndarray
            Fila modificada con falsos después del primer falso
        """
        fila[np.argmax(fila == False):] = False
        return fila
    
    def calcular_primas(self):
        """
        Calcula las primas estocásticas basadas en la tabla de sobrevivencia.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        lista_primas : list
            Lista de primas estocásticas calculadas
        """
        j = ((1.04) * (1.03)) - 1

        matriz_prob = np.zeros((45, 96))

        for i in range(0, 45):
            for k in range(0, 96):
                matriz_prob[i, k] = self.__px_hombres[min(20 + i + k, 115), 25 + k]

        filmat, colmat = matriz_prob.shape

        matriz_rnd = norm.cdf(np.random.normal(loc=0, scale=1, size=(filmat, colmat)))
        matriz_rnd = matriz_rnd < matriz_prob
        matriz_rnd = np.apply_along_axis(self.fila_muerte, 1, matriz_rnd)
        id = np.sum(matriz_rnd, axis=1)

        edades_pensiones = [np.arange(0, max(entrada + 1, 1)) for entrada in (np.minimum(65 - 19 - np.arange(1, 46), id) - 1)]
        an = [np.sum(np.power(1/(1+j), np.maximum(edad, 0))) for edad in edades_pensiones]
        annos_65 = [np.arange(65 - np.arange(20, 65)[entrada], id[entrada] + 1) for entrada in range(0, 45)]

        ben = [np.where((id[i] + np.arange(20, 65)[i]) < 65, 
                        5_000_000 * np.power(1/(1+j), id[i]), 
                        np.sum(300_000 * 13 * np.power(1/(1+j), annos_65[i])) + 1_000_000 * np.power(1/(1+j), id[i])) for i in range(0, 45)]

        lista_primas = [np.array(ben)/np.array(an)]
        prom_primas = 0

        while abs(prom_primas - np.mean(np.array(lista_primas))) > 0.001:
            matriz_rnd = norm.cdf(np.random.normal(loc=0, scale=1, size=(filmat, colmat)))
            matriz_rnd = matriz_rnd < matriz_prob
            matriz_rnd = np.apply_along_axis(self.fila_muerte, 1, matriz_rnd)
            id = np.sum(matriz_rnd, axis=1)
            edades_pensiones = [np.arange(0, max(entrada + 1, 1)) for entrada in (np.minimum(65 - 19 - np.arange(1, 46), id) - 1)]
            an = [np.sum(np.power(1/(1+j), np.maximum(edad, 0))) for edad in edades_pensiones]
            annos_65 = [np.arange(65 - np.arange(20, 65)[entrada], id[entrada] + 1) for entrada in range(0, 45)]
            ben = [np.where((id[i] + np.arange(20, 65)[i]) < 65, 
                            5_000_000 * np.power(1/(1+j), id[i]), 
                            np.sum(300_000 * 13 * np.power(1/(1+j), annos_65[i])) + 1_000_000 * np.power(1/(1+j), id[i])) for i in range(0, 45)]

            prom_primas = np.mean(np.array(lista_primas))
            lista_primas.append(np.array(ben)/np.array(an))

        return lista_primas

    def calcular_tiempo_promedio(self):
        """
        Calcula el tiempo promedio en segundos que tarda en ejecutarse el modelo.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        tiempo_promedio : float
            Tiempo promedio en segundos por iteración
        """
        inicio = time.time()
        prueba = self.calcular_primas()
        fin = time.time()
        tiempo_promedio = (fin - inicio) / len(prueba)
        return tiempo_promedio
