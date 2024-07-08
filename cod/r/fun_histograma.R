#' Función que genera un histograma a partir de una columna específica de un DataFrame.
#' 
#' @param df DataFrame que contiene los datos.
#' @param indice_col Índice de la columna o nombre de columna que se utilizará para 
#' generar el histograma.
#' 
#' @return No retorna nada. Genera y muestra un objeto ggplot que representa el 
#' histograma de la columna especificada.
fun.histograma <- function(df, indice_col){
  ggplot(data.frame(valor = df[[indice_col]]), aes(x = valor)) +
    geom_histogram(binwidth = 1, fill = "blue", color = "black") +
    labs(y = "Frecuencia", caption = "Fuente: elaboración propia") +
    theme_minimal()
}
