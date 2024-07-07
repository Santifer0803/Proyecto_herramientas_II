
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
    
  def barras(self, df, variable_x, variable_y, num_ejercicio):
    
    
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
                
    num_ejercicio: int
                   numero del ejercicio a mostrar en el título del gráfico.
             
    Returns:
    --------
    None
    """
    
    fig = px.bar(df, x = variable_x, y = variable_y, color_discrete_sequence = ["#1f77b4"],
    title = f'Tiempos de ejecución por integrante - Ejercicio {num_ejercicio}')
    
    fig.update_layout(
      
      xaxis_title = 'Integrante',
      yaxis_title = 'Tiempo (segundos)',
      template = 'simple_white'
      
      )
      
    fig.show()

  def barras_agrupadas(self, df, variable_x, variable_y1, variable_y2, 
  nombres_leyendas, num_ejercicio):
    
    
    """
    Método que genera y muestra un gráfico de barras agrupadas a partir de un 
    DataFrame dado y 3 de sus columnas.

    Parameters:
    -----------
    df: pandas.DataFrame
        DataFrame que contiene los datos para el gráfico.
                          
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
                
    num_ejercicio: int
                   numero del ejercicio a mostrar en el título del gráfico.
             
    Returns:
    --------
    None
    """
    
    df_mod = df.melt(id_vars = [variable_x], value_vars = [variable_y1, variable_y2],
                     var_name = 'Variable', value_name = 'Valor')

    fig = px.bar(df_mod, x = variable_x, y = 'Valor', color = 'Variable', 
    barmode = 'group', color_discrete_map = {variable_y1: '#1f77b4', 
    variable_y2: '#ff7f0e'},
    title = f'Tiempos de ejecución por integrante - Ejercicio {num_ejercicio}')
    
    fig.update_layout(
      
      xaxis_title = 'Integrante',
      yaxis_title = 'Tiempo (segundos)',
      legend_title_text = nombres_leyendas[0],
      template = 'simple_white'
      
      )
      
    for i, trace in enumerate(fig.data):
      
      trace.name = nombres_leyendas[i+1]
      
    fig.show()




