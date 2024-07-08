import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
from numba import prange, njit
import seaborn as sns
from IPython.display import clear_output
from Madre import Madre

class TrabajoDataframes(Madre):
    """
    Clase para trabajar con dataframes heredando de la clase Madre.
    
    Attributes
    ----------
    ruta : str
        Una cadena de texto con una ruta de un archivo
        
    dataframe : pandas.DataFrame
        DataFrame leído desde el archivo especificado por la ruta

    banda : int
        Tamaño de la ventana a considerar alrededor de cada valor nulo para calcular el promedio de 
        imputación. La ventana se extiende `banda` posiciones a la izquierda y a la derecha del valor nulo.
    
    Methods
    -------
    limpiar_datos(self)
        Realiza la limpieza del DataFrame eliminando y reemplazando valores según ciertas reglas.
    
    histograma(df, columna)
        Crea un histograma para una columna numérica específica de un DataFrame.
    
    barras(df, columna)
        Crea un gráfico de barras para una columna categórica específica de un DataFrame.
    
    tipos_columnas(df)
        Identifica y separa las columnas numéricas y categóricas en un DataFrame.
    
    generar_graficos(self, limpiar=True)
        Genera gráficos de histogramas para variables numéricas y gráficos de barras para variables categóricas.
    
    imputar_por_prom_movil(self, columna)
        Imputa valores nulos en una columna específica de un DataFrame utilizando un promedio móvil.
    
    eliminar_columnas_por_nulos(self, porcentaje)
        Elimina columnas con un porcentaje alto de valores nulos.
    
    imputar_por_agrupacion(self)
        Imputa valores faltantes en la columna 'Salario base' por agrupación.
    """

    
    def __init__(self, ruta):
        """
        Constructor de la clase TrabajoDataframes
        
        Parameters
        ----------
        ruta : str
            Una cadena de texto con una ruta de un archivo
        
        Returns
        -------
        None
        """
        super().__init__(ruta)
        if (isinstance(ruta, str)): 
            self.__dataframe = self.leer_excel()
        else:
            self.__dataframe = None  
        self.__banda = 4


    @property
    def banda(self):
        """
        Método get de la clase TrabajoDataframes

        Parameters
        ----------
        None

        Returns
        -------
        banda : int
            Tamaño de la ventana para el promedio móvil
        """
        return self.__banda

    @banda.setter
    def banda(self, nueva_banda):
        """
        Método set de la clase TrabajoDataframes

        Parameters
        ----------
        nueva_banda : int
            Nuevo tamaño de la ventana para el promedio móvil

        Returns
        -------
        None
        """
        self.__banda = nueva_banda

    @property
    def dataframe(self):
        """
        Método get de la clase TrabajoDataframes

        Parameters
        ----------
        None

        Returns
        -------
        dataframe : pandas.DataFrame
            El DataFrame actual
        """
        return self.__dataframe

    @dataframe.setter
    def dataframe(self, nuevo_dataframe):
        """
        Método set de la clase TrabajoDataframes

        Parameters
        ----------
        nuevo_dataframe : pandas.DataFrame
            El nuevo DataFrame que reemplazará el actual

        Returns
        -------
        None
        """
        self.__dataframe = nuevo_dataframe

    
    def __str__(self):
        """
        Una cadena de texto que resume la clase TrabajoDataframes.

        Parameters
        ----------
        None

        Returns
        -------
        cadena : str
            Texto explicativo que resume la clase TrabajoDataframes
        """
        return f'{super().__str__()}\nBanda: {self.__banda}\nDataFrame: {self.__dataframe}'

