#' Función que genera un gráfico de barras a partir de una columna específica de
#' un DataFrame.
#'
#' @param df DataFrame que contiene los datos.
#' @param indice_col Índice de la columna o nombre de columna que se utilizará para
#' generar el gráfico.
#'
#' @return No retorna nada. Genera y muestra un objeto ggplot que representa el
#' gráfico de barras de la columna especificada.
fun.barras <- function(df, indice_col) {
  ggplot(data.frame(valor = df[[indice_col]]), aes(x = valor)) +
    geom_bar(fill = "skyblue") +
    labs(y = "Cantidad", caption = "Fuente: elaboración propia") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}
