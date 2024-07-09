import pandas as pd
import plotly.express as px
import random

class GenerarGraficos:
  
  """
  Clase que representa la generación de gráficos a partir de un DataFrame.
  
  Attributes
  ----------
  df: pandas.DataFrame
      DataFrame que contiene los datos para el o los gráficos.
  
  Methods
  -------
  barras(self, variable_x, variable_y, titulo)
      Genera y muestra un gráfico de barras a partir del DataFrame actual y dos de sus columnas.
  
  barras_agrupadas(self, variable_x, variable_y1, variable_y2, nombres_leyendas, titulo)
      Genera y muestra un gráfico de barras agrupadas a partir del DataFrame actual y tres de sus columnas.
  """
  
  # Constructor
  def __init__(self, df):

    """
    Constructor de la clase GenerarGraficos. Inicializa una nueva instancia
    de esta clase.

    Parameters:
    -----------
    df: pandas.DataFrame
        DataFrame que contiene los datos para el o los gráficos.
             
    Returns:
    --------
    None
    """
    
    self.__df = df.copy()
    
  # Get
  @property
  def df(self):
    """
    Método get de la clase GenerarGraficos
        
    Parameters:
    ---------
    None
        
    Returns:
    -----
    df: pandas.DataFrame
        DataFrame actual que contiene los datos para el o los gráficos.
    """
    return self.__df
    
    
  # Set
  @df.setter
  def df(self, nuevo_df):
    """
    Método set de la clase GenerarGraficos
        
    Parameters:
    ---------
    nuevo_df: pandas.DataFrame
              Nuevo DataFrame con los datos para el o los gráficos.
        
    Returns:
    -----
    None
    Cambia el atributo vectores de un objeto de la clase Matriz
    """
    self.__df = nuevo_df
    
  # str
  def __str__(self):
    """
    Devuelve una representación legible en forma de cadena de la
    instancia de la clase
        
    Parameters:
    -----------
    None
               
    Returns:
    -------
      str: Texto que describe los atributos de la instancia.
    """
    return f'DataFrame actual: {self.__df}'
    
  def barras(self, variable_x, variable_y, titulo):
    
    """
    Método que genera y muestra un gráfico de barras a partir del DataFrame actual
    y 2 de sus columnas.

    Parameters:
    -----------
                          
    variable_x: str
                Nombre de la columna en el DataFrame que se utilizará como 
                la variable en el eje x.
                    
    variable_y: str
                Nombre de la columna en el DataFrame que se utilizará como 
                la variable en el eje y.
                
    titulo: str
            título que tendrá el gráfico
             
    Returns:
    --------
    None
    """
    
    def random_color():
    
      return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    
    fig = px.bar(self.__df, x = variable_x, y = variable_y, 
                 color_discrete_sequence = [random_color()], title = titulo)
    
    fig.update_layout(
      
      xaxis_title = 'Integrante',
      yaxis_title = 'Tiempo (segundos)',
      template = 'simple_white'
      
      )
      
    fig.show()

  def barras_agrupadas(self, variable_x, variable_y1, variable_y2, 
  nombres_leyendas, titulo):
    
    
    """
    Método que genera y muestra un gráfico de barras agrupadas a partir del
    DataFrame actual y 3 de sus columnas.

    Parameters:
    -----------
                          
    variable_x: str
                Nombre de la columna en el DataFrame que se utilizará como 
                la variable en el eje x.
                    
    variable_y1: str
                 Nombre de una columna en el DataFrame que se utilizará como 
                 variable en el eje y.
                
    variable_y2: str
                 Nombre de otra columna en el DataFrame que se utilizará como 
                 variable en el eje y.
                 
    nombres_leyendas: list
                      lista con el nombre de la leyenda y los nombres para las 
                      categorías en la leyenda. El primer elemento será el título 
                      de la leyenda y los siguientes elementos serán los nombres de 
                      las categorías.
                
    titulo: str
            título que tendrá el gráfico
             
    Returns:
    --------
    None
    """
    
    def random_color():
    
      return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    
    df_mod = self.__df.melt(id_vars = [variable_x], 
                            value_vars = [variable_y1, variable_y2], 
                            var_name = 'Variable', value_name = 'Valor')

    fig = px.bar(df_mod, x = variable_x, y = 'Valor', color = 'Variable', 
                 barmode = 'group', 
                 color_discrete_map = {variable_y1: random_color(), variable_y2: random_color()},
                 title = titulo)
    
    fig.update_layout(
      
      xaxis_title = 'Integrante',
      yaxis_title = 'Tiempo (segundos)',
      legend_title_text = nombres_leyendas[0],
      template = 'simple_white'
      
      )
      
    for i, trace in enumerate(fig.data):
      
      trace.name = nombres_leyendas[i+1]
      
    fig.show()