#-------------------------------- Ejercicio 2---------------------------------------   
    
    def limpiar_datos(self):
        """
        Realiza la limpieza del DataFrame eliminando y reemplazando valores según ciertas reglas.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        muertes_cr : pandas.DataFrame
            DataFrame limpio según las reglas especificadas
        """
        muertes_cr = self.__dataframe
    
        muertes_cr = muertes_cr.drop(columns = ['pc', 'causamuer', 'des_causa', 'instmurio', 'pcocu', 'nacmadre', 'pcregis', 'gruposcb'])
    
        # Se realiza la limpieza de la base de datos
        
        muertes_cr = muertes_cr[muertes_cr['edads'] >= 15]
        
        muertes_cr = muertes_cr[muertes_cr['anodef'] >= 2014]
        
        muertes_cr = muertes_cr[muertes_cr['anotrab'] >= 2014]
        
        muertes_cr = muertes_cr[muertes_cr['anodeclara'] >= 2014]
        
        muertes_cr['estcivil'] = muertes_cr['estcivil'].str.replace("Ã³", "o")
        
        muertes_cr['ocuparec'] = muertes_cr['ocuparec'].str.replace("Ã¡", "a")
        
        muertes_cr['ocuparec'] = muertes_cr['ocuparec'].str.replace("Ã©", "e")
        
        muertes_cr['ocuparec'] = muertes_cr['ocuparec'].str.replace("Ã", "i")
        
        muertes_cr['regsalud'] = muertes_cr['regsalud'].str.replace("Ã\xad", "i")
        
        muertes_cr['regsalud'] = muertes_cr['regsalud'].str.replace("Ã³", "o")
        
        muertes_cr['provincia'] = muertes_cr['provincia'].str.replace("Ã©", "e")
        
        muertes_cr['provincia'] = muertes_cr['provincia'].str.replace("Ã³", "o")
        
        muertes_cr['provocu'] = muertes_cr['provocu'].str.replace("Ã©", "e")
        
        muertes_cr['provocu'] = muertes_cr['provocu'].str.replace("Ã³", "o")
        
        muertes_cr['provregis'] = muertes_cr['provregis'].str.replace("Ã©", "e")
        
        muertes_cr['provregis'] = muertes_cr['provregis'].str.replace("Ã³", "o")
        
        muertes_cr['reginec'] = muertes_cr['reginec'].str.replace("Ã\xad", "i")
        
        muertes_cr['reginec'] = muertes_cr['reginec'].str.replace("Ã³", "o")
        
        muertes_cr['edadsrec'] = muertes_cr['edadsrec'].str.replace("100 y mÃ¡s", "100 - 121")
        
        muertes_cr['autopsia'] = muertes_cr['autopsia'].str.replace("Ã©", "e")
        
        muertes_cr['autopsia'] = muertes_cr['autopsia'].str.replace("Ã\xad", "i")
        
        muertes_cr['asistmed'] = muertes_cr['asistmed'].str.replace("Ã©", "e")
        
        muertes_cr['asistmed'] = muertes_cr['asistmed'].str.replace("Ã\xad", "i")
        
        muertes_cr['nacionalid'] = muertes_cr['nacionalid'].apply(lambda x: 'Extranjero' if x != 'Costa Rica' else x)
        
        otros = ['Ignorado', 'Union libre', 'Separado', 'Menor']
        
        muertes_cr['estcivil'] = muertes_cr['estcivil'].replace(otros, 'Otros')
        
        trabajadores_activos = ['Profesionales cienti\xadficos e intelectuales', 
                                'Agricultores y trabajadores calificados agropecuarios, forestales y pesqueros',
                                'Ocupaciones elementales', 'Trabajadores de los servicios y vendedores de comercios y mercados',
                                'Operadores de instalaciones y maquinas y ensambladores', 'Tecnicos y profesionales de nivel medio',
                                'Oficiales, operarios y artesanos de artes mecanicas y de otros oficios', 'Personal de apoyo administrativo',
                                'Directores y gerentes']
        
        muertes_cr['ocuparec'] = muertes_cr['ocuparec'].replace(trabajadores_activos, 'Trabajadores activos')
        
        otros = ['Pensionado', 'Persona con discapacidad', 'Estudiante', 'Mal especificadas', 'Privado de libertad']
        
        muertes_cr['ocuparec'] = muertes_cr['ocuparec'].replace(otros, 'Otros')
        
        rangos_etarios = ["15 - 19", "20 - 24", "25 - 29", "30 - 34", "35 - 39", "40 - 44", "45 - 49", 
                          "50 - 54", "55 - 59", "60 - 64", "65 - 69", "70 - 74", "75 - 79", "80 - 84", 
                          "85 - 89", "90 - 94", "95 - 99", "100 - 121"]
        
        muertes_cr['edadsrec'] = pd.Categorical(muertes_cr['edadsrec'], categories = rangos_etarios, ordered = True)
        
        muertes_cr.reset_index(drop = True, inplace = True)
        
        return muertes_cr
#-------------------------------------------------------------------------------------------------------

