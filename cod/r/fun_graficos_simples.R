#' Función que crea un gráfico de barras interactivo con el color y título
#' deseados, recibe un DataFrame de la función df.tiempos.
#'
#' @param df (DataFrame) DataFrame de la función df.tiempos.
#' @param color (Character) Color que tendrán las barras del gráfico.
#' @param titulo (Character) Título del gráfico.
#'
#' @return None
#'
graficos.simples <- function(df, color, titulo) {
  fig <- ggplot(df, aes(x = integrante, y = tiempo)) +
    geom_col(fill = color) +
    labs(
      x = "Integrante",
      y = "Tiempo (segundos)",
      title = titulo,
      caption = "Fuente: elaboración propia"
    ) +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
  ggplotly(fig, width = 800, height = 500)
}
