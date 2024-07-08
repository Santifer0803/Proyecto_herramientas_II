import pandas as pd
import timeit

class Madre:
    """
    Clase para heredar atributos y métodos a clases futuras

    Attributes
    ----------
    ruta : str
        una cadena de texto con una ruta de un archivo
    
    repeticiones : int
        numero de repeticiones para la ejecición de un módulo, por default es 10

    Methods
    -------
    leer_txt(self)
        Función que lee el contenido de un archivo de texto y 
        devuelve su contenido como un string
    
    leer_excel(self)
        Función que lee el contenido de un archivo de Excel y devuelve su 
        contendio en un Dataframe
    
    medir_tiempo(self, metodo_str)
        Función que mide el tiempo promedio por numero de repeticiones
        en la ejecución de un método de la clase
    
    transpuesta(self)
        Calcula la matriz transpuesta y devuelve el resultado
    """
    
    
    def __init__(self, ruta):
        ''' Constructor de la clase Madre
        
        Parameters
        ---------
        ruta : str
            Una cadena de texto con una ruta de un archivo
        
        Returns
        -----
        None
            Construye el objeto, pero no lo devuelve
        '''
        self.__ruta = ruta
        self.__repeticiones = 10

    
    @property
    def ruta(self):
        ''' Método get de la clase Madre
        
        Parameters
        ---------
        None
        
        Returns
        -----
        ruta : str
            Una cadena de texto con una ruta de un archivo
        '''
        return self.__ruta

    
    @ruta.setter
    def ruta(self, nueva_ruta):
        
        ''' Método set de la clase Madre
        
        Parameters
        ---------
        nueva_ruta : str
            Una cadena de texto con una ruta de un archivo
        
        Returns
        -----
        None
            Cambia el atributo ruta de un objeto de la clase Madre
        '''
        self.__ruta = nueva_ruta

    
    @property
    def repeticiones(self):
        ''' Método get de la clase Madre
        
        Parameters
        ---------
        None
        
        Returns
        -----
        repeticiones : int
            Numero de repeticiones para la ejecición de un módulo
        '''
        return self.__repeticiones

    
    @repeticiones.setter
    def repeticiones(self, nuevas_repeticiones):
        ''' Método set de la clase Madre
        
        Parameters
        ---------
        nuevas_repeticiones : int
            Numero de repeticiones para la ejecición de un módulo
        
        Returns
        -----
        None
            Cambia el atributo repeticiones de un objeto de la clase Madre
        '''
        self.__repeticiones = nuevas_repeticiones

    
    def __str__(self):
        ''' Texto explicando un resumen de la clase Madre
            
        Parameters
        ---------
        None
        
        Returns
        -----
        Cadena : str
            Texto explicativo que resume la clase Madre
        '''
        return f'Ruta:{self.__ruta} \nRepeticiones: {self.__repeticiones}'
    
    def leer_txt(self):
        '''
        Esta función abre un archivo de texto en modo de lectura, 
        lee todo su contenido y lo retorna como una cadena de texto.
        
        Parameters
        ---------
        None
        
        Returns:
        -------
        contenido: str
           Cadena de texto que contiene el contenido completo del archivo leído
        '''
        with open(self.__ruta, 'r') as archivo:
            contenido = archivo.read()
            return contenido

    def leer_excel(self):
        '''
        Esta función utiliza pandas para abrir un archivo de Excel en modo de lectura, 
        y carga su contenido en un DataFrame.
        
        Parameters
        ---------
        None
        
        Returns:
        -------
        contenido: pandas.DataFrame
           DataFrame que contiene los datos del archivo Excel leído
        '''
        contenido = pd.read_excel(self.__ruta, engine = 'openpyxl')
        return contenido
        
    def medir_tiempo(self, metodo_str):
        '''
        Función que mide el tiempo de ejecución de un método de la clase.
        Esta función toma el nombre del método y sus argumentos como una cadena, 
        construye y ejecuta esa llamada varias veces, y mide el tiempo promedio 
        de ejecución utilizando la función timeit.
    
        Parameters
        ----------
        metodo_str: str
           Cadena que contiene el nombre del método y los argumentos. 
           Ejemplo: "sumar(1,2)"
    
        Returns:
        -------
        tiempo: float
           Tiempo promedio de ejecución del método en segundos
        '''
        # Obtener el nombre del método y los argumentos de la cadena
        metodo_nombre, args_str = metodo_str.split('(', 1)
        args_str = args_str.rstrip(')')
        # Construir la cadena de código para ejecutar el método con los argumentos
        codigo = f"self.{metodo_nombre}({args_str})"
        # Medir el tiempo de ejecución
        tiempo = timeit.timeit(stmt=f"resultado = {codigo}", number=self.repeticiones, globals={'self': self}) / self.repeticiones
        return tiempo