#--------------------------------------Ejercicio 3------------------------------------------------------
    # Se define una función que realice los histogramas para las variables numéricas
    @staticmethod
    def histograma(df, columna):
        '''
        Función que crea un histograma para una columna numérica específica de un DataFrame.

        Parameters:
        ----------
        df: pandas.DataFrame
           DataFrame que contiene los datos

        columna: str
           Nombre de la columna numérica para la cual se desea crear el histograma

        Returns:
        -------
        fig: matplotlib.figure.Figure
           Figura del histograma generado
        '''
        plt.figure()
        
        sns.histplot(df[columna], bins = 'auto', color = 'blue', edgecolor = 'black')
        
        plt.xlabel('Valor')
        
        plt.ylabel('Frecuencia')
        
        return plt.gcf()

    # Se define otra función que haga los gráficos de barras para las variables categóricas
    @staticmethod
    def barras(df, columna):
        '''
        Función que crea un gráfico de barras para una columna categórica específica de un DataFrame.

        Parameters:
        ----------
        df: pandas.DataFrame
           DataFrame que contiene los datos

        columna: str
           Nombre de la columna categórica para la cual se desea crear el gráfico de barras

        Returns:
        -------
        fig: matplotlib.figure.Figure
           Figura del gráfico de barras generado
        '''
        
        plt.figure()
        
        sns.countplot(x = columna, data = df, color = 'red')
    
        plt.xticks(rotation = 45)
        
        plt.xlabel('Categorías')
        
        plt.ylabel('Cantidad')
        
        return plt.gcf()

    # Definimos una función que devuelve las columnas numéricas y categóricas en listas por aparte
    @staticmethod
    def tipos_columnas(df):
        '''
        Función que identifica y separa las columnas numéricas y categóricas en un DataFrame.

        Parameters:
        ----------
        df: pandas.DataFrame
           DataFrame que contiene los datos

        Returns:
        -------
        numericas: pandas.Index
           Índice con los nombres de las columnas numéricas

        categoricas: pandas.Index
           Índice con los nombres de las columnas categóricas
        '''
        
        numericas = df.select_dtypes(include = ['number']).columns
            
        categoricas = df.select_dtypes(include = ['object', 'category']).columns
    
        return numericas, categoricas

    
    # Definimos una función que genere los gráficos deseados
    def generar_graficos(self, limpiar = True):
        '''
        Función que genera gráficos de histogramas para variables numéricas y gráficos de barras para variables categóricas.

        Parameters:
        ----------
        limpiar: bool
           Si es True, se limpiará la salida después de mostrar los gráficos (por defecto True)
        '''
        
        muertes_cr = self.__dataframe
        # Obtenemos las variables numericas y categóricas
        numericas, categoricas = self.tipos_columnas(muertes_cr)
        
        # Generamos y guardamos los gráficos tanto de histogramas como de barras usando la paralelización de joblib
        histogramas = Parallel(n_jobs = -1)(
        
            delayed(self.histograma)(muertes_cr, col) for col in numericas
        
        )
    
        graficos_barras = Parallel(n_jobs = -1)(
        
            delayed(self.barras)(muertes_cr, col) for col in categoricas
        
        )
    
        # Mostramos los gráficos
        for grafico in histogramas + graficos_barras:
    
            plt.show()
    
        # Si el parámetro limpiar es True, no se mostrarán los gráficos
        if limpiar:
    
            clear_output()

    
#-------------------------------------------------------------------------------------------------------

