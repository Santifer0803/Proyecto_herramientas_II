class GenerarDataframes():
    """
    Clase para generar dataframes a partir de listas de tiempos y nombres de integrantes.

    Attributes
    ----------
    integrantes : list
        Lista de nombres de los integrantes.
    
    Methods
    -------
    tiempos_simples(self, tiempos)
        Genera un dataframe con los nombres de los integrantes y sus tiempos simples.

    tiempos_dobles(self, nombre1, tiempos1, nombre2, tiempos2)
        Genera un dataframe con los nombres de los integrantes y dos series de tiempos.
    """
    
    def __init__(self, integrantes):
        """
        Constructor de la clase GenerarDataframes
        
        Parameters
        ----------
        integrantes : list
            Lista de nombres de los integrantes
        
        Returns
        -------
        None
        """
        self.__integrantes = integrantes
        
    @property
    def integrantes(self):
        """
        Método get de la clase GenerarDataframes
        
        Parameters
        ----------
        None
        
        Returns
        -------
        integrantes : list
            Lista de nombres de los integrantes
        """
        return self.__integrantes

    @integrantes.setter
    def integrantes(self, nuevos_integrantes):
        """
        Método set de la clase GenerarDataframes
        
        Parameters
        ----------
        nuevos_integrantes : list
            Nueva lista de nombres de los integrantes
        
        Returns
        -------
        None
        """
        self.__integrantes = nuevos_integrantes

    def __str__(self):
        """
        Devuelve una cadena de texto que resume la clase GenerarDataframes.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        cadena : str
            Texto explicativo que resume la clase GenerarDataframes
        """
        return f'Integrantes: {self.__integrantes}'




    def tiempos_simples(self, tiempos):
        """
        Genera un dataframe con los nombres de los integrantes y sus tiempos .
        
        Parameters
        ----------
        tiempos : list
            Lista de tiempos correspondientes a los integrantes
        
        Returns
        -------
        df : pandas.DataFrame
            DataFrame con los nombres de los integrantes y sus tiempos
        """
        
        dic = {
            'integrante' : self.__integrantes,
            'tiempo' : tiempos
        }
        df = pd.DataFrame(dic)
        return df

    def tiempos_dobles(self, nombre1, tiempos1, nombre2, tiempos2):
        """
        Genera un dataframe con los nombres de los integrantes y dos series de tiempos.
        
        Parameters
        ----------
        nombre1 : str
            Nombre de la primera serie de tiempos
        tiempos1 : list
            Lista de tiempos para la primera serie
        nombre2 : str
            Nombre de la segunda serie de tiempos
        tiempos2 : list
            Lista de tiempos para la segunda serie
        
        Returns
        -------
        df : pandas.DataFrame
            DataFrame con los nombres de los integrantes y dos series de tiempos
        """
        
        dic = {
            'integrante' : self.__integrantes,
            nombre1 : tiempos1,
            nombre2 : tiempos2
        }
        df = pd.DataFrame(dic)
        return df
