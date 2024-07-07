
class GenerarGraficos:
  
  def __init__(self):

    """
    Constructor de la clase GenerarGraficos. Inicializa una nueva instancia
    de esta clase.

    Parameters:
    -----------
    None
             
    Returns:
    --------
    None
    """
    
  def grafico_barras(self, df, variable_x, variable_y):
    
    
    """
    Método que genera y muestra un gráfico de barras a partir de un DataFrame
    dado y 2 de sus columnas.

    Parameters:
    -----------
    df: pandas.DataFrame
        DataFrame que contiene los datos para el gráfico.
                          
    variable_x: str
                Nombre de la columna en el DataFrame que se utilizará como 
                la variable en el eje x.
                    
    variable_y: str
                Nombre de la columna en el DataFrame que se utilizará como 
                la variable en el eje y.
             
    Returns:
    --------
    None
    """
    
    px.bar(df, x = variable_x, y = variable_y).show()