#--------------------------------------Ejercicio 4------------------------------------------------------
   
    def imputar_por_prom_movil(self, columna):
        '''
        Función que imputa valores nulos en una columna específica de un DataFrame utilizando un promedio móvil.
        Esta función lee un archivo de Excel, imputa los valores nulos en la columna especificada utilizando
        el método `imputar_valores_nulos` y retorna el DataFrame con los valores imputados.
    
        Parameters:
        ----------    
        columna: str
            Nombre de la columna en la cual se desean imputar los valores nulos.
    
    
        Returns:
        -------
        dataframe: pandas.DataFrame
            DataFrame que contiene los datos del archivo Excel leído, con los valores nulos en la columna 
            especificada imputados utilizando un promedio móvil.
        '''

        #Numba tiene limitaciones en cuanto a la compatibilidad con ciertos tipos de datos y estructuras de 
        #objetos complejas, como instancias de clases. Por lo tanto esta función tuvo que estar dentro del
        #método y no puede ser un método por sí misma.
        @njit(parallel=True)
        def imputar_valores_nulos(data, banda):
            '''
            Función que imputa valores nulos en un array de datos utilizando un promedio móvil.
            
            Esta función utiliza Numba para acelerar el proceso de imputación de valores nulos en un array,
            reemplazando cada valor nulo por el promedio de los valores no nulos dentro de una ventana definida 
            por el parámetro `banda`. La imputación se realiza de manera paralela para mejorar el rendimiento.
        
            Parameters
            ----------
            data : numpy.ndarray
                Array de datos que contiene los valores a imputar. Puede contener valores nulos (np.nan).
            
            banda : int
                Tamaño de la ventana a considerar alrededor de cada valor nulo para calcular el promedio de 
                imputación. La ventana se extiende `banda` posiciones a la izquierda y a la derecha del valor nulo.
        
            Returns
            -------
            resultado : numpy.ndarray
                Array de datos con los valores nulos imputados. Los valores nulos originales se reemplazan por el 
                promedio de los valores no nulos dentro de la ventana definida por `banda`.
            '''
            n = len(data)
            resultado = data.copy()
            
            for i in prange(n):
                if np.isnan(data[i]):
                    principio = max(0, i - banda)
                    final = min(n, i + banda + 1)
                    suma, cuenta = 0.0, 0
                    
                    for j in range(principio, final):
                        if not np.isnan(data[j]):
                            suma += data[j]
                            cuenta += 1
                            
                    if cuenta > 0:
                        resultado[i] = suma / cuenta
                        
            return resultado

        dataframe = self.__dataframe
        data = dataframe[columna].values
        data_imputado = imputar_valores_nulos(data, self.__banda)
        dataframe[columna] = data_imputado
        return dataframe


#------------------------------------------------------------------------------------------------------- 
    
#--------------------------------------Ejercicio 5------------------------------------------------------    
    
    def eliminar_columnas_por_nulos(self, porcentaje):
        '''
        Función que elimina columnas con un porcentaje alto de valores nulos.
        Esta función lee un archivo de Excel, calcula el número máximo de valores nulos 
        permitidos por columna basado en el porcentaje especificado, y elimina las columnas 
        que exceden este umbral.
    
        Parameters:
        ----------
        porcentaje: float
           Porcentaje máximo de valores nulos permitidos en una columna para que no sea eliminada.
           Debe ser un valor entre 0 y 1.
    
        Returns:
        -------
        df_filtrado: pandas.DataFrame
           DataFrame que contiene los datos del archivo Excel leído, con las columnas 
           que exceden el porcentaje de valores nulos eliminadas
        '''
        # Llamo al método heredado para leer la base de datos
        df = self.__dataframe    
        # Calculamos el número máximo de valores nulos permitidos
        max_nulos = len(df) * porcentaje
        
        # Filtramos las columnas que tienen menos de max_nulos valores nulos
        df_filtrado = df.dropna(axis=1, thresh=len(df) - max_nulos)
        
        return df_filtrado
#------------------------------------------------------------------------------------------------------- 

#--------------------------------------Ejercicio 6------------------------------------------------------ 
    
    def imputar_por_agrupacion(self):
        '''
        Función que imputa valores faltantes en la columna 'Salario base' por agrupación.
        Esta función lee un archivo de Excel, y luego imputa los valores faltantes en la columna 
        'Salario base' utilizando el promedio de los valores agrupados por 'Género' y 'Grado de estudio'.
    
        Parameters:
        ----------
        None
    
        Returns:
        -------
        base_salarios: pandas.DataFrame
           DataFrame que contiene los datos del archivo Excel leído, con los valores 
           faltantes en la columna 'Salario base' imputados por el promedio de los grupos 
           de 'Género' y 'Grado de estudio'
        '''
        # Llamo al método heredado para leer la base de datos
        base_salarios = self.__dataframe
        # Imputación utilizando pandas
        base_salarios['Salario base'] = base_salarios.groupby(['Género', 'Grado de estudio'])['Salario base'] \
                               .transform(lambda x: x.fillna(x.mean()))
        
        return base_salarios

#------------------------------------------------------------------------------------------------------- 

